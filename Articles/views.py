from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Articles
from django.contrib.auth.models import User
from Comments.models import Comment
import json
import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

def error(request):
    return render(request,"404.html")

@login_required(login_url="/login/")
def home_view(request):
    a = Articles.objects.all()
    art_list = []
    for i in a:
        if i.is_active == True:
            comments = Comment.objects.filter(articles_id = i.id)
            comments = comments.count()
            dic_temp = {}
            dic_temp['title'] = i.title
            dic_temp['artid'] = i.id 
            dic_temp['content'] = i.content[:100]+"..."
            dic_temp['time'] = i.timestamp.date()
            dic_temp['writer'] = i.user.first_name+" "+i.user.last_name
            dic_temp["comments"] = comments
            art_list.append(dic_temp)
        else:
            pass
    return render(request,'home.html',{"artlist":art_list})

@login_required(login_url="/login/")
@csrf_exempt
def create_view(request):
    if request.method == "POST":
        print request.body
        data = json.loads(request.body)
        user = request.user.id
        title = data["title"]
        content = data["content"]
        if len(title.strip()) > 0 and len(content.strip()) > 0:
            u = User.objects.filter(id=user)
            print u
            art = Articles()
            art.user = u[0]
            art.title = data["title"].strip()
            art.content = data["content"].strip()
            art.publish = datetime.datetime.now()
            print art
            art.save()
            return HttpResponse(json.dumps({"flag":"Success","msg":"Created Successfully"}))
        else:
            return HttpResponse(json.dumps({"flag":"Success","msg":"Please Add Title and Content."}))
    else:
        return render(request, "create_article.html")

@login_required(login_url="/login/")
@csrf_exempt
def detail_view(request,art_number):
    print request.method
    if request.method=="GET":
        print art_number
        try:
            article = Articles.objects.get(id=art_number)
            comment = Comment.objects.filter(articles_id=article.id)
            if article.is_active == True:
                data = {}
                artid = article.id
                if request.user.id == article.user.id:
                    owner = True
                else:
                    owner = False
                data['title'] = article.title
                data["content"] = article.content
                data["modified"] = article.timestamp.date()
                data["written"] = article.user.first_name+" "+ article.user.last_name
                print data
                comments = []
                for i in comment:
                    print i
                print comment
                return render(request,"details.html",{"data":data, "artid":artid, "owner":owner, "comment":comment})
            else:
                return render(request,"404.html")
        except Exception as e:
            print "Not Found "+str(e)
            return render(request,"404.html")

@login_required(login_url="/login/")
@csrf_exempt
def update_view(request, art_number):
    print request.method
    if request.method=="GET":
        try:
            article = Articles.objects.get(id=art_number)
            if article.is_active == True:
                heading = article.title
                content = article.content
                print"this is content"
                print content
            else:
                return render(request,"404.html")
            return render(request, "editArticle.html",{"heading":heading,"content":content,"artid":art_number})
        except Exception as e:
            return render(request, "404.html")
    else:
        data = json.loads(request.body)
        article = Articles.objects.get(id=data['id'])
        article.title = data["title"]
        article.content = data["content"]
        article.save()
        return HttpResponse(json.dumps({"flag":"Success","msg":"Edited Successfully"}))
@login_required(login_url = "/login/")
def delete_view(request, art_number):
    if request.method == "GET":
        try:
            article = Articles.objects.get(id=art_number)
            if request.user.id == article.user.id:
                article.is_active = False
                article.save()
            else:
                return render(request, "404.html")
        except Exception as e:
            return render(request, "404.html")
    return redirect("/")