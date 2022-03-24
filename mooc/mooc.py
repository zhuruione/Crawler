import requests
import json
from bs4 import BeautifulSoup

def get_video_url(url):
    video_url_data=requests.get(url)
    data=json.loads(video_url_data.text)
    video_url=[]
    for each in data['result']['videos']:
        video_url.append(each['videoUrl'])
    return video_url


def get_video_data(url):
    video_data_req=requests.get(url,stream=True)

    video_size=int(video_data_req.headers['Content-Length'])
    bs=0
    with open("E:/Desktop/test.mp4",'wb') as v:
        for b in video_data_req.iter_content(chunk_size=1024*1024):
            bs+=len(b)
            print('\r',bs/video_size*100,'%',end='',flush=True)
            v.write(b)


url='https://vod.study.163.com/eds/api/v1/vod/video?videoId=1004231003&signature=414a764953312b7257576355773941666d45753056776d736c73477246766348356a32526e55766d555a67367862616f7a79652f436342796730763748594d4744514564345a593336654d506e33716d7735546a36337867375a6831652f7a6b693056674b4c4c4a6c56774d394f77617035524d39327a6a53677a6741646c35625243474d524a61787178664d6663635a3145572b773d3d&clientType=1'
video_url=get_video_url(url)
print(video_url[0])
get_video_data(video_url[0])
