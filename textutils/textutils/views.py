# i created
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse('''<h1>hello users</h1>  1) <a href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-20/">start learn django</a>''') 

    
def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    
    #check checkbox
    djcheck=request.POST.get('removepunc','off')
    caps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremove=request.POST.get('extraspaceremove','off')
    charcount=request.POST.get('charcount','off')
    
    #analyzed=djtext
    #check which check box is on
    if djcheck == "on":
            punctuation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
            analyzed=""
            for char in djtext:
                if char not in punctuation:
                    analyzed=analyzed+char
            params={"purpose":"remove punctuation", "analyzed_text":analyzed}
            djtext=analyzed
            #return render(request, 'analyze.html' ,params)
    
    if caps == "on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params={"purpose":"make uppercase", "analyzed_text":analyzed}
        #return render(request, 'analyze.html' ,params)
        djtext=analyzed
    
    if newlineremove == "on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed + char
        params={"purpose":"remove new line", "analyzed_text":analyzed}
        #return render(request, 'analyze.html' ,params)
        djtext=analyzed
    
    if extraspaceremove == "on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
               
                analyzed=analyzed + char
                params={"purpose":"remove extra space", "analyzed_text":analyzed}
        #return render(request, 'analyze.html' ,params)
        djtext=analyzed    
        
    if charcount == "on":
        analyzed=""
        count=len(djtext)
        analyzed=count
        params={"purpose":"character count", "analyzed_text":analyzed}
        
    if(djcheck!="on" and caps!="on" and newlineremove!="on" and extraspaceremove!="on" and charcount!="on"):
        
        return HttpResponse("checkbox is not checked")
          
    return render(request, 'analyze.html' ,params)      
             
        
            

def capfirst(request):
    return HttpResponse("capitalize") 

def newlineremove(request):
    return HttpResponse("new line remove") 

def spaceremove(request):
    return HttpResponse("space remove") 

def charcount(request):
    return HttpResponse("character count") 
