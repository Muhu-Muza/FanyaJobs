import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FanyaJobs.settings')

import django
django.setup()
from datetime import datetime
# import time
# from time import sleep




# headers = {'User-agent': 'Mozilla/5.0 (Windows 10; Win64; x64; rv:101.0.1) Gecko/20100101 Firefox/101.0.1'}
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
baseUrl = 'https://elitejobstoday.com/'
url = "https://elitejobstoday.com/"
# url = "https://elitejobstoday.com/page/2/"

try:
    r = requests.get(url, headers = headers)   
except requests.exceptions.ConnectTimeout:
    None

c = r.content
soup = BeautifulSoup(c, "lxml")
    


table = []
results = soup.find_all("a", attrs = {"class": "job-details-link"})
[table.append(x) for x in results if x not in table]


def jobScan(link):
     
    the_job = {}

    jobUrl = link['href']
    the_job['urlLink'] = jobUrl

    try:
        jobs = requests.get(jobUrl, headers = headers )      
    except requests.exceptions.ConnectTimeout:
        None

    jobC = jobs.content
    jobSoup = BeautifulSoup(jobC, "lxml")
        

    to_test = soup.find_all("a", attrs = {"class": "job-details-link"})

    if to_test == []:
        return None
    else:
        name = jobSoup.find("h1", attrs={"class": "page-title"})
        title = name.text
        the_job['title'] = title
 
        # company = jobSoup.find_all("span", {"class": "job-company"})[0]
        # company = company.text
        # the_job['company'] = company


        locas = jobSoup.find_all("span", {"class": "job-full-address"})[0]
        location = locas.text
        the_job['location'] = location


        # category = jobSoup.find_all("span", {"class" :"job-category"})[0]
        # category = category.text
        # the_job['category'] = category
 
        try:
            postDate = jobSoup.find_all("span", {"class": "job-date__posted"})[0]
            postDate = postDate.text
            date_posted = datetime.strptime(postDate.strip('\n'), '%B %d, %Y')
            the_job['date_posted'] = date_posted
        except:
            postDate = jobSoup.find_all("span", {"class": "job-date__posted"})[0]
            postDate = postDate.text
            date_posted = datetime.strptime(postDate.strip('\n'), ' %B %d, %Y')
            the_job['date_posted'] = date_posted

        try:
            closeDate = jobSoup.find_all("span", {"class": "job-date__closing"})[0]
            closeDate = closeDate.text
            closingdate = closeDate.replace('- ','')
            closing_date = datetime.strptime(closingdate.strip('\n'), '%B %d, %Y')
            the_job['closing_date'] = closing_date
        except:
            closeDate = jobSoup.find_all("span", {"class": "job-date__closing"})[0]
            closeDate = closeDate.text
            closingdate = closeDate.replace('- ','')
            closing_date = datetime.strptime(closingdate.strip('\n'), ' %B %d, %Y')
            the_job['closing_date'] = closing_date


        full_part_time = jobSoup.find_all("span", attrs={"class": "job-type"})[0]
        full_part_time = full_part_time.text
        the_job['nature'] = full_part_time

 
        desc = jobSoup.find("div", attrs={"class": "job-desc"})            
        paragraphs = desc.find_all("p") 

        description = ''

        for p in paragraphs:
            description += p.text
            the_job['description'] = description
           
        return the_job


from jobapp.models import *
from django.contrib.auth.models import User

final_jobs = []
# final_jobs = final_jobs[:10]

for a in table:
    job = jobScan(a)
    if job:
        final_jobs.append(job)
    else:
        None


the_user = User.objects.get(email = 'muhumuza@gmail.com')
the_company = Company.objects.get(uniqueId = 'ba468201')
# the_category = Category.objects.get(uniqueId = '')


for test_job in final_jobs:

    try:

        if 'manager' in test_job['title']:
            the_category = Category.objects.get(title='Manager')
        elif 'engineer' in test_job['title']:
            the_category = Category.objects.get(title= 'Engineer')
        elif 'architect' in test_job['title']:
            the_category = Category.objects.get(title='Architect')
        elif 'developer' in test_job['title'] or 'software' in test_job['title']:
            the_category = Category.objects.get(title='SoftwareDeveloper')
        elif 'bank' in test_job['title']:
            the_category = Category.objects.get(title='Bank')
        elif 'accountant' in test_job['title']:
            the_category = Category.objects.get(title='Accountant')
        elif 'HR' in test_job['title'] or 'Human Resource' in test_job['title']:
            the_category = Category.objects.get(title='HumanResource')
        elif 'Education' in test_job['title']:
            the_category = Category.objects.get(title='Education')
        elif 'officer' in test_job['title'] or 'administrator' in test_job['title']:
            the_category = Category.objects.get(title='Administrator')
        elif 'finance' in test_job['title'] or 'financial' in test_job['title']:
            the_category = Category.objects.get(title='Finance')
        elif 'supervisor' in test_job['title']:
            the_category = Category.objects.get(title='Supervisor') 
        elif 'doctor' in test_job['title'] or 'pharmacy' in test_job['title'] or 'medical' in test_job['title']:
            the_category = Category.objects.get(title='Medical')
        elif 'Nurse' in test_job['title'] or 'Nursing' in test_job['title']:
            the_category = Category.objects.get(title='Nursing')
        elif 'Service' in test_job['title'] or 'Customer' in test_job['title']:
            the_category = Category.objects.get(title='CustomerService')
        elif 'research' in test_job['title']:
            the_category = Category.objects.get(title='Research')
        elif 'insurance' in test_job['title']:
            the_category = Category.objects.get(title='Insurance')
        elif 'driver' in test_job['title']:
            the_category = Category.objects.get(title='Driver')
        elif 'IT' in test_job['title']  or 'graphic' in test_job['title'] or 'computer' in test_job['title']:
            the_category = Category.objects.get(title='Computing')
        elif 'ngo' in test_job['title']:
            the_category = Category.objects.get(title='NGO')
        else:
            the_category = Category.objects.get(title="Uncategorised")
  
        newjob = Jobs.objects.create(
            title = test_job['title'],
            location = test_job['location'],
            # category = test_job['category'],
            date_posted = test_job['date_posted'],
            closing_date = test_job['closing_date'],
            nature = test_job['nature'],
            urlLink = test_job['urlLink'],
            description = test_job['description'],
            category = the_category,
            company = the_company,
            owner = the_user,
        )

    except Category.DoesNotExist:
        the_category = None

# print(final_jobs)
# print(len(final_jobs))





