#!/usr/bin/python3
""" Script that converts Markdown to HTML """


import sys
import os


def markdown2html():
    """
    Script that converts Markdown to HTML

    Args:
        First argument is the name of the Markdown file.
        Second argument is the output file name.

    Returns:
        Nothing.
    """
    if (len(sys.argv) < 3):
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not(os.path.isfile("./{}".format(md_file))):
        sys.stderr.write("Missing " + sys.argv[1] + '\n')
        exit(1)

    exit(0)

if __name__ == "__main__":
    markdown2html()
