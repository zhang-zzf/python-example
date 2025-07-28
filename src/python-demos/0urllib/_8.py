import datetime
import re
from pathlib import PurePosixPath
from urllib.parse import urlparse, ParseResult

str = '''<script>
	   	        	 <!--
	   	      document.write(strencode2("%3c%61%20%74%61%72%67%65%74%3d%62%6c%61%6e%6b%20%68%72%65%66%3d%68%74%74%70%73%3a%2f%2f%63%6e%73%2e%6b%69%6c%6c%63%6f%76%69%64%32%30%32%31%2e%63%6f%6d%2f%6d%70%34%68%64%2f%37%37%35%31%34%32%2e%6d%70%34%3f%73%74%3d%4a%6c%66%46%51%54%62%46%31%53%4b%6b%59%38%33%75%4b%61%7a%41%6f%41%26%65%3d%31%36%37%36%38%38%30%36%31%35%3e"));
	   	        	 //-->
		  </script>'''

print(re.search(r'"(.*)"', str).group(1))

url = 'https://cns.killcovid2021.com/mp43/774507.mp4?st=KVbo3pCb9gPvcW4padc8Og&e=1676856025'
print(urlparse(url).path.split('/')[-1])

print(PurePosixPath(urlparse(url).path).name)

print(datetime.date.today())

print('55777.mp4'.split('.')[1])
