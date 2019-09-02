from django.shortcuts import render, HttpResponse, redirect
from .models import User, Job
from django.contrib import messages

import bcrypt


def index(request):
    return render(request, "haiku_in_apps/index.html")

def regi(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            f_name = request.POST["fn"]
            l_name = request.POST["ln"]
            e_ma = request.POST["em"]
            p_w = request.POST["pa"]
        #######################
        # check to make sure to get information
            print(request.POST)
        ############send info to DB##########################
            hash1 = bcrypt.hashpw(p_w.encode(), bcrypt.gensalt())
            new = User.objects.create(first_name=f_name, last_name=l_name, email=e_ma, password=hash1)
            print(new)
            # ##### get last info from DB #############
            # send = User.objects.last()
            # return redirect(f'/shows/{send.id}')
            # #how to send info to 
            request.session['id'] = new.id
            request.session['f_name'] = new.first_name
            return redirect("/dashboard")

def login(request):
    if request.method == "POST":
        errors = User.objects.process_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            elemail = request.POST["mail_e"]
            elpas = request.POST["pass_word"]
            user =  User.objects.filter(email = elemail)
            if not user:
                messages.error(request, "Your email address doesn't exist")
                return redirect("/")
            else:
                user = User.objects.get(email=elemail)
                if bcrypt.checkpw(elpas.encode(), user.password.encode()):
                    print("password match")
                    request.session['id'] = user.id
                    request.session['f_name'] = user.first_name
                    return redirect("/dashboard")
                else:
                    print("failed password")
                    return redirect("/")

def dashbord(request):
    # us = User.objects.get(id=1)
    # 今ログインしているユーザの情報が欲しい　ユーザIDとトリップの情報が欲しい
    rrr = request.session['id']
    context = {
    	"dogs": Job.objects.filter(created_by=rrr),
        "jobs": Job.objects.exclude(created_by=rrr),
    }
    print(context['jobs'])

    return render(request, "haiku_in_apps/dashboard.html", context)

def add(request):
    context = {
    	"jobs": Job.objects.all()
    }
    return render(request, "haiku_in_apps/add.html", context)

def add_process(request):
    errors = Job.objects.process_add_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/jobs/new')
    #######################
    else:
        # request.method == "POST":
        tit = request.POST["s_tit"]
        net = request.POST["s_des"]
        funde = request.POST["s_loc"]
        #######################
        # check to make sure to get information
        print(request.POST)
        ############send info to DB##########################
        us = User.objects.get(id=request.session["id"])
        new = Job.objects.create(name=tit, description=net, location=funde,created_by=us)
        ##### get last info from DB #############
        send = Job.objects.last()
        return redirect("/dashboard")
        #how to send info to 

def edit(request,idr):
    context = {
        "jobs": Job.objects.get(id=idr),
    }
    return render(request, "haiku_in_apps/edit.html", context)

def edit_process(request,idr):
    errors = Job.objects.process_add_validator(request.POST)
    print("*"*80)
    print(errors)
    print("*"*80)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/trips/edit{idr}')
    else:
        tit = request.POST["s_tit"]
        funde = request.POST["s_des"]
        rel = request.POST["s_loc"]
        idd = request.POST["whatever"]
        print(request.POST)
        ####### need to update ########
        easy=Job.objects.get(id=idd)
        easy.name = tit
        easy.description = funde
        easy.location = rel
        easy.save()
        print("*"*80)
        print(easy.name)
        return redirect(f'/jobs/{easy.id}')

def show(request,idr):
    # ＃トリップのidをとってくる　トリップを特定したいから
    context = {
    	"jobs": Job.objects.get(id=idr),
    }
    print(context['jobs'].name)
    print(context['jobs'].created_by)
    return render(request, "haiku_in_apps/show.html", context)

def destroy(request):
    request.session.clear()
    return redirect("/")

def delete(reqest,idr):
    instance = Job.objects.get(id=idr)
    instance.delete()
    return redirect("/dashboard")