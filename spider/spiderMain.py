import pandas as pd
import requests
from lxml import etree
import re
import json
import csv
import os
import time
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()
from app.models import Travel
class spider(object):
    def __init__(self):
        self.url='https://piao.qunar.com/ticket/list.json?keyword=%s&page=%s'
        self.detailUrl='https://piao.qunar.com/ticket/detail_%s.html'
        self.headers={
        'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
        'cookie':'QN1=0000f300306c65c3ad488513; QN300=s%3Dbaidu; QN99=2443; QN269=585083F1838711EF863C1A212474A0FA; fid=927d12ad-fb0e-492b-a5a2-66ac790cc38c; ariaDefaultTheme=null; QN205=s%3Dbaidu; QunarGlobal=10.80.126.68_56f09d1b_19231efc53f_6f24|1728180383359; QN243=4; QN277=organic; QN57=17282041164930.4788689734406657; ctt_june=1683616182042##iK3wasg8WhPwawPwa%3DamEKt%2BXsDnVRETERThXPaNXKXmVKDNERDAaDDsEKkGiK3siK3saKgwVR38VKa%2BVKP8VuPwaUvt; ctf_june=1683616182042##iK3wWRj%2BWuPwawPwa%3DjNESD%3DaK3OEPfTESj%2BVRoRXS3sXSGIWKXAaSGRWSDsiK3siK3saKgwVR38VKamaR3AaUPwaUvt; cs_june=645007511c10e36bd9c2003611148160a611626a2eb3dc6ba38e9decc5d48240232c62578fa11534d15bc4581a655e132c1136fd3bdbd93b6c42dd272f0f0d55b17c80df7eee7c02a9c1a6a5b97c11798f450fda48a2c90f4c67f4d4f0638cae5a737ae180251ef5be23400b098dd8ca; QN271AC=register_pc; QN271SL=2cf5b868400580da078e89b82b7410cc; QN271RC=2cf5b868400580da078e89b82b7410cc; _q=U.pyiinov1225; csrfToken=oYglvnmPZlVEcggvdynT8cDkrkpIg2kp; _s=s_PEI6ZVP3LPFVCYTKPOYFLZY6WI; _t=28912930; _v=49cjQgqFvyZ2PU0ST8kXgc660qpfVdjxmAh8ZKUvEawI-zd6GnSfiheFBDhZktjChpY8sUTnx5DGSnf90RzMgWMZGhUoJGTiNBFLl9yB_hWFJbc5IekyeUEcCKbIClcdVaiolaJGTA_7k0vhtObKiALaEoFccBmP97mWBAzylZ-D; QN43=""; QN42=%E5%8E%BB%E5%93%AA%E5%84%BF%E7%94%A8%E6%88%B7; _i=VInJOyxEuq3CQYcqMgnyh4ViQAYq; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; QN44=pyiinov1225; QN48=tc_7d4a407ee03c4a5b_1927b280120_17e5; QN71="MjAyLjExMy4xMy41NTrljJfkuqw6MQ=="; _vi=iRETygtFAUG5v0QD7vnDlzFdfRiCB6_Mgwj9vFOZPzgqq6usUuTVCCLjgXc1dg9Df_a-CL9lOMu53-3koKFtfKmlWARCPkBLljC45koxegdozYkfTSasiGwDpQoJJcuPI14-PBcGyI_K_C-2yrZB_0AwOcPEKYVN8bRfOJcO8i4L; QN267=2141711564b94b39fb; QN58=1728656711874%7C1728657652749%7C4; QN271=f8d9589f-074f-4fe9-b2bb-fdf747d27d23; __qt=v1%7CVTJGc2RHVmtYMTlLVEcwR3BOc1dibkRKTWhFTlc5QWIzTVRNSVdZK0lrRmE3eXhvRGVibVAvdG1FZm85V294RUd2cW9NVVdTdnloUncxamNDcFpGZkRmTngxUUszWm5iY1ZnZGxlcEUzeWtEYlF5cUFmSVNia2JFQmJxWlViVFkwL2pvdXV6RGVsZVRGaDJTZHBaY25ZblhJU2NUL1Z0eU9aTnVTejlEQVNjPQ%3D%3D%7C1728657708715%7CVTJGc2RHVmtYMTl0T0JPMkxyOHhOL0o3b3RtQVp4bDNnK3NVNWdVVzNrTCtzamdIZkZ1dmJWQXNwNEFZUXVBWUhlZVU3dUdmN3kvN3AydnNrdmFHYXc9PQ%3D%3D%7CVTJGc2RHVmtYMTlWVUZBQ3J5NklRdEgzNlZYM0lsVGQwS3lnL204Nmd4NjdUbG9qVXdGQXhtUFJGQURDN2wxa3Jmc0U3ajV0UWprUE1EazE3ckJTWXZtc3BTSyt2QXNpY3hKTE1uWHMwOGd1aTBhY3BpYXhVVVFsNUVUa3B0b1JkS2UwbHZDQnB5dkMwVFBqcWRoN1lFdE9MWGVjeEF0MmY5WkNkSDczUDZJWHVxNzUzY2tUTFIrQU1MYkVxTzJ0aWZkZWd6MFJ2YlRnbUNlNFA0ak5jT2kxK1YyODlhNmx3eCtpeGFZR0ZjWDhIQUREK0FYeC91UkJ5R2MxNTc5TW13OWZhaU1oNWFvNGxPRTJpYXZuZzNJL2YwSnV5VGJmUWJ5K3NPWWRzbi9wNDdicFRDRWxVQUJ4WWpIN21RSjc3MVk5YktvaDE0UlY0Wm16WFlrRmNQY2VEQjhxRDFJUEU0bTdNMU4xRUN2TWo0L2VMWTZaNVR5Q0tvcDF6WEtrRy9sSFFUcXp6cGwvbmFSK09uUVROMmdQTzNzWHVCRlFETCsrV083dG50ZCt6MWQ2TGpkK1ZvL256dU15bVd6S3l4eDY5VXhERFU1S05HVmVNQVF0MFQxalA4UCtvcjF1NVZQTVpGK2lUTnZNZ25jTHFFWUhxYU1PZXNKTkhYZUFGLzE1U3lpWE1WY29OUzRaS3NRV0hZSUdYMWNkWUJZc2RCV0xhamhFclNYL3E4RnZta3VPZVU4WlRmTHBoWkROUFZodGVYUmVsbmhxUkRtRHJqNEZSNHRRZVhJUXJkY2dWVWMwSkdHWVM1OVlmcFR3Q004SDNpTWFKRlU3bXZYWHUxcEJWRTVmNXJ4T2JrSk9KQVh3TVNpZnVzclRvOGprSmxjeW1rSDNVRytVTnd2c1Z3OTNkdUVKZG5xU2lDQkp5WEs4MW9mejY1Sk02UkUyZUlxQVBCU0xlMlBTUUtDbXkrVVVscDE0bHJIL2pqM29kMHFWWUpCNlpDMzZ6Q2ZY; JSESSIONID=62559F0E5C2467F1B8B43B58C81F9397'
        }

    def init(self):
        if not os.path.exists('tempData.csv'):
            with open('tempData.csv', 'w', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([
                    'title',
                    'level',
                    'province',
                    'star',
                    'detailAddress',
                    'shortIntro',
                    'detailUrl',
                    'score',
                    'price',
                    'commentsLen',
                    'detailIntro',
                    'img_list',
                    'comments',
                    'cover',
                    'discount',
                    'saleCount'
                ])

    def send_request(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response
        else:
            return None


    def save_to_csv(self,row):
        with open('tempData.csv', 'a', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(row)
    def spiderMain(self,resp,province):
        respJson = resp.json()['data']['sightList']
        for travel in respJson:
            detailAddress=travel['address']
            discount=travel['discount']
            shortIntro=travel['intro']
            price=travel['qunarPrice']
            saleCount=travel['saleCount']
            try:
                star=travel['star']+'景区'
            except:
                star='未评价'
            title=travel['sightName']
            cover=travel['sightImgURL']
            sightId=travel['sightId']
            #--------------------------------详情页爬取
            detailUrl=self.detailUrl % sightId
            respDetailXpath=etree.HTML(self.send_request(detailUrl).text)
            score=respDetailXpath.xpath('//span[]')
            print(respDetailXpath,score)

    def start(self):
        with open('./city.csv', 'r', encoding='utf-8', newline='') as csvfile:
            readerCsv = csv.reader(csvfile)
            for cityData in readerCsv:
                for page in range(1,10):
                    url=self.url % (cityData[0],page)
                    print('正在爬取 %s 该城市旅游数据正在第 %s 页 路径为：%s' % (cityData[0],page,url))
                    reponse = self.send_request(url)
                    self.spiderMain(reponse,cityData[0])
                    break
                break
if __name__ == '__main__':
    spiderObj=spider()
    spiderObj.init()
    spiderObj.start()



def save_to_sql(self):
    with open('tempData.csv', 'a', encoding='utf8') as csvfile:
        readerCsv = csv.reader(csvfile)
        next(readerCsv)
        for travel in readerCsv:
            travel.objects.create(
                title=travel[0],
                level=travel[1],
                province=travel[2],
                star=travel[3],
                detailAddress=travel[4],
                shortIntro=travel[5],
                detailUrl=travel[6],
                score=travel[7],
                price=travel[8],
                commentsLen=travel[9],
                img_list =travel[10],
                comments=travel[11],
                cover =travel[12],
                discount=travel[14],
                saleCount=travel[15],
            )
