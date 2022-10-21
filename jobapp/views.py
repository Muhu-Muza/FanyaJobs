from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from userapp.models import User


# def index(request):
#     listed_jobs = Jobs.objects.all()
#     listed_jobs = Jobs.objects.order_by('title')[:10]
#     # elitejobs = Jobs.objects.filter(company__title='EliteJobsToday')[:5]
#     # alljobs = Jobs.objects.filter(company__title='alljobspo')[:5]
    
#     # context = {}
#     # context['jobapp'] = elitejobs
#     # context['jobapp'] = alljobs
#     # listed_jobs = Jobs.objects.order_by('date_created')[:30]

#     return render(request, 'index.html', {'jobapp': listed_jobs})

def index(request):

 
    # return render(request, 'index.html', {'jobapp': listed_jobs})

    form = SearchForm()

    listed_jobs = Jobs.objects.all()
    listed_jobs = Jobs.objects.order_by('closing_date')[:10]

    # elitejobs = Jobs.objects.filter(company__title='EliteJobsToday')[:5]
    # alljobs = Jobs.objects.filter(company__title='alljobspo')[:5]


    context = {}

    context['jobapp'] = listed_jobs
    # context['elitejobs'] = elitejobs
    # context['alljobs'] = alljobs
   

    context['Manager'] = Category.objects.get(title='Manager')
    context['Engineer'] = Category.objects.get(title='Engineer')
    context['Architect'] = Category.objects.get(title='Architect')
    context['SoftwareDeveloper'] = Category.objects.get(title='SoftwareDeveloper')
    context['Bank'] = Category.objects.get(title='Bank')
    context['Finance'] = Category.objects.get(title='Finance')
    context['Supervisor'] = Category.objects.get(title='Supervisor')
    context['Research'] = Category.objects.get(title='Research')
    context['Insurance'] = Category.objects.get(title='Insurance')
    context['Driver'] = Category.objects.get(title='Driver')
    context['Medical'] = Category.objects.get(title='Medical')
    context['Computing'] = Category.objects.get(title='Computing')
    context['NGO'] = Category.objects.get(title='NGO')
    context['Human Resource'] = Category.objects.get(title='HumanResource')
    context['Education'] = Category.objects.get(title='Education')
    context['Administrator'] = Category.objects.get(title='Administrator')
    context['Nursing'] = Category.objects.get(title='Nursing')
    context['Customer Service'] = Category.objects.get(title='CustomerService')
    context['Others'] = Category.objects.get(title='Others')

    
    context['form'] = form

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('title')

            jobs = []
            if len(search.split())>1:
                search_list = search.split()
                item_list = []
                for item in search_list:
                    a_list = Jobs.objects.filter(title__icontains=item)
                    for x in a_list:
                        item_list.append(x)
                [jobs.append(x) for x in item_list if x not in jobs]        
                
                return render(request, 'job-list.html', {'jobapp': jobs})
            else:
                jobs = Jobs.objects.filter(title__icontains=search)

                return render(request, 'job-list.html', {'jobapp': jobs})
        else:
            messages.error(request, 'Error Processing Your Request')
            context['form'] = form
            return render(request, 'index.html', context)
    
    return render(request, 'index.html', context)
    # job_list = Jobs.objects.order_by('date_created')[:30]

def terms(request):
    return render(request, 'terms-and-conditions.html',{})

@login_required
def job_list(request):
    # job_list = Jobs.objects.all()
    # job_list = job_list[:20]
  
    job_list = Jobs.objects.order_by('-date_created')

    return render(request, 'job-list.html', {'jobapp': job_list})

@login_required
def job_detail(request, slug):
    the_job = Jobs.objects.get(slug=slug)

    return render(request, 'job-detail.html', {'object': the_job })

def category_detail(request, slug):
    the_category = Category.objects.get(slug=slug)
    context = {}

    jobs = Jobs.objects.filter(category__slug=slug)[:20]
    context['jobs'] = jobs
    context['the_category'] = the_category

    return render(request, 'category-detail.html', context)


def contact(request):
    if request.method =="POST":
        contact=Contact()
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact.fname = firstname 
        contact.lname = lastname
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return HttpResponse("<h2>FanyaJobs</h2> <br><p>Thanks for Contacting FanyaJobs. Our service team will get in touch with you soon.</p>")

    return render(request, 'contact.html',{})

def add_job(request):
    categories_data = Category.objects.all()
    context = {'categories': categories_data}
    companies = Company.objects.all()
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.owner = request.user
            for company in companies:
                if company.employer_id == request.user.id:
                    obj.company = company
                    
            obj.save()
            messages.success(request, 'Job added Successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'add-job.html', context)

    else:
        form = JobForm()
        context = {'form': form}
        return render(request, 'add-job.html', context)

@login_required
def register_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.employer = User.objects.get(id=request.user.id)
            obj.save()
            messages.success(request, "Company saved successfully")
            return redirect('profile')
        else:
            messages.error(request, "Error processing your request")
            context = {'form': form}
            return render(request, 'register_company.html', context)
    else:
        form = CompanyForm()
        context = {'form': form}
        return render(request, 'register_company.html', context)
    
   
    


