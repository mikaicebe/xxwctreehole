from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Message, Comment
import json


# Create your views here.

class MesObj:
    id = 1
    content = ""
    time = ""
    comments = []

    def __init__(self, content, time, comments, id):
        self.content = content
        self.time = time
        self.comments = comments
        self.id = id


class CmtObj:
    id = 1
    content = ""
    time = ""

    def __init__(self, content, time, id):
        self.content = content
        self.time = time
        self.id = id


def index(request):
    return HttpResponse("Hello Kitty")


@csrf_exempt
def createMessage(request):
    try:
        print(request.body[0])
        message = json.loads(request.body.decode())['content']
        Message(message_text=message, time=timezone.now()).save()
        return HttpResponse('{status: 0}')
    except:
        return HttpResponse('{status: 1}')


@csrf_exempt
def createComment(request, message_id):
    try:
        message = Message.objects.get(pk=message_id)
        Comment(message=message, comment_text=json.loads(request.body.decode())['content'], time=timezone.now()).save()
        return HttpResponse('{status: 0}')
    except:
        return HttpResponse('{status: 1}')


@csrf_exempt
def getAllMessages(request):
    res = []
    messages = Message.objects.all()
    for message in messages:
        comments = []
        for comment in message.comment_set.all():
            comments.append(CmtObj(content=comment.comment_text, time=comment.time.ctime(), id=comment.id).__dict__)
        res.append(MesObj(content=message.message_text, time=message.time.ctime(), comments=comments, id=message.id).__dict__)
    return HttpResponse(json.dumps(res))
