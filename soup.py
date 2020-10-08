from bs4 import BeautifulSoup
import requests
import json
from name import *


haveNew = False


def getAllBlogPic(member,listNewestDate):

    count = 0

    allPic = []

    for i in keyakizaka:
        if(member == i['name']):
            memberLink = 'https://www.keyakizaka46.com/s/k46o/diary/member/' + \
                i['blog']

    # main page of one member's blog
    init_response = requests.get((memberLink))

    # 以 Beautiful Soup 解析 HTML 程式碼
    soup = BeautifulSoup(init_response.text, 'html.parser')

    # find the newest blog
    newestLinkWrap = soup.find('li', class_='singlePage')
    newestLink = 'https://www.keyakizaka46.com' + \
        newestLinkWrap.select_one('a').get('href')

    while (True):

        # member's newest blog
        next_response = requests.get((newestLink))

        # 以 Beautiful Soup 解析 HTML 程式碼
        soup = BeautifulSoup(next_response.text, 'html.parser')

        blogWrap = soup.find('div', class_='box-main')

        # get img list
        img_tags = blogWrap.find_all('img',{"src":True})

        
        ##### get info for list #####
        # get date
        datediv = blogWrap.find('div', class_='box-bottom')
        dateli = datediv.find('li')
        print(dateli.get_text().strip())
        date = dateli.get_text().strip()

        if date==listNewestDate: 
            return allPic

        # get title
        titlediv = blogWrap.find('div', class_='box-ttl')
        titleli = titlediv.find('h3')
        print(titleli.get_text().strip())
        print(newestLink)
        title = titleli.get_text().strip()

        oneBlog = {'date': date, 'title': title, 'link': newestLink, 'img': []}

        for tag in img_tags:

            print(tag['src'])
            oneBlog['img'].append(tag['src'])

        allPic.append(oneBlog)
        ##### end of appending dict to list #####

        if (date=='2018/06/07 02:37' and title=='スキマスイッチさん。'): #a page error in saitou shiori's blog found
            print('Error blog skipped')
            newestLink = 'https://www.keyakizaka46.com/s/k46o/diary/detail/15602?ima=0000&cd=member'
            continue

        print("-----------------")

        if soup.find('div', class_='btn-navi btn-prev') == None:
            print("Finish")
            break
        else:
            prev_blog = soup.find('div', class_='btn-navi btn-prev')
            newestLink = 'https://www.keyakizaka46.com' + \
                prev_blog.select_one('a').get('href')

    return allPic

def writeMemberJSON(member):

    fileName = "./memberdata/" + member + ".json"

    with open(fileName, "w", encoding='utf-8') as file:
        json.dump(getAllBlogPic(member,0), file)

    file.close()

def writeAllMemberJSON():

    for i in keyakizaka:
        if i['gen']==2.5:
            writeMemberJSON(i['name'])

def updateMemberJSON(member):
    fileName = "./memberdata/" + member + ".json"

    with open(fileName, "r+", encoding='utf-8') as file:   
        data = json.loads(file.read())  

    print(data[0])
    tempList = getAllBlogPic(member,data[0]['date'])
        
    tempList.extend(data)

    with open(fileName, "w", encoding='utf-8') as file:
        json.dump(tempList, file)

def updateAllMemberJSON():

    for i in keyakizaka:
        updateMemberJSON(i['name'])

def createMemberJSON():

    for i in keyakizaka:
        fileName = "./memberdata/" + i['name'] + ".json"

        with open(fileName, "w", encoding='utf-8') as file:
            json.dump("", file)



updateAllMemberJSON()