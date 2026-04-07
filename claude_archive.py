import argparse
import datetime as dt
import html
import json
import os
import re
import urllib.parse
import xml.etree.ElementTree as ET

import requests


DATA_FILE = "data.json"
DOC_DIR = "doc"

RSS_QUERIES = [
    "Claude 技巧",
    "Claude 提示词",
    "Claude prompt tips",
    "Claude workflow",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
}

CLAUDE_PATTERN = re.compile(r"\bclaude\b", re.I)
TIPS_PATTERN = re.compile(
    r"(技巧|提示词|教程|实战|攻略|tips?|workflow|best practice|prompt)", re.I
)


def write_json(path, data, encoding="utf8"):
    with open(path, "w", encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def read_json(path, default_data=None, encoding="utf8"):
    if default_data is None:
        default_data = {}
    if os.path.exists(path):
        try:
            with open(path, "r", encoding=encoding) as f:
                return json.load(f)
        except Exception:
            write_json(path, default_data, encoding=encoding)
            return default_data
    write_json(path, default_data, encoding=encoding)
    return default_data


def sanitize_filename(name: str) -> str:
    name = re.sub(r"[\/\\:\*\?\"<>\|]", "", name).strip()
    name = re.sub(r"\s+", " ", name)
    return name[:120] or "untitled"


def parse_pub_date(text: str) -> dt.datetime:
    if not text:
        return dt.datetime.now(dt.timezone.utc)
    from email.utils import parsedate_to_datetime

    try:
        value = parsedate_to_datetime(text)
        if value.tzinfo is None:
            return value.replace(tzinfo=dt.timezone.utc)
        return value
    except Exception:
        return dt.datetime.now(dt.timezone.utc)


def extract_real_url(link: str) -> str:
    if not link:
        return ""
    parsed = urllib.parse.urlparse(link)
    if "bing.com" in parsed.netloc and parsed.path.endswith("/apiclick.aspx"):
        q = urllib.parse.parse_qs(parsed.query)
        target = q.get("url", [""])[0]
        return urllib.parse.unquote(target) if target else link
    return link


def match_claude_tips(title: str, desc: str) -> bool:
    text = f"{title} {desc}"
    return bool(CLAUDE_PATTERN.search(text) and TIPS_PATTERN.search(text))


def fetch_rss_items(query: str):
    rss_url = "https://www.bing.com/news/search"
    params = {"q": query, "format": "RSS"}
    resp = requests.get(rss_url, params=params, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    root = ET.fromstring(resp.text)
    items = []
    for item in root.findall("./channel/item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        desc = (item.findtext("description") or "").strip()
        source = (item.findtext("source") or "").strip()
        pub_text = (item.findtext("pubDate") or "").strip()
        pub_date = parse_pub_date(pub_text)
        real_url = extract_real_url(link)
        if not real_url:
            continue
        if not match_claude_tips(title, desc):
            continue
        items.append(
            {
                "title": html.unescape(title),
                "url": real_url,
                "source": html.unescape(source),
                "description": html.unescape(desc),
                "published_at": pub_date.astimezone(dt.timezone.utc),
            }
        )
    return items


def to_reader_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    rebuilt = parsed.netloc + parsed.path
    if parsed.query:
        rebuilt += f"?{parsed.query}"
    return f"https://r.jina.ai/http://{rebuilt}"


def fetch_markdown(url: str) -> str:
    reader_url = to_reader_url(url)
    resp = requests.get(reader_url, headers=HEADERS, timeout=45)
    if resp.status_code == 200 and len(resp.text.strip()) > 300:
        return resp.text.strip()
    raise RuntimeError(f"reader fetch failed: {resp.status_code}")


def archive(days: int = 1, max_items: int = 80):
    now_utc = dt.datetime.now(dt.timezone.utc)
    cutoff = now_utc - dt.timedelta(days=max(days, 1))

    all_items = []
    for q in RSS_QUERIES:
        try:
            all_items.extend(fetch_rss_items(q))
        except Exception as e:
            print(f"[WARN] RSS 拉取失败: {q} -> {e}")

    dedup = {}
    for item in all_items:
        if item["published_at"] < cutoff:
            continue
        dedup[item["url"]] = item

    items = sorted(dedup.values(), key=lambda x: x["published_at"], reverse=True)[:max_items]
    if not items:
        print("今天没有抓到新的 Claude 技巧文章")
        return []

    os.makedirs(DOC_DIR, exist_ok=True)
    data = read_json(DATA_FILE, {})
    saved = []

    for item in items:
        if item["url"] in data:
            continue
        try:
            content = fetch_markdown(item["url"])
        except Exception as e:
            print(f"[WARN] 文章抓取失败: {item['url']} -> {e}")
            continue

        pub_local = item["published_at"].astimezone()
        day_dir = os.path.join(DOC_DIR, pub_local.strftime("%Y-%m-%d"))
        os.makedirs(day_dir, exist_ok=True)

        filename = sanitize_filename(item["title"]) + ".md"
        file_path = os.path.join(day_dir, filename)
        if os.path.exists(file_path):
            base = os.path.splitext(filename)[0]
            file_path = os.path.join(day_dir, f"{base}-{int(dt.datetime.now().timestamp())}.md")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {item['title']}\n\n")
            f.write(f"- 来源: {item['source'] or '未知'}\n")
            f.write(f"- 发布时间(UTC): {item['published_at'].strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"- 原文链接: {item['url']}\n\n")
            f.write("----\n\n")
            f.write(content)

        rel_path = os.path.relpath(file_path, ".")
        data[item["url"]] = {
            "title": item["title"],
            "file": rel_path.replace("\\", "/"),
            "source": item["source"],
            "published_at": item["published_at"].isoformat(),
            "archived_at": now_utc.isoformat(),
        }
        write_json(DATA_FILE, data)
        saved.append(item["title"])
        print(item["title"], end="、")

    if not saved:
        print("今天没有新增归档（可能都已抓取过）")
    return saved


def main():
    parser = argparse.ArgumentParser(description="Claude 技巧文章归档")
    parser.add_argument("mode", nargs="?", default="today", choices=["today", "history"])
    parser.add_argument("--days", type=int, default=30, help="history模式下回溯天数")
    args = parser.parse_args()

    if args.mode == "today":
        archive(days=1)
    else:
        archive(days=args.days)


if __name__ == "__main__":
    main()
