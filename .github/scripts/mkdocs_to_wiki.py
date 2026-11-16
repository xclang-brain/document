"""Convert an MkDocs docs tree into GitHub Wiki pages.

Usage: python mkdocs_to_wiki.py <mkdocs_dir> <wiki_dir>
"""
import re
import shutil
import sys
from pathlib import Path

import yaml


def page_name(title: str, is_home: bool) -> str:
    # Periods in wiki page names can break URLs, so drop them.
    return "Home" if is_home else title.replace(".", "").replace(" ", "-")


def main(src_dir: str, wiki_dir: str) -> None:
    src = Path(src_dir)
    wiki = Path(wiki_dir)
    # mkdocs.yml contains !!python/name tags (e.g. the mermaid fence); ignore them.
    loader = type("Loader", (yaml.SafeLoader,), {})
    loader.add_multi_constructor("tag:yaml.org,2002:python/", lambda l, s, n: None)
    conf = yaml.load((src / "mkdocs.yml").read_text(encoding="utf-8"), Loader=loader)
    nav = [next(iter(item.items())) for item in conf["nav"]]

    # Remove previously generated content (keep .git)
    for p in wiki.iterdir():
        if p.name == ".git":
            continue
        shutil.rmtree(p) if p.is_dir() else p.unlink()

    names = {md: page_name(title, i == 0) for i, (title, md) in enumerate(nav)}

    def fix_links(text: str) -> str:
        def repl(m):
            target = m.group(2)
            path, _, anchor = target.partition("#")
            if path in names:
                return f"]({names[path]}{'#' + anchor if anchor else ''})"
            return m.group(0)
        return re.sub(r"\]\((([^)\s]+))\)", repl, text)

    for md, name in names.items():
        text = (src / "docs" / md).read_text(encoding="utf-8")
        if name != "Home":
            # The wiki shows the page name as the title; drop the duplicate H1.
            text = re.sub(r"\A# .*\n+", "", text)
        (wiki / f"{name}.md").write_text(fix_links(text), encoding="utf-8")

    img = src / "docs" / "img"
    if img.is_dir():
        shutil.copytree(img, wiki / "img")

    sidebar = "\n".join(
        f"- [{title}]({names[md]})" for title, md in nav
    )
    (wiki / "_Sidebar.md").write_text(sidebar + "\n", encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
