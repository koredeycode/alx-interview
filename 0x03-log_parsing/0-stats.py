#!/usr/bin/python3
"""
module documentation
"""

import sys
import re


def main():
    """
    main function
    """
    p = r'^([\d.]+) - \[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+)$'
    pattern = p
    count = 0
    size = 0
    stats = {}
    try:
        for line in sys.stdin:
            line = line.strip()
            if not re.match(pattern, line):
                continue

            match = re.match(pattern, line)
            file_size = int(match.group(4))
            status_code = int(match.group(3))

            size += file_size
            stats[status_code] = stats.get(status_code, 0) + 1
            count += 1
            if count % 10 == 0:
                print("File size: {}".format(size))
                for code in sorted(stats.keys()):
                    print("{}: {}".format(code, stats[code]))
        print("File size: {}".format(size))
        for code in sorted(stats.keys()):
            print("{}: {}".format(code, stats[code]))
    except KeyboardInterrupt:
        print("File size: {}".format(size))
        for code in sorted(stats.keys()):
            print("{}: {}".format(code, stats[code]))


if __name__ == "__main__":
    main()
