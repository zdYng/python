from django.shortcuts import render

# Create your views here.
def home(request):
    string = u"我真的不会写前端啊！！！"
    return render(request,'learn/home.html',{'string':string})

def home_2(request):
    TutorialList = ["HTML","CSS","JQuery","Python","Django"]
    return render(request,'learn/home_2.html',{'TutorialList':TutorialList})
