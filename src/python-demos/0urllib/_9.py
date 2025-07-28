import datetime
import os


def _remove():
    with open('a_file', 'w') as file:
        file.write('Hello, World!\n')
        file.write(str(datetime.datetime.now()))
    # os.remove('a_file')


def _open_not_exist():
    with open('a_file', 'r') as file:
        line = file.readline()
        print(line)


a = ''
print(type(a))
if __name__ == '__main__':
    _remove()
    # _open_not_exist()
