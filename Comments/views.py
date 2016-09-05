from django.shortcuts import render
from django.http.response import HttpResponse
import json
from .models import Comment
from Articles.models import Articles
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
@csrf_exempt
def create_view(request,artid):
    if request.method == "POST":
        data = json.loads(request.body)
        if len(data["comment"].strip()) > 0:
            user = User.objects.get(id=request.user.id)
            article = Articles.objects.get(id=artid)
            comment = Comment()
            comment.articles = article
            comment.article_id = article.id
            comment.user = user
            comment.comment_text = data["comment"]
            comment.save()
            return HttpResponse(json.dumps({"msg":"Comment Successful","flag":"Success"}))
        else:
            return HttpResponse(json.dumps({"msg":"Please Write Your Comment","flag":"Error"}))
    else:
        return HttpResponse(json.dumps({"msg":"Post Request Only"}))