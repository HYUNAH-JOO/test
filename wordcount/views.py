from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def result(request):
    chitext=request.GET['mytext']
    sp_sen=chitext.split(' ')
    # chitext에 저장이 된 문자가 띄어쓰기를 기준으로 분리되어 list에 저장된다
    mydict={}
    for i in sp_sen:
        if i in mydict:
            mydict[i]+=1
        else:
            mydict[i]=1
    context={'textchi':chitext,'mydict':mydict, 'myitem':mydict.items}
    return render(request,'result.html',context)
