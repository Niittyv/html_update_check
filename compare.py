from bs4 import BeautifulSoup
from pathlib import Path
import difflib
import sys


def normalize_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.prettify().splitlines()


def compare_html(local_file, local_file2):

    local_html = Path(local_file).read_text(encoding="utf-8")
    local_html2 = Path(local_file2).read_text(encoding="utf-8")

    local_lines = normalize_html(local_html)
    remote_lines = normalize_html(local_html2)

    diff = difflib.unified_diff(
        local_lines,
        remote_lines,
        fromfile="Local HTML",
        tofile="Remote HTML",
        lineterm=""
    )

    result = list(diff)

    output_file = "compare_result.txt"
    print("\n".join(result) if result else "No HTML differences found.")

    with open(output_file, "w", encoding="utf-8") as f:
        if result:
            f.write("\n".join(result))
        else:
            f.write("No HTML differences found.")


if __name__ == "__main__":
    compare_html(sys.argv[1], sys.argv[2])
