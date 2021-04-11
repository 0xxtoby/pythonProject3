import json
import pprint
import re

import scrapy

from bcy.items import BcyItem
from scrapy import cmdline

from bcy.items import BcyItem


class PcycosSpider(scrapy.Spider):
    name = 'pcycos'
    # allowed_domains = ['bcy.cn']

    start_urls = ['https://bcy.net/apiv3/common/getFeeds?refer=channel&direction=loadmore&cid=6618800694038102275&_signature=lUArjQAAAACojcXarY3iqpVAK5AAPU-']

    def parse(self, response):
        print(response.status)
        # print(response.body)

        json_pcy=json.loads(response.text)
        # print(json_pcy['data']['item_info'])
        i=0
        for li in json_pcy['data']['item_info']:

            # print(li)
            i=i+1
            li_url=li['item_detail']['item_id']
            print(li_url)



            yield  scrapy.Request(url='http://bcy.net/item/detail/'+li_url, callback=self.jpgre)
            # yield  scrapy.Request(url='http://www.baidu.com', callback=self.jpgre)
            # if i==1:
            #     break
            # else:
            #     print(i)
        for 变量 in range(10):
            yield scrapy.Request(url='https://bcy.net/apiv3/common/getFeeds?refer=channel&direction=loadmore&cid=6618800694038102275&_signature=lUArjQAAAACojcXarY3iqpVAK5AAPU-')
        # print(json_pcy)
    def jpgre(self, response):
        item=BcyItem()


        # print(response.text)
        # jpg_id_list=response.xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/div[1]/article/div[1]/div[2]/div/div/div/img').extract()
        # print(response.text)


        #保存网页源码
        f = open('jpglist.html', 'wb')
        f.write(response.body)

        #获得js代码
        jpg_htlm=response.text
        # print(jpg_htlm)

        url_list=re.search('window.__ssr_data = JSON.parse((.*))',jpg_htlm)
        # print(url_list)
        # print(url_list[0])

        #"path":"~tplv-banciyuan-w650.image",
        # "path": "https:\u002F\u002Fp3-bcy.byteimg.com\u002Fimg\u002Fbanciyuan\u002Fa2ef55375e554a72a066b21f954d86fc~tplv-banciyuan-w650.image"
        # \"path\":\"https:\\u002F\\u002Fp3-bcy.byteimg.com\\u002Fimg\\u002Fbanciyuan\\u002Fa2ef55375e554a72a066b21f954d86fc~tplv-banciyuan-w650.image\"
# https://p3-bcy.byteimg.com/img/banciyuan/(.*?))~tplv-banciyuan-logo-v3:.*?.image?
        #{\"path\":\"https:\\u002F\\u002Fp3-bcy.byteimg.com\\u002Fimg\\u002Fbanciyuan\\u002F7b60a9073d4a45e6a7e9ce9c63a96d7f~tplv-banciyuan-w650.image\",
        # \"origin\":\"https:\\u002F\\u002Fp3-bcy.byteimg.com\\u002Fimg\\u002Fbanciyuan\\u002F7b60a9073d4a45e6a7e9ce9c63a96d7f~tplv-banciyuan-logo-v3:wqljb3NlcumbquiQvemYoemZjArljYrmrKHlhYMgLSBBQ0fniLHlpb3ogIXnpL7ljLo=.image?sig=_QZGUjDbBlFCbURnL1-r-Gr2Gsg%3D\"




        #处理js代码
        nuwurl=''
        for index in str(url_list[0]):
            if index!='\\':
                nuwurl=nuwurl+index
        # print(nuwurl)
        zurl = re.sub('(u002F)', '/', nuwurl)


        #选择jpg原图url
        # urrl=re.findall('.*?path.*?:.*?https:(.*?)~tplv-banciyuan-w650.image',str(url_list[0]))
        urrl=re.findall('"origin":"(.*?)"',zurl)
        pprint.pprint(urrl)



        item['urlid'] = urrl


        # for url in urrl:
        #     print(url)
        #     url_data=re.split('u002F',url)
        #     url_id=url_data[-1]
        #     url_top=re.split('\\\\',url_data[2])[0]
        #     print(url_id)
        #     print(url_top)
            # https://p9-bcy.byteimg.com/img/banciyuan/698ca67978c24818962eb50f36caea80~tplv-banciyuan-w650.image
            # print('https://'+url_top+'/img/banciyuan/'+url_id+'~tplv-banciyuan-w650.image')

        # url_list=response.xpath('/html/body/div/div/div[1]/div/div[1]/div/div[1]/article/div[1]/div[2]/div[2]/div')


        #=========获取标题===================


        print(response.url)
        print("================================")
        print(response.status)

        biaoti=response.xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/div[1]/article/div[1]/div[1]/text()')[0].extract()
        print(biaoti)

        bcy_neme=response.xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[1]/div[1]/div/div[1]/div/div[2]/a/text()')[0].extract()

        print(bcy_neme)


        jpg_num=response.xpath('/html/body/div/div/div[1]/div/div[1]/div/div[1]/article/header/div[1]/span[2]/text()')[0].extract()
        print(jpg_num)

        # dz_num=response.xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/text()')[0].extract()
        # print(dz_num)

        item['biaoti']=biaoti
        item['bcy_name']=bcy_neme
        item['jpg_num']=jpg_num
        # item['dz_num']=dz_num

        yield item


#=======================
        # alldata_item = []
        # pattern = re.compile(' {"item_detail":(.*?)} ' , re.S)
        # items = re.search(pattern, response.body)
        # result = items.group().replace(', //', '')
        # pageJson = json.loads(result)  # 将str解析成dic，解析json格式,解出来是一个字典
        #
        # print(pageJson)


        # f=open('bcy.json','wb')
        # f.write(response.body)





if __name__ == '__main__':
    cmdline.execute("scrapy crawl pcycos  ".split())

