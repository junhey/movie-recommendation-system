from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def index(request):
    return HttpResponse('这是首页')



# 登录页面
def rlogin(request):
    # 判断是否已经登录
    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER','/'))
    else:
        if request.method == 'GET':
            request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
            return render(request,'login.html',locals())
        elif request.method == 'POST':
            username = request.POST.get("username",'')
            password = request.POST.get("password",'')
            if username != '' and password != '':
                user = authenticate(username=username, password=password)
                print(user)
                if user is not None:
                    login(request,user)
                    print("登录成功！")
                    return redirect(request.session['login_from'])
                else:
                    print(username,password,user)
                    errormsg = '用户名或密码错误！'
                    return render(request,'login.html',locals())
            else:
                return JsonResponse({"e":"chucuo"})
    # return HttpResponse("这是登录页")

# 注册页面
def register(request):
    if request.method == 'GET':
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
        return render(request,'register.html',locals())
    elif request.method == 'POST':
        # 接收表单数据
        username = request.POST.get("email", '')
        password = request.POST.get("password", '')
        email = request.POST.get("email", '')
        # 判断数据是否正确
        if username != '' and password != '' :
            # 判断用户是否存在
            if User.objects.filter(username=username).exists() == False:
                # 注册
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                # 登录
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request,user)
                # 重定向跳转
                return redirect(request.session["login_from"],'/')
                
            else:
                errormsg = '用户名已存在！'
                return render(request,'register.html',locals())
        else:
            return JsonResponse({"success": False, "msg": "信息填写错误:{0},{1},{2},{3}".format(username,password,checkcode)})
    # return HttpResponse("这是注册页")

# 注销
def rlogout(request):
    try:
        logout(request)
    except Exception as e:
        print(e)
    return redirect(request.META['HTTP_REFERER'])

