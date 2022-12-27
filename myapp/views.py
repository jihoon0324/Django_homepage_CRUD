from django.shortcuts import render ,HttpResponse ,redirect
import random
from django.views.decorators.csrf import csrf_exempt

nextId =4
topics=[{'id':1, 'title':'routing','body': 'Routing is...'},
    {'id':2, 'title':'view','body': 'View is...'},
    {'id':3, 'title':'Model','body': 'Model is...'},
    ]

def HTMLTemplate(articleTag ,id=None):
    global topics
    contextUI=""
    if id !=None:
        contextUI = f'''
         <li>
        <form action="/delete/" method="post">
            <input type="hidden" name="id"  value={id}>
            <input type="submit" value="delete">
        </form>
    </li>
        
        '''
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
    <ul>
    <li><a href="/create/"> Create</a></li>
    {contextUI}
    </ul>
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
    article=''
    for topic in topics:
        if topic['id'] ==int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article ,id))
@csrf_exempt
def create(request):
    global nextId
    if request.method == "GET":
        article ='''
        <form action="/create/" method="post">
        <p><input type="text" name ="title" placeholder="title"> </p>
        <p><textarea name="body" placeholder="body"></textarea></p>
        <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method =='POST' :
        title = request.POST['title']
        body= request.POST['body']
        newTopic ={"id":nextId ,"title":title , "body":body}
        topics.append(newTopic)
        url='/read/'+str(nextId)
        nextId +=1
        return redirect(url)

@csrf_exempt
def delete(request):
    global topics
    if request.method =="POST" :
        id = request.POST['id']
        newTopics=[]
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')