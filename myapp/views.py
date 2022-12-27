from django.shortcuts import render ,HttpResponse
import random

topics=[{'id':1, 'title':'routing','body': 'Routing is...'},
    {'id':2, 'title':'view','body': 'View is...'},
    {'id':3, 'title':'Model','body': 'Model is...'},
    ]

def HTMLTemplate(articleTag):
    global topics
    ol=''
    # f 가 들어가면 중가로 {} 를 바로 사용 할수 있따 
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
        # ''' 따옴표 3 개는 여러개의 문자열 작성가능 '''
    return  f''' 
    <html>
    <body>
    
    <h1><a href="/">Django</a></h1>
    <ol>
    {ol}
    </ol>
    {articleTag}
    </body> 
    </html>      '''
# Create your views here.
def index(request):
    article= '''
    <h2>Welcom</h2>
    Hello Django
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request ,id):
    global topics
    for topic in topics:
        if topic['id'] ==int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))
def create(request):
    
    return HttpResponse('create')