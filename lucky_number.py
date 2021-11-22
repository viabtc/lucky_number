#!/usr/bin/env python3

import sys
import random


def main(seeds, start_num, end_num, count):
    results = set()
    random.seed(int(seeds, 16))
    while len(results) < count:
        r = random.randint(start_num, end_num)
        results.add(r)

    for item in sorted(results):
        print(item)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
