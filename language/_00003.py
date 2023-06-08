s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """ 
hello, 
world!
"""
print(s1, s2, s3, end='')

s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

print('\n')
s1 = 'hello'
# 字符串重复操作
print(s1 * 3)
# 字符串拼接
print(s1 + ' world')
# 字符串包含
print('ll' in s1)
print('lll' in s1)
print(len(s1))
# 字符串下标操作
s2 = 'abc123456'
print(s2[2])
print(s2[::2])
print(s2[:-1])
print(s2[0:5:1])
print(s2[::-1])
print(s2[::-2])

str1 = 'hello, World!'

print(len(str1))
print(str1.capitalize(), str1.title(), str1.upper(), str1.lower())
print(str1.find('llo'), str1.find('wor'))
print(str1.index('llo'))
print(str1.startswith('he'), str1.startswith('He'))
print(str1.endswith('d'), str1.endswith('orld!'))
str2 = str1.center(80, '*')
print(str2, str1.rjust(80, '-'), str1.ljust(80, '+'), sep='\n')
print(str2.strip('*'), str2.rstrip('*'), str2.lstrip('*'), sep='\n')
str3 = '1Hello2World'
print(str3.isalnum(), str3.isalpha(), str3.isascii(), str3.isdigit(), str3.isnumeric())
print(str1[:])
for x in str3:
    print(x)
for x in '你好，世界':
    print(x)


