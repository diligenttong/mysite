from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, RegisterForm, SetPasswordForm
from django.contrib.auth.models import User
import random
import hashlib
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.conf import settings
from account.models import UserInFo


# Create your views here.


def hash_code(s, salt='mysite'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def user_login(request):
    request.session['is_login'] = None
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = User.objects.filter(username=username).first()
            if user:
                login(request, user)
                if user.password == hash_code(password):
                    request.session['username'] = username
                    request.session['is_login'] = True
                    return redirect('/blog/blog_homepage/')

                else:
                    message = '密码错误！'
            else:
                message = '用户不存在'

        return render(request, 'account/login.html', locals())
    if request.method == 'GET':
        login_form = UserForm()
        return render(request, 'account/login.html', locals())


# Get 取到URL中携带的参数，POST 取到表单提交的数据


def user_logout(request):
    request.session.clear()
    return render(request, "account/logout.html")


def user_register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
            else:
                same_name_user = User.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
            # 当一切都OK的情况下，创建新用户
            new_user = User.objects.create_user(username)
            new_user.username = username
            new_user.password = hash_code(password1)
            new_user.email = email
            new_user.save()
            user_info = UserInFo.objects.create(id=new_user.id, username=new_user.username, email=new_user.email)
            user_info.save()
            return redirect('/account/login/')  # 自动跳转到登录页面
    if request.method == 'GET':
        register_form = RegisterForm()
        return render(request, 'account/register.html', locals())


def get_random_str():
    code = ''
    for i in range(6):
        num = random.randint(0, 9)
        alf = chr(random.randint(65, 90))
        add = random.choice([num, alf])
        code = ''.join([str(add), code])

    return code


def password_reset(request):
    ret = {'status': 0, 'msg': ''}
    if request.method == 'POST':
        email = request.POST.get('email')
        if email is '':
            ret['msg'] = '邮箱不能为空'
            return JsonResponse(ret)
        user = User.objects.filter(email=email).first()
        if user:
            # 发送邮件
            from django.core.mail import send_mail
            from django.conf import settings
            # 多线程发送邮件
            import threading
            global code
            code = get_random_str()
            print(code)
            t = threading.Thread(target=send_mail, args=(' %s reset password' % user.username,
                                                         '验证码: %s ' % code,
                                                         settings.EMAIL_HOST_USER,
                                                         [email]))
            t.start()
            ret['status'] = 1
            return JsonResponse(ret)

        else:
            ret['msg'] = 'the email no register'
            return JsonResponse(ret)

    return render(request, 'account/password_reset.html')


def password_reset_test(request):
    if request.method == 'POST':
        ret = {'status': 0, 'msg': ''}
        email = request.POST.get('email')
        checking_code = request.POST.get('checkingCode')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if checking_code == code and password == password2:
            User.objects.filter(email=email).update(password=hash_code(password))
            ret['msg'] = '重置密码成功'
            return JsonResponse(ret)

        else:
            ret['status'] = 1
            ret['msg'] = '你输入的验证码或密码有误'
            return JsonResponse(ret)

    return render(request, 'account/password_reset.html')


def setpassword(request):
    err_msg = ''
    username = request.session.get('username')
    user = User.objects.get(username=username)
    # user = authenticate(request, username=username)
    if request.method == 'POST':
        set_password_form = SetPasswordForm(request.POST)
        if set_password_form.is_valid():  # 获取数据
            old_password = hash_code(set_password_form.cleaned_data['old_password'])
            print(old_password)
            new_password = set_password_form.cleaned_data['new_password1']
            print(new_password)
            repeat_password = set_password_form.cleaned_data['new_password2']
            # 检查旧密码是否正确
            if user.check_password(old_password):
                if not new_password:
                    err_msg = '新密码不能为空'
                elif new_password != repeat_password:
                    err_msg = '两次密码不一致'
                else:
                    user.set_password(hash_code(new_password))
                    user.save()
                    return redirect("/account/login/")
            else:
                err_msg = '原密码输入错误'
                return render(request, 'account/set_password.html', locals())
    if request.method == 'GET':
        set_password_form = SetPasswordForm()
        return render(request, 'account/set_password.html', locals())


def my_image(request):
    if request.is_ajax():
        img = request.FILES.get('f1')
        user = User.objects.get(username=request.user.username)
        userinfo = UserInFo.objects.get(username=user)
        userinfo.photo = 'account/' + img.name
        userinfo.save()
        fname = settings.MEDIA_ROOT + "account/" + img.name
        with open(fname, 'wb') as f:
            for c in img.chunks():
                f.write(c)
        return HttpResponse('1')
    else:
        return render(request, 'account/upload_file.html')


def edit_info(request):
    # if request.method == "POST":
    #     userinfo_form = UserInFoForm(request.POST)
    #     print(userinfo_form)
    #     if userinfo_form.is_valid():
    #         age = userinfo_form.cleaned_data['age']
    #         profession = userinfo_form.cleaned_data['profession']
    #         hobby = userinfo_form.cleaned_data['hobby']
    #         phone = userinfo_form.cleaned_data['phone']
    #         weichat = userinfo_form.cleaned_data['weiChat']
    #         skills = userinfo_form.cleaned_data['skills']
    #         user = User.objects.get(username=request.user.username)
    #         userinfo = UserInFo.objects.get(username=user)
    #         userinfo.age = age
    #         userinfo.profession = profession
    #         userinfo.hobby = hobby
    #         userinfo.phone = phone
    #         userinfo.weiChat = weichat
    #         userinfo.skills = skills
    #         userinfo.save()
    #     return redirect('/blog/about/')
    #
    # else:
    #     user = User.objects.get(username=request.user.username)
    #     userinfo = UserInFo.objects.get(username=user)
    #     userinfo_form = UserInFoForm()
    #     return render(request, 'account/edit_info.html', locals())
    edit_obj = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        new_age = request.POST.get('age')
        new_profession = request.POST.get('profession')
        print(new_profession)
        new_hobby = request.POST.get('hobby')
        new_phone = request.POST.get('phone')
        new_wei = request.POST.get('weiChat')
        new_skills = request.POST.get('skills')
        ret1 = UserInFo.objects.filter(username=edit_obj)
        ret1.update(age=new_age, profession=new_profession, hobby=new_hobby, phone=new_phone, weiChat=new_wei,
                    skills=new_skills)
        return redirect('/blog/about/')
    ret = UserInFo.objects.filter(username=edit_obj).first()
    return render(request, 'account/edit_info.html', locals())
