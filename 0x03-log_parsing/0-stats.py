#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status
                code> <file size>
"""
import re
import sys
import traceback
db = {}
pattern = r"^((\d+(\.\d+){3})|\w+?)\s?\-\s?" +\
    r"(\[\d+(\-\d+){2}\s\d+(\:\d+\.?(\d+)?)" +\
    r"{2}\])\s(\"GET \/projects\/260 HTTP\/1.1\")" +\
    r"\s(\w+)\s(\d+)$"
code = [200, 301, 400, 401, 403, 404, 405, 500]
sum = 0


def print_stats():
    """
    Function that print stats about log
    """
    global sum

    print("File size: {}".format(sum))
    stcdor = sorted(db.items())
    for key, value in stcdor:
        print("{}: {:d}".format(key, value))


if __name__ == "__main__":
    count = 0
    try:
        for data in sys.stdin:
            count += 1
            log = data.rstrip()
            matches = re.findall(pattern, log)
            size = 0

            if matches is not None and len(matches) > 0:
                matches = list(matches[0])
                size = int(matches[-1])
                try:
                    status = int(matches[-2])

                    if status in code:
                        if db.get(status) is None:
                            db[status] = 0
                        db[status] += 1
                except ValueError:
                    pass
                sum += int(size)

            if count == 10:
                print_stats()
                count = 0
    except KeyboardInterrupt:
        print_stats()
        traceback.print_exc()
    else:
        print_stats()
