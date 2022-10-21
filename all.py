from unicodedata import category
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FanyaJobs.settings')

import django
django.setup()
from datetime import datetime

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
baseUrl = 'https://www.alljobspo.com/uganda-jobs/'
url = "https://www.alljobspo.com/uganda-jobs/"

r = requests.get(url, headers = headers)
c = r.content
soup = BeautifulSoup(c, "lxml")


table = []

results = soup.find_all("article", attrs = {"class": "job"})
for x in results:
    x = x.h2
    x = x.a

[table.append(x) for x in results if x not in table]




def jobScan(link):
     
    the_job = {}

    # leenk = soup.find_all("article", attrs={"class": "job"})
    # for link in leenk:
    #     link = link.a

        # link = leenk.a
    jobUrl = link['href']
    the_job['urlLink'] = jobUrl
    # jobUrl = link['href']
    # the_job['urlLink'] = jobUrl

    jobs = requests.get(jobUrl, headers = headers )
    jobC = jobs.content
    jobSoup = BeautifulSoup(jobC, "lxml")

    to_test = soup.find_all("article", attrs = {"class": "job"})
    
    
    if to_test == []:
        return None
    else:
        name = jobSoup.find("h1")
        title = name.a.text
        the_job['title'] = title
        
        locas = soup.find_all("span", attrs = {"class": "value"})[0]
        location = locas.text
        the_job['location'] = location
        
        postDate = jobSoup.find_all("span", {"data-value": "2016-04-03 12:00:00 AM"})[0]
        postDate= postDate.text[14:]
        date_post = postDate.replace('th','')
        date_posted = datetime.strptime(date_post.strip('\n'), '%d %B %Y')
        the_job['date_posted'] = date_posted

        description = soup.find_all("div", attrs={"class": "summary"})[0]
        description = description.p.text
        the_job['description'] = description
    
        return the_job    

# jobScan(table)



from jobapp.models import *
from django.contrib.auth.models import User

final_jobs = []

for a in table:
    job = jobScan(a)
    if job:
        final_jobs.append(job)
    else:
        None
    




the_user = User.objects.get(email = 'muhumuza@gmail.com')
the_company = Company.objects.get(uniqueId = 'a4f68910')
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
            the_category = Category.objects.get(title='Developer/Software')
        elif 'bank' in test_job['title']:
            the_category = Category.objects.get(title='Bank')
        elif 'accountant' in test_job['title']:
            the_category = Category.objects.get(title='Accountant')
        elif 'HR' in test_job['title'] or 'Human Resource' in test_job['title']:
            the_category = Category.objects.get(title='Human Resource')
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
            the_category = Category.objects.get(title='Customer Service')
        elif 'research' in test_job['title']:
            the_category = Category.objects.get(title='Research')
        elif 'insurance' in test_job['title']:
            the_category = Category.objects.get(title='Insurance')
        elif 'driver' in test_job['title']:
            the_category = Category.objects.get(title='Driver')
        elif 'IT' in test_job['title'] or 'developer' in test_job['title'] or 'graphic' in test_job['title'] or 'computer' in test_job['title']:
            the_category = Category.objects.get(title='Computing')
        elif 'ngo' in test_job['title']:
            the_category = Category.objects.get(title='NGO')
        else:
            the_category = Category.objects.get(title="Uncategorised")
  
        newjob = Jobs.objects.create(
            urlLink = test_job['urlLink'],
            title = test_job['title'],
            location = test_job['location'],
            # category = test_job['category'],
            date_posted = test_job['date_posted'],
            description = test_job['description'],
            company = the_company,
            category = the_category,
            owner = the_user,
        )

    except Category.DoesNotExist:
        the_category = None


print(final_jobs)
print(len(final_jobs))




