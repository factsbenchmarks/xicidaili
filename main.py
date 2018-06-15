import requests
from bs4 import BeautifulSoup
from requests.exceptions import ProxyError,ConnectionError
URL = 'http://www.xicidaili.com/'
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
}
r = requests.get(url=URL,headers=HEADERS)
f = open('proxy','w')
if r.status_code == 200:
    soup = BeautifulSoup(r.text,'lxml')
    trs = soup.select('table#ip_list > tr')
    trs = trs[2:]
    for tr in trs:
        try:
            ip = tr.select('td:nth-of-type(2)')[0].text
            port = tr.select('td:nth-of-type(3)')[0].text
            type = tr.select('td:nth-of-type(6)')[0].text.lower()

            proxy = '{}:{}'.format(ip,port)

            if type in ['https','http']:
                try:
                    r = requests.get(url='https://www.baidu.com',proxies={type:proxy},timeout=5)
                    if r.status_code == 200:
                        f.write("ip:{}    port:{}    type:{}".format(ip,port,type))
                        f.write('\n')
                except:
                    pass
        except IndexError as e:
            continue
    f.close()



