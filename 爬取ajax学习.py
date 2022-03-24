import requests
import json
def get_data(key,page):
    data={
        "key":key,
        "page":page
    }
    url='https://data.variflight.com/analytics/Codeapi/airportCode'
    res=requests.request('post',url,data=data)
    return res.text
def parse_data(data):
    return json.loads(data)
data=get_data('pek','0')
j=parse_data(data)
print(j)