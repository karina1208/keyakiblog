import json, time
from datetime import *

keyakizaka = [
    {'name': '上村莉菜', 'gen': 1, 'blog': 'list?ima=0000&ct=03'},
    {'name': '尾関梨香', 'gen': 1, 'blog': 'list?ima=0000&ct=04'},
    {'name': '小池美波', 'gen': 1, 'blog': 'list?ima=0000&ct=06'},
    {'name': '小林由依', 'gen': 1, 'blog': 'list?ima=0000&ct=07'},
    {'name': '齋藤冬優花', 'gen': 1, 'blog': 'list?ima=0000&ct=08'},
    {'name': '佐藤詩織', 'gen': 1, 'blog': 'list?ima=0000&ct=09'},
    {'name': '菅井友香', 'gen': 1, 'blog': 'list?ima=0000&ct=11'},
    {'name': '土生瑞穂', 'gen': 1, 'blog': 'list?ima=0000&ct=14'},
    {'name': '原田葵', 'gen': 1, 'blog': 'list?ima=0000&ct=15'},
    {'name': '守屋茜', 'gen': 1, 'blog': 'list?ima=0000&ct=18'},
    {'name': '渡辺梨加', 'gen': 1, 'blog': 'list?ima=0000&ct=20'},
    {'name': '渡邉理佐', 'gen': 1, 'blog': 'list?ima=0000&ct=21'},
    {'name': '井上梨名', 'gen': 2, 'blog': 'list?ima=0000&ct=43'},
    {'name': '関有美子', 'gen': 2, 'blog': 'list?ima=0000&ct=44'},
    {'name': '武元唯衣', 'gen': 2, 'blog': 'list?ima=0000&ct=45'},
    {'name': '田村保乃', 'gen': 2, 'blog': 'list?ima=0000&ct=46'},
    {'name': '藤吉夏鈴', 'gen': 2, 'blog': 'list?ima=0000&ct=47'},
    {'name': '松田里奈', 'gen': 2, 'blog': 'list?ima=0000&ct=48'},
    {'name': '松平璃子', 'gen': 2, 'blog': 'list?ima=0000&ct=49'},
    {'name': '森田ひかる', 'gen': 2, 'blog': 'list?ima=0000&ct=50'},
    {'name': '山﨑天', 'gen': 2, 'blog': 'list?ima=0000&ct=51'},
    {'name': '遠藤光莉', 'gen': 2.5, 'blog': 'list?ima=0000&ct=53'},
    {'name': '大園玲', 'gen': 2.5, 'blog': 'list?ima=0000&ct=54'},
    {'name': '大沼晶保', 'gen': 2.5, 'blog': 'list?ima=0000&ct=55'},
    {'name': '幸阪茉里乃', 'gen': 2.5, 'blog': 'list?ima=0000&ct=56'},
    {'name': '増本綺良', 'gen': 2.5, 'blog': 'list?ima=0000&ct=57'},
    {'name': '守屋麗奈', 'gen': 2.5, 'blog': 'list?ima=0000&ct=58'},

]

def getAllName():
    nameList = []
    for i in keyakizaka:
        nameList.append(i['name'])

    return nameList


def openJSON(member):
    fileName = "./memberdata/" + member + ".json"

    with open(fileName, "r", encoding='utf-8') as file:   
        return json.loads(file.read())  

def countBlog(member):

    data = openJSON(member)

    return len(data)

def countAllBlog():
    blogCount = []

    for i in keyakizaka:
        blogCount.append({'name':i['name'],'gen':i['gen'],'count':countBlog(i['name'])})

    return blogCount

def totalNumberOfImg():
    totalNumberOfImg = []

    for i in keyakizaka:

        data = openJSON(i['name'])
        
        count = 0

        print (len(data))
        for blog in range(len(data)):
            for img in data[blog]['img']:
                count += 1

        totalNumberOfImg.append({'name':i['name'],'gen':i['gen'],'count':count})

    return totalNumberOfImg

def countBlogTime(member):

    dateDict = {}

    for i in range(24):
        num = str(i).zfill(2)
        dateDict[num] = 0


    data = openJSON(member) 

    for blog in range(len(data)):
        oriDate = data[blog]['date']
        date = oriDate[11]+oriDate[12]
        dateDict[date] += 1

    
    return json.dumps(dateDict)

def blogWithPic(member):
    withPic = {}
    withPic['yes'] = 0
    withPic['no'] = 0
    data = openJSON(member)
    for blog in range(len(data)):
        if (len(data[blog]['img'])!=0):
            withPic['yes'] += 1
        else:
            withPic['no'] += 1

    return json.dumps(withPic)

def blogPerYear(member):
    perYear = {}
    

    for i in range(2015,2021): #2015-2020
         perYear[i] = 0
         print(i)

    data = openJSON(member)
    for blog in range(len(data)):
        
        oriDate = data[blog]['date']
        date = (int)(oriDate[0:4])
        perYear[date] += 1

    return json.dumps(perYear)

# print(countAllBlog())