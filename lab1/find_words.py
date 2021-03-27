import sys
import os
import re
from typing import Optional

FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "find_words_file.txt")


def find_words(words: Optional[list]):
    """Find how many times the words are repeated in provided file."""
    if not words:
        sys.exit("No words provided")

    try:
        file = open(FILE_NAME, "r", encoding="utf8")
    except IOError:
        sys.exit("File does not exist")

    words_dict = {w: 0 for w in words if re.match(r"\w+", w) is not None}

    find_re = re.compile(r"\b\w+\b")
    for line in file:
        for word in find_re.findall(line):
            if word in words_dict.keys():
                words_dict[word] += 1
    file.close()
    print("\n".join([f"{key}: {value}" for key, value in words_dict.items()]))