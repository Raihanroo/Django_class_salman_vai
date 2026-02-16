from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from sample.models import User, Student


def sample_view(request):
    return HttpResponse("Salman bin sultan")


def demo_template(request):
    name = "raihan"
    password = "123"
    data = {"uname": name, "pw": password}

    return render(request, "demo.html", data)


import random  # eta ekta libriry

import secrets
from django.core.mail import send_mail
from django.conf import settings


def send_otp_email(user_email, otp):
    send_mail(
        subject="Your OTP Code",
        message=f"Your OTP is {otp}. It will expire in 5 minutes.",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email],
        fail_silently=False,
    )
    return HttpResponse("send")


def generate_otp():
    # return ''.join([str(secrets.randbelow(10)) for _ in range(6)])
    return random.randint(100000, 999999)


def demo_insert(req):
    name = req.POST.get("uname")
    conpw = req.POST.get("conpw")
    pw = req.POST.get("pw")
    email = req.POST.get("email")

    # otp = generate_otp()  # ei function ta call korbo
    # return HttpResponse(otp)

    # return HttpResponse(name)
    if len(name) == 0 or len(pw) == 0 or len(conpw) == 0 or len(email) == 0:
        return HttpResponse("This is empty")
    else:
        if pw != conpw:
            return HttpResponse("password does not match")
        elif len(name) > 21:
            return HttpResponse("the name size must be below 21")

        else:
            otp = generate_otp()
            v_status = 0
            send_otp_email(email, otp)
            create_user = User(u_name=name, password=pw, email=email, v_status=v_status,otp=otp)
            create_user.save()
            return redirect("/user_list/")


def user_list(req):
    data = User.objects.all().order_by("-id")  # eta desending korar torika
    d = {
        "users": data
    }  # user er madhome somostto data gulu dictionary niye ase d contex a assign kore diche
    return render(req, "show_user.html", d)


###################edit function33############# after edit/How to make update function############


def editUser(req, uid):
    single_user = get_object_or_404(User, id=uid)
    s_user = {"data": single_user}
    return render(req, "edit_user.html", s_user)


def update_user(req):
    name = req.POST.get("uname")
    conpw = req.POST.get("conpw")
    pw = req.POST.get("pw")
    uid = req.POST.get("id")

    if len(name) == 0 or len(pw) == 0 or len(conpw) == 0:
        return HttpResponse("This is empty")
    else:
        if pw != conpw:
            return HttpResponse("password does not match")
        elif len(name) > 21:
            return HttpResponse("the name size must be below 21")

        else:

            user = get_object_or_404(User, id=uid)
            user.u_name = name
            user.password = pw
            user.save()
            return redirect("show_user")


###########################delete function #############################


def delete_user(req, uid):
    user = get_object_or_404(User, id=uid)
    user.delete()
    return redirect("show_user")
