#!/usr/bin/python3
""" Script that converts Markdown to HTML
    Args:
        First argument is the name of the Markdown file.
        Second argument is the output file name.
"""

import sys
import os


def markdownToHtml():
    if (len(sys.argv) < 3):
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not(os.path.isfile("./{}".format(md_file))):
        print("Missing {}".format(md_file), file=sys.stderr)
        exit(1)

    exit(0)

if __name__ == "__main__":
    markdownToHtml()
