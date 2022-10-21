from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
# settings.configure(DEBUG=True)
from django.template.defaultfilters import slugify
from uuid import uuid4
from django.urls import reverse




class Company(models.Model):
    title = models.CharField(max_length = 500, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    uniqueId = models.CharField(null = True, blank = True, max_length= 100)
    companyLogo = models.ImageField(default = 'default.png', upload_to = 'upload_images')
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="employer", on_delete=models.CASCADE)
    slug = models.SlugField(max_length= 500, unique = True, blank = True, null = True)
    seoDescription = models.CharField(max_length = 500, null = True, blank = True)
    seoKeywords = models.CharField(max_length = 500, null = True, blank = True)


    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('company-detail', kwargs = {'slug': self.slug})

    def save(self, *args, **kwargs):
        # if self.uniqueId is None:
        #     self.uniqueId = str(uuid4()).split('-')[0]
        #     self.slug = slugify('Company {} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('Company {}'.format(self.title))
        self.seoDescription = 'Apply for {} Jobs online, start your career journey today'.format(self.title)
        self.seoKeywords = '{}, Jobs, FanyaJobs|Ug, Apply for Jobs'.format(self.title)
        super(Company, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Companies"

    
class Category(models.Model):
    title = models.CharField(max_length= 200, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    uniqueId = models.CharField(null = True, blank = True, max_length = 100)
    categoryImage = models.ImageField(default = 'category.png', upload_to = 'upload_images')
    slug = models.SlugField(max_length = 500, unique=True, blank = True, null = True)
    seoDescription = models.CharField(max_length = 500, null = True, blank = True)
    seoKeywords = models.CharField(max_length = 500, null = True, blank = True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('category-detail', kwargs = {'slug': self.slug})

    def save(self, *args, **kwargs):
        # if self.uniqueId is None:
        #     self.uniqueId = str(uuid4()).split('-')[0]
        #     self.slug = slugify('Category {} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('Category {}'.format(self.title))
        self.seoDescription = 'Apply for {} Jobs online, start your career journey today'.format(self.title)
        self.seoKeywords = '{}, Jobs, FanyaJobs|Ug, Apply for Jobs'.format(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"

class Jobs(models.Model):

    FULL_TIME = 'Full Time'
    PART_TIME = 'Part Time'
    INTERNSHIP = 'Internship'
    NOT_PROVIDED = 'N/A'
    TIER1 = 'Less than 2yrs'
    TIER2 = '2yrs - 5yrs'
    TIER3 = '5yrs -10yrs'
    TIER4 = '10yrs - 15yrs'
    TIER5 = 'More than 15yrs'

    TYPE_CHOICES = [
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part TIme'),
        (NOT_PROVIDED, 'N/A'),
        (INTERNSHIP, 'INTERNSHIP'),
    ]

    EXP_CHOICES = [
        (TIER1, 'Less than 2yrs'),
        (TIER2, '2yrs - 5yrs'),
        (TIER3, '5yrs - 10yrs'),
        (TIER4, '10yrs - 15yrs'),
        (TIER5, 'More than 15yrs'),
        (NOT_PROVIDED, 'N/A'),
    ]


    title = models.CharField(max_length=1000, null = True, blank = True)
    company = models.ForeignKey(Company, on_delete = models.CASCADE, null = True, blank = True)
    category = models.ForeignKey(Category, related_name= 'Category', on_delete = models.CASCADE, null = True, blank = True)
    location = models.CharField(max_length=1000, null = True, blank = True)
    salary = models.CharField(max_length=1000, null = True, blank = True)
    uniqueId = models.CharField(null = True, blank = True, max_length = 100)
    nature = models.CharField(max_length=100, choices=TYPE_CHOICES, default=NOT_PROVIDED)
    experience = models.CharField(max_length=100, choices=EXP_CHOICES, default=NOT_PROVIDED)
    summary = models.TextField(null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    requirements = models.TextField(null = True, blank = True)
    duties = models.TextField(null = True, blank = True)
    enquiries = models.TextField(null = True, blank = True)
    applications = models.TextField(null = True, blank = True)
    note = models.TextField(null = True, blank = True)
    closing_date = models.DateField(blank = True, null = True)
    date_posted = models.DateField(blank = True, null = True)
    contract_type = models.CharField(max_length = 1000, null = True, blank = True)
    date_created = models.DateTimeField(default = timezone.now) 
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    slug = models.SlugField(max_length = 1000, unique = True, blank = True, null = True)
    seoDescription = models.CharField(max_length =1000, null = True, blank =True)
    seoKeywords = models.CharField(max_length=1000, null = True, blank = True)
    urlLink = models.CharField(max_length=1000, null = True, blank = True)


    def __str__(self):
        return '{} - {}'.format(self.company, self.title)

    def get_absolute_url(self):
        return reverse('job-detail', kwargs = {'slug': self.slug})

    def save(self, *args, **kwargs):
        # creating a unique identifier for the resume(useful for other things in the future)
        # if self.uniqueId is None:
        #     self.uniqueId = str(uuid4()).split('-')[0]
        #     self.slug = slugify('{} {} {}'.format( self.title, self.location, self.uniqueId))
    
        self.slug = slugify('{} {}'.format( self.title, self.location))
        # self.seoKeywords = 'FanyaJobs, Online job application, full time jobs, get a job, apply for a job, {}, {}'.format(self.company.title, self.title)
        # self.seoDescription = '{}'.format('FanyaJobs {} Job application. Apply for job: {} in {}, online today'.format(self.company.title, self.title, self.location))
        super(Jobs, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Jobs"

    
class Contact(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    subject = models.TextField(max_length=200)
    message = models.TextField(max_length=1000)
    
    def __str__(self):
        return '{} {} {}, {} || {}' .format(self.firstname, self.lastname, self.email, self.subject, self.message)
    
    
   

