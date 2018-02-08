###################################### 네이버 검색 Open API 예제 - 블로그 검색

import urllib.request
import json

client_id = "R1JCmA0iVfg4x_ecHHkN"
client_secret = "EycJ4UgDEA"
input_text = urllib.parse.quote("우동")
recipe_text = urllib.parse.quote(" 레시피")
enc_text = input_text + recipe_text

url = "https://openapi.naver.com/v1/search/blog?query=" + enc_text # JSon_ 결과

req = urllib.request.Request(url)

req.add_header("X-Naver-Client-Id",client_id)
req.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(req)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


"http://blog.naver.com/theboni?Redirect=Log&amp;logNo=221065338934"

"https://theboni.blog.me/221065338934?Redirect=Log&from=postView"

"https://blog.naver.com/theboni/221065338934"

"http://blog.naver.com/dngusghk?Redirect=Log&amp;logNo=221161588949"
"https://blog.naver.com/dngusghk/221161588949"