import os
import time


def main():
    content = '北京欢迎你，为你开天辟地。。。'.center(80, '*')
    while True:
        os.system('clear')
        print(content)
        content = content[1:] + content[0]
        time.sleep(0.5)


if __name__ == '__main__':
    main()
