import re
import requests
import os
import scrapy
import json
from zhihuphoto1.items import Zhihuphoto1Item
from bs4 import BeautifulSoup
class zhihuspider(scrapy.Spider):
    start_urls=["https://www.zhihu.com/api/v4/questions/37787176/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&limit=20&sort_by=default&offset="]
    name = "zhihu"
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    }
    html = requests.get('https://www.zhihu.com/question/37787176', headers=header)
    result = BeautifulSoup(html.text, 'lxml')
    count = result.find('meta', attrs={'itemprop': re.compile('answerCount')}).attrs['content']
    def start_requests(self):
        num = [x for x in range(0, int(self.count)) if x % 20 == 0]
        for i in num:
            yield self.make_requests_from_url(self.start_urls[0]+str(i))
    def parse(self,response):
        photos=[]
        pattern = re.compile('https://pic[1-4]\.zhimg\.com\/[a-z0-9-/_]*?_hd\.jpe?g')
        jsondata=json.loads(response.body.decode("utf-8"))
        for tt in jsondata["data"]:
            pa=re.compile(pattern)
            con=tt["content"]
            result=pa.findall(con)
            finall = list(set(result))
            if finall:
                photos=photos+finall
        item = Zhihuphoto1Item()
        item['imageurls']=photos
        return item