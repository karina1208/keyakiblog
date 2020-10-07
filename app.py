from flask import Flask, render_template, url_for, request, redirect, jsonify
from datetime import datetime
import json, math
from name import *


# picList = getAllBlogPic()

app = Flask(__name__)

def get_count(member):
    app.logger.info(member.get('count'))
    return member.get('count')


#initial page
@app.route('/', methods=['POST','GET'])
def index():
    he = "hello world"

    nameList = getAllName()

    allBlogCount = countAllBlog()
    allBlogCount.sort(key=get_count,reverse=True)
    jBlogCount = json.dumps(allBlogCount)

    totalImgNo = totalNumberOfImg()
    totalImgNo.sort(key=get_count,reverse=True)
    jImgNo = json.dumps(totalImgNo)

    return render_template('index.html',nameList=nameList,allBlogCount=jBlogCount,totalImgNo=jImgNo)

def getMemberImg(member):
    fileName = "./memberdata/" + member + ".json"
    app.logger.info(fileName)

    with open(fileName, "r+", encoding='utf-8') as file:   
        data = json.loads(file.read())  

    return [d for d in data if len(d['img']) !=0]

def get_date(blog):
    app.logger.info(blog.get('date'))
    return blog.get('date')


@app.route('/memberBlog', methods=['GET'])
def findMemberBlog():

    nameList = getAllName()

    member = request.args.get('member', 0, type=None)
    sort = request.args.get('sort', 0, type=None)
    app.logger.info(sort)
    if sort=='a':
        blogData = getMemberImg(member)
    elif sort=='d':
        blogData = getMemberImg(member)
        blogData.sort(key=get_date)
    page = request.args.get('page', 0, type=int)
    perPage = 30
    totalPage = math.ceil(len(blogData)/perPage)
    app.logger.info(str(1*page)+" "+str(perPage*page))

    return render_template('memberBlog.html', blogData=blogData[perPage*page-30:perPage*page],nameList=nameList,member=member,page=page,totalPage=totalPage,sort=sort)

@app.route('/memberStat', methods=['GET'])
def findMemberStat():

    nameList = getAllName()

    member = request.args.get('member', 0, type=None)

    blogTime = countBlogTime(member)
    blogPic = blogWithPic(member)
    blogYear = blogPerYear(member)

    return render_template('memberStat.html',nameList=nameList,member=member,blogTime=blogTime,blogPic=blogPic,blogYear=blogYear)


if __name__ == "__main__":
    app.run(debug=True)