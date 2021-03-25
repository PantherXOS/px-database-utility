from sys import stdout

import px_database_utility


def main():
    res = px_database_utility.main()
    stdout.flush()
    if isinstance(res, str):
        stdout.write(res)
    else:
        stdout.buffer.write(res)
    stdout.flush()

if __name__ == '__main__':
    main()
