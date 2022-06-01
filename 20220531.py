import datetime
import functools
import json
import pprint
import random
import re 
import time
import sys

import requests



DEFAULT_HEADER = {
	"Accept": "application/json, text/plain, */*",
	"Accpet-Encoding": "utf-8",
	"Accept-Language": "en-US,en;q=0.9",
	"User-Agent":	"Mozilla/5.0 (X11;Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
	"X-Requested-With": "XMLHttpRequest",
}

sys_path = sys.path
wlc_path = sys_path[0]
date_format = '%Y%m%d%H%M%S%f'
wlc_path = wlc_path + '/'

bilibili_url_1 = "https://api.bilibili.com/x/space/arc/search?"
bilibili_url_2 = "https://api.bilibili.com/x/player/pagelist?bvid="


bilibili_user_id = [282170862]

bilibili_parameters = {'jsonp': 'jsonp',
            'keyword': '',
            'mid': 323737328,
            'order': 'pubdate',
            'pn': 1,
            'ps': 30,
            'tid': 0}
task = []

def wlc_get():
    url_1 = bilibili_url_1 + 'mid=' + str(bilibili_parameters['mid']) + '&ps=' + str(bilibili_parameters['ps']) + '&tid=' + str(bilibili_parameters['tid']) + '&pn=' + str(bilibili_parameters['pn']) + '&keyword=' + str(bilibili_parameters['keyword']) + '&order=' + bilibili_parameters['order'] + '&jsonp=' + bilibili_parameters['jsonp']
    #print(url)
    response = requests.get(url_1,headers=DEFAULT_HEADER)
    #print(response) 
    wlc_json = response.json()
    if str(wlc_json['code']) == '0':
        vlist = wlc_json['data']['list']['vlist']
        task.extend(vlist)
        if len(vlist) < 30:
            print("This is the last Page!")
            #print(vlist['bvid'])
        else:
            print("This is not the last Page!")
            bilibili_parameters['pn'] = bilibili_parameters.get('pn') + 1
            wlc_get()
            #print(vlist['bvid'])

def wlc_get_all_episode():
    for wlc_get_all_episode_i in range(0,len(task)):
        url_2 = bilibili_url_2 + task[wlc_get_all_episode_i]['bvid']
        response_2 = requests.get(url_2,headers=DEFAULT_HEADER)
        wlc_json_2 = response_2.json()
        if str(wlc_json_2['code']) == '0':
                data = wlc_json_2['data']
                length_data = len(data)
                task[wlc_get_all_episode_i]["episode_all"] = length_data
    #time.sleep(0.1)

        

def wlc_ifstream():
    date = datetime.datetime.now().strftime(date_format)[:-3]
    wlc_result_path = wlc_path + 'UserID_' + str(bilibili_parameters['mid']) + '_' + date + '.txt'
    for j in range(0,len(task)):
        if str(task[j]['episode_all']) == '1':
            with open(wlc_result_path,"a+") as f:
                f.write("https://www.bilibili.com/video/" + task[j]['bvid'])
                f.write("\n")
        else:
            for k in range(1,task[j]['episode_all'] + 1):
                with open(wlc_result_path,"a+") as f:
                    f.write("https://www.bilibili.com/video/" + task[j]['bvid'] + '?p=' + str(k))
                    f.write("\n")


def wlc_test():
    for i in range(0,len(bilibili_user_id)):
        print(i)
        bilibili_parameters['mid'] = bilibili_user_id[i]
        print(bilibili_parameters['mid'])
        wlc_get()
        wlc_get_all_episode()
        wlc_ifstream()
        bilibili_parameters['pn'] = 1
        task.clear()

if __name__ == '__main__':
    wlc_test()
    #print(wlc_result_path)
    #print(len(task))
    #print(task[0]['bvid'])
    #pprint.pprint(task)
