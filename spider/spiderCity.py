import requests
from lxml import etree
import csv
import os
def init():
    if not os.path.exists('tempData.csv'):
       with open('tempData.csv', 'w', encoding='utf-8',newline='') as csvfile:
           writer = csv.writer(csvfile)
           writer.writerow([
              'city',
              'citylink',

           ])
def writerRow(row):
    with open('city.csv', 'a', encoding='utf-8', newline='') as csvfile:
     writer = csv.writer(csvfile)
     writer.writerow(row)
def get_html(url):
    headers={
        'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
        'cookie':'QN1=0000f300306c65c3ad488513; QN300=s%3Dbaidu; QN99=2443; QN269=585083F1838711EF863C1A212474A0FA; fid=927d12ad-fb0e-492b-a5a2-66ac790cc38c; ariaDefaultTheme=null; QN205=s%3Dbaidu; QunarGlobal=10.80.126.68_56f09d1b_19231efc53f_6f24|1728180383359; QN243=4; QN277=organic; QN57=17282041164930.4788689734406657; ctt_june=1683616182042##iK3wasg8WhPwawPwa%3DamEKt%2BXsDnVRETERThXPaNXKXmVKDNERDAaDDsEKkGiK3siK3saKgwVR38VKa%2BVKP8VuPwaUvt; ctf_june=1683616182042##iK3wWRj%2BWuPwawPwa%3DjNESD%3DaK3OEPfTESj%2BVRoRXS3sXSGIWKXAaSGRWSDsiK3siK3saKgwVR38VKamaR3AaUPwaUvt; cs_june=645007511c10e36bd9c2003611148160a611626a2eb3dc6ba38e9decc5d48240232c62578fa11534d15bc4581a655e132c1136fd3bdbd93b6c42dd272f0f0d55b17c80df7eee7c02a9c1a6a5b97c11798f450fda48a2c90f4c67f4d4f0638cae5a737ae180251ef5be23400b098dd8ca; QN271AC=register_pc; QN271SL=2cf5b868400580da078e89b82b7410cc; QN271RC=2cf5b868400580da078e89b82b7410cc; _q=U.pyiinov1225; csrfToken=oYglvnmPZlVEcggvdynT8cDkrkpIg2kp; _s=s_PEI6ZVP3LPFVCYTKPOYFLZY6WI; _t=28912930; _v=49cjQgqFvyZ2PU0ST8kXgc660qpfVdjxmAh8ZKUvEawI-zd6GnSfiheFBDhZktjChpY8sUTnx5DGSnf90RzMgWMZGhUoJGTiNBFLl9yB_hWFJbc5IekyeUEcCKbIClcdVaiolaJGTA_7k0vhtObKiALaEoFccBmP97mWBAzylZ-D; QN43=""; QN42=%E5%8E%BB%E5%93%AA%E5%84%BF%E7%94%A8%E6%88%B7; _i=VInJOyxEuq3CQYcqMgnyh4ViQAYq; QN71="MjAyLjExMy4xMy41NTrlpKnmtKU6MQ=="; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; QN44=pyiinov1225; _vi=sXd3fS-xurU1sp0kdaxdN38g_9fxNyxtLhSPPmkdFoaORrN3mnW7QBGEtWc4Jb2OBjvKRcWUo6fOrhhvL7C-3SA_sYq_jH3aHB-eUxc_iDXVAJAelPN2vlDZfVzV-2U3d7uwJsDBSDoMB7O1lxIso2_UYY4voXCchIZ5GYMnZQrh; QN48=tc_7d4a407ee03c4a5b_1927b280120_17e5; QN271=16008f9b-0b0e-431f-a223-7e4e383c6d03; QN267=21417115647f062801; QN58=1728641111386%7C1728643074265%7C11; JSESSIONID=C0581B7ABC72928F33AA08B14C7E8C3F; __qt=v1%7CVTJGc2RHVmtYMTloRlhaaXZnNTg3Z2dNTjhEUksycXJyT1Q3TTRHZnVjQmlqWGRERzF2bjV2RVl4ak4vZ1lPTktBWGxiRzNhVVBoTzNEK1d2Q2RoSnNsUWd5WGlBSEp5LzdGZWh3NnY3amtXb2lNbnJRMGVMWC9SV1dhalJTSThUSmZmNHNEN0IydWlzV0dDUFNXWDE5aXh3RHZDNWROdXFwckJyZWI5RFlrPQ%3D%3D%7C1728643088303%7CVTJGc2RHVmtYMStYWkIxNVRuSyttL1hNQkhNZVROeGdhUGVvY3RhQnZvamN2eXNkeDFHcFhLUDErc3M5MStWejByOTlheDdDMDNtVXA3ZDgxUDY3Qmc9PQ%3D%3D%7CVTJGc2RHVmtYMTlkd01la29TdlJyeFdKOTVOQkJJRklmMGRENDRIenFDQTNPQkxUUnUvYjNqc1ZoRENCWjZSRmhuazgzZmlJYlFySzJabFIrNytNUGJGL3c4M2xvMlVnRk43R282azRjdllZeHdDTzlqVGd4ZnhidVRXMWR6dlVRNjJaWGhZc2JRWWxIRlFZZEZuUjRTOWRTZkowV3hWNUg1UVBOdGxYZXNkOUduY2E0YmRsWWhCUmxiMVVldE1RZDE3TU8vc3RxcHZqVjhYZFQ4blM5cEVaRm0xNWxvMHFkQ3dlL0wza1NEUzkyTzMxR09KZjBsd3dPY1NRV1Z5N0VSdnVyL1ZGcDZydVdoazVnb1V5QTFwSitQOGRCVkZDeXIzR2lNNUc4ZEJNUmdxMnFPYXMzeHkxRnFQVlppYzVsUy9SYzFkTU9tbTFsdjFYbkFnNFRoRjNtdmRaYWlTa04vaWlHa3MybCszdWtkd0c4R21XMXA3Y0cxMWVhdGQ1WVAwVCtGZ2ZCMVU1c2ErTWRBOU52QlN1VjQ1N3lUU1ZPZi9rT09uM0wzdUVGSytXNXlYZTBneU4zVGZicXNIUjZUUkNlWDZaRm0vRFkxUjdpaXFLRlJ5NGwrdzNHZHV5dXgyaEFQUVpOYkcxZUw5ZU4vdGZucXNseUxDaHhob2pEbVFPTDNvcEpCYldreVdpaytCSGxScUY3Kzk3YTZ4eVErYjR2U1FNNkRkZGxKM0VqN2kzaThNb1pSRUkreFo3MkZjUTZUcVVoSnhGRkY0eEJFMFl3RFJDTlpValA5dUxuOVhNYTA3V2dFaWd6YlQzQjZ6QUI5TlM4MU5zcXhYWXI2M0kxMEt0d1FDT1liK08ydE9aNSsySHhUZ3o0QWlZaDFLWUtLSFoyN0NOVndsTDFPWnZvWitxUE5FT0x1eFEwVUZQM0N3dWNaSWNNdExQMUkrcTYrMURYMVNYNnZ5NzFXSHUzWkNtNzJrQzRoTk5FTENqNjRXNU13eitveUEv'

    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response
    else:
        return None
def pasre_html(response):
    root=etree.HTML(response.text)
    citylist=root.xpath('//div[@class="mp-city-content"]//li[@class="mp-city-item"]/a')
    for city in citylist:
        cityName=city.text
        cityLink='http://piao.qunar.com/daytrip/list.htm?keyword=%s' % cityName
        writerRow(
            [
                cityName,
                cityLink
            ]
        )
        print( cityName,
                cityLink)
if __name__ == '__main__':
    url='https://piao.qunar.com/daytrip/list.htm'
    init()
    response=get_html(url)
    pasre_html(response)