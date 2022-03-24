import requests
from selenium import webdriver

url='http://api.tianqiip.com/getip?secret=b37g81m5b7vjkrvk&type=txt&num=1&time=3&port=1'
req=requests.request(method='GET',url=url)
print(req.text)