import requests
import json
import re

headers = {
    'User-Agent': 'BiLiBiLi/1.0.0 (1244382469@qq.com)'
}

#  视频
filter_list = ['新型肺炎', '新型冠状病毒', '传染']
url = 'https://api.bilibili.com/x/web-interface/view?aid='

for av in range(84726389, 84738342):
    txt = requests.get(url + str(av), headers=headers).text
    txt = json.loads(txt)
    if txt['message'] == '0':
        flag = False
        for i in filter_list:
            if i in txt['data']['dynamic']:
                flag = True

        for i in filter_list:
            if i in txt['data']['title']:
                flag = True

        print(av)
        if flag:
            av = txt['data']['aid']  # av号
            partition = txt['data']['tname']  # 分区
            up_name = txt['data']['owner']['name']  # up名
            title = txt['data']['title']  # 标题
            description = txt['data']['dynamic']
            #  up_pic = txt['data']['owner']['face']  # up头像
            #  pic = txt['data']['pic']  # 封面

            with open('data1.doc', 'a+') as f:
                f.write("{} \n".format(title))
                f.write(description + '\n')
                f.write('up:{}     分区：{}\n'.format(up_name, partition))
                f.write('链接：www.bilibili.com/video/av{} \n \n'.format(av))

