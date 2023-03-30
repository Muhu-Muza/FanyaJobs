from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from datetime import datetime
from .functions import WelcomeEmail, sendEmail, ForgotEmail


from django.conf import settings

# from django.core.mail import send_mail

from django.views.static import serve
import os
from uuid import uuid4
# from django.contrib.auth.models import User

from userapp.models import User

# from django.contrib.auth import get_user_model
# User = get_user_model()


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            
            # send email to user
            # to_email = form.cleaned_data.get('email')
            # welcome = WelcomeEmail()
            # sendEmail(welcome.email, welcome.subject, [to_email])

            # send success to user
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            return redirect('login_page')
        else:
            
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register.html', context)

    return render(request, 'login.html', {})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')
            

    context = {}
    return render(request, 'login.html', context)


@login_required
def profile(request):
    return render(request, 'profile.html',{})


def logout_user(request):
    logout(request)
    return redirect('logout.html/')



@login_required
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)

            obj.user = request.user

            obj.save()

            messages.success(request, 'Resume created Successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'create-resume.html', context)

    if request.method == 'GET':
        form = ResumeForm()
        context = {'form': form}
        return render(request, 'create-resume.html', context)

    return render(request, 'create-resume.html', {})


def update_resume(request, resume_id):
    context = {}
    obj = get_object_or_404(Resume, id=resume_id)
    form = ResumeForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('profile')

    context['form'] = form
    return render(request, 'update-resume.html', context)
    

class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'resume-detail.html'


def resume_detail(request, slug):
    edu_form = EducationForm()
    exp_form = ExperienceForm()

    obj  = Resume.objects.get(slug = slug)

    educations = Education.objects.filter(resume = obj)
    experiences = Experience.objects.filter(resume = obj)
    context = {}
    context['object'] = obj
    context['educations'] = educations
    context['experiences'] = experiences

    if request.method == 'POST':
        edu_form = EducationForm(request.POST)
        exp_form = ExperienceForm(request.POST)

        if edu_form.is_valid():
            o = edu_form.save(commit = False)
            o.resume = obj
            o.save()

            messages.success(request, 'Resume updated Successfully')
            return redirect('resume-detail', slug = slug)

        if exp_form.is_valid():
            p = exp_form.save(commit = False)
            p.resume = obj
            p.save()

            messages.success(request, 'Resume updated Successfully')
            return redirect('resume-detail', slug = slug)

        else:
            messages.error(request, 'Error Processing Your Request')
            context['edu_form'] = edu_form
            context['exp_form'] = exp_form
            return render(request, 'resume-detail.html', context)

    context['edu_form'] = edu_form
    context['exp_form'] = exp_form
    return render(request, 'resume-detail.html', context)


def update_view_education(request, education_id):
    context = {}
    obj = get_object_or_404(Education, id=education_id)
    form = EducationForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('profile')
        # return render(request, 'profile.html', context)

    context['edu_form'] = form
    return render(request, 'update-education.html', context)


def update_view_experience(request, experience_id):
    context = {}
    obj = get_object_or_404(Experience, id=experience_id)
    form = ExperienceForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        # return redirect('profile')
        return render(request, 'profile.html', context)

    context['exp_form'] = form
    return render(request, 'update-experience.html', context)


def delete_view_education(request, education_id):
    context={}
    education_instance=get_object_or_404(Education, id=education_id) 
    if education_instance:
        education_instance.delete()
        messages.success(request,"Information Deleted Successfully")

    return render(request, 'profile.html', context)


def delete_view_experience(request, experience_id):   
    context={}
    experience_instance=get_object_or_404(Experience, id=experience_id)  
    if experience_instance:
        experience_instance.delete()
        messages.success(request,"Information Deleted Successfully")

    return render(request, 'profile.html', context)


def about_us(request):
    return render(request, 'aboutus.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def resume_list(request):
    resume_list = Resume.objects.all()
    resume_list = Resume.objects.order_by('district')
    return render(request, 'resume-list.html', {'userapp': resume_list,})
                                            
                                                

def resume_full(request, id):
    the_resume = Resume.objects.get(id=id)
    the_edu = Education.objects.get(resume=id)
    the_exp = Experience.objects.get(resume=id)
    return render(request, 'resume-full.html', {
                                                
                                                'object_exp': the_exp,
                                                'object_edu': the_edu,
                                                'object_res': the_resume,
                                                })
                                                
                                                


  
    

    












# def test_email(request):

#     send_mail('Hello from FanyaJobs',
#             'hello there, Trust FanyaJobs',
#             'fanyajobs256@gmail.com',
#             ['schumannivan@gmail.com'],
#             fail_silently=False)
    

    # return render(request, 'basic.html', {})


# def test(request):
#     return render(request, 'basic.html', {})

def download(request, foldername, filename):
    file_path = settings.MEDIA_ROOT +'/'+foldername+'/'+ filename
    return serve(request, os.path.basename(file_path), os.path.dirname(file_path))



def forgot(request):
    if request.method == 'POST':
        form = ForgotForm(request.POST)
        if form.is_valid():
            user_email = request.POST['email'].lower().replace(' ', '')

            u = User.objects.get(email=user_email)
            if u is not None:

                new_pass = str(uuid4()).split('-')[4]

                forgot = ForgotEmail(new_pass)
                # send the Forgot Email . . .
                to_email = u.email

                e_mail = forgot.email()
                sendEmail(e_mail, forgot.subject, [to_email])

                u.set_password(new_pass)
                u.save()

                messages.success(request, 'your password has been rest, check your email for more details')
                return redirect('login_page')
            else:
                messages.error(request, 'we could not find a user with a matching email')
                return redirect('home_page')

        else:
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'forgot.html', context)

    if request.method == 'GET':
        form = ForgotForm()
        context = {'form': form}
        return render(request, 'forgot.html', context)

    return render(request, 'forgot.html', {})
