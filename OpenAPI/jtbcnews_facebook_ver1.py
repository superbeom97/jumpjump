import os
import json

def Jtbc_News(data):
    link_num_ls = []
    for compa in data:
        set_ls = []
        set_ls.append(compa.get('shares').get('count'))
        set_ls.append(compa.get('name'))
        set_ls.append(compa.get('link'))
        link_num_ls.append(set_ls)

    Comparison_Link(link_num_ls)

def Comparison_Link(link_num_ls):
    link_ls = []
    for compa in link_num_ls:
        link_ls.append(compa[0])
    link_ls.sort()
    link_ls.reverse()

    Sort_Fuction(link_num_ls, link_ls)

def Sort_Fuction(link_num_ls, link_ls):
    sort_news = []
    for search_news in link_ls:
        for news in link_num_ls:
            if search_news == news[0]:
                sort_news.append(news)

    Only_One(sort_news)

def Only_One(sort_news):
    index_count = -1
    for compa in sort_news:
        index_count += 1
        if index_count == len(sort_news) - 1:
            break
        for next_compa in sort_news[(index_count):]:
            if compa[1] == next_compa[1]:
                del sort_news[(index_count+1)]

    for prn in sort_news:
        print("공유 수 : %s" % prn[0])
        print("기사 제목 : %s" % prn[1])
        print("링크 : %s\n" % prn[2])


## Entry Point!!
data = []
with open("jtbcnews_facebook_2018-01-24_2018-01-25.json", encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    data = json.loads(json_string)
    data = data.get('data')
    Jtbc_News(data)