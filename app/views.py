from django.shortcuts import render, redirect
from  app.models import Users,Travel
from  django.http import HttpResponse

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            Users.objects.get(username=username,password=password)
            request.session['username'] = username
            print(request.session.keys())
            return redirect('/app/home')
        except:
            return


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        try:
            Users.objects.get(username=username)
        except:
            if not username or not password or not confirm_password: return
            if password != confirm_password: return
            Users.objects.create(username=username, password=password)
            return redirect('/app/login')
        return
def logOut(request):
    request.session.clear()
    return redirect('/app/login')
def home(request):
    username = request.session.get('username')
    userInfo= Users.objects.get(username=username)

    return render(request,'home.html'
                  ,{'userInfo':userInfo,

                    }
                  )

def changeSelfInfo(request):
    username = request.session.get('username')
    userInfo= Users.objects.get(username=username)
    return render(request,'changeSelfInfo.html',{'userInfo':userInfo,})
