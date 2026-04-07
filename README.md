# Claude 技巧文章归档

[![GitHub Actions](https://github.com/gelusus/wxvl/actions/workflows/update_today.yml/badge.svg)](https://github.com/gelusus/wxvl/actions)

本项目已改为：**每天自动抓取 Claude 使用技巧相关文章并归档为 Markdown**。

## 功能

- 每天从 Bing News RSS 按关键词抓取 Claude 技巧文章
- 自动筛选（需同时命中 `Claude` + `技巧/提示词/tips/workflow`）
- 通过 `r.jina.ai` 提取正文 Markdown
- 按天归档到 `doc/YYYY-MM-DD/`
- `data.json` 去重，避免重复归档

## 使用

```bash
# 抓取当天新增
python run.py

# 回填近30天历史（可改天数）
python run_history.py history --days 30
```

## 目录结构

```text
doc/
  2026-04-07/
    xxx.md
data.json
```
