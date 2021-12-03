import sys
from typing import Dict


def main():
    if len(sys.argv) != 3:
        print(f'USAGE: {sys.argv[0]} <students file> <comma separated list of names>')

    students: Dict[str, str] = {}
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            name, uni = line.split(':')
            students[name] = uni.strip()

    for name in sys.argv[2].split(','):
        try:
            print(f'Name: {name}, University: {students[name]}')
        except KeyError:
            print(f"No record of '{name}' was found!")


if __name__ == '__main__':
    main()
