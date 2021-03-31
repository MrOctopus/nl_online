import sys

from os import path
from os import makedirs
from datetime import datetime

FORMAT = "%a %b %d %H:%M:%S %Y"

def main():
    if not len(sys.argv) == 3:
        exit(1)

    if path.isdir(sys.argv[2]):
        exit(1)

    file = None

    if not path.isfile(sys.argv[2]):
        makedirs(path.dirname(sys.argv[2]), exist_ok=True)
        file = open(sys.argv[2], 'w+')
    else:
        file = open(sys.argv[2], "r+")

    line = file.readline()

    old_date = None
    new_date = datetime.strptime(' '.join(sys.argv[1].split(' ')[:-1]), FORMAT)

    if not line:
        old_date = datetime.fromisoformat('1900-01-01')
    else:
        old_date = datetime.strptime(line, FORMAT)

    if new_date <= old_date:
        file.close()
        exit(1)
    else:
        file.seek(0, 0)
        file.write(new_date.strftime(FORMAT))
        file.close()

if __name__ == "__main__":
    """
        Usage: compare_git_timestamps.py TIME FILE
        TIME should be derived from git log -1 --format=%cd
        FILE can be an existing file or a file path
    """
    main()