import argparse

from claude_archive import archive


def main():
    parser = argparse.ArgumentParser(description="Claude 技巧文章历史回填")
    parser.add_argument("mode", nargs="?", default="history", choices=["history"])
    parser.add_argument("--days", type=int, default=30, help="回溯天数，默认30天")
    args = parser.parse_args()
    archive(days=args.days)


if __name__ == "__main__":
    main()
