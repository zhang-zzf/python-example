from urllib import parse

# encode
encoded_params: str = parse.urlencode({'wd': '爬虫'})
print(encoded_params)
url: str = "https://www.baidu.com/s?" + encoded_params
print(url)

unquote: str = parse.unquote(url)
print(unquote)

# result -> ws%3D%E7%88%AC%E8%99%AB
encoded_params = parse.quote("爬虫")
print(encoded_params)
url = 'https://www.baidu.com/s?wd={}'.format(encoded_params)
print(url)
print(parse.unquote(url))

str = '%3c%61%20%74%61%72%67%65%74%3d%62%6c%61%6e%6b%20%68%72%65%66%3d%68%74%74%70%73%3a%2f%2f%63%6e%73%2e%6b%69%6c%6c%63%6f%76%69%64%32%30%32%31%2e%63%6f%6d%2f%6d%70%34%68%64%2f%37%37%35%31%34%32%2e%6d%70%34%3f%73%74%3d%6d%79%6a%6e%6d%75%66%4b%6f%63%45%32%4b%31%65%70%36%41%74%5a%6d%67%26%65%3d%31%36%37%36%38%37%36%32%35%38%3e'

str = parse.unquote(str)
print(str)
