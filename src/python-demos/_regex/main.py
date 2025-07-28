# This is a sample Python script.
import re
from pathlib import Path


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def read_file(file_name: str) -> str:
    return Path(file_name).read_text()


def regex_ut():
    text = read_file('ZxfbSpider.html')
    # re.S  -> `.` 匹配换行符
    match = re.search(r'initPubProperty\((.*?)\)', text, re.S)
    # 选择 `()` 内的内容
    # 以 `\W` 分割字符串，并去除空字符串
    # strip() 可以去除 `\n`
    raw_arg_vals: list[str] = [arg.strip() for arg in re.split(r',', match.group(1)) if arg != '']
    args_name = ['siteCode', 'tab', 'qt', 'debug', 'page', 'pageSize', 'timestamp', 'wordToken', 'tabToken', 'tagParam', 'apiUrl', 'auto', 'multiSelect', 'suid']
    processed_arg_vals = [
        arg[1:-1] if arg.startswith("'") and arg.endswith("'") else arg
        for arg in raw_arg_vals
    ]
    # 构建字典 合并2个列表
    args = {name: val for name, val in zip(args_name, processed_arg_vals)}
    print(args)
    print(args['wordToken'])


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def main():
    # print_hi('PyCharm')
    regex_ut()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
