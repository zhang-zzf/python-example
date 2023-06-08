import hashlib

url = 'https://www.baidu.com'

md5_ = hashlib.md5()
md5_.update(url.encode())
hex_digest = md5_.hexdigest()
print(hex_digest)
