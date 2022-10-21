# from webbrowser import WindowsDefault
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from uuid import uuid4
import random
from django.conf import settings

# from django.contrib.auth import get_user_model
# User = get_user_model()


# class User(AbstractUser):
#     is_email_verified = models.BooleanField(default=False)

#     def __str__(self):
#         return self.email

class User(AbstractUser):
    JOB_SEEKER = "JOB SEEKER"
    EMPLOYER = "EMPLOYER"

    ROLES = (
        (JOB_SEEKER, JOB_SEEKER),
        (EMPLOYER, EMPLOYER)
    )

    role = models.CharField(max_length=200, choices=ROLES, default="JOB SEEKER", verbose_name="role")

    def __str__(self) -> str:
        return f"{self.username} - {self.role}"

    


class Resume(models.Model):
    MALE ='Male'
    FEMALE = 'Female'
    OTHER = 'Other'
    MARRIED = 'Married'
    SINGLE = 'Single'
    WIDOWED = 'Widowed'
    DIVORCED =  'Divorced'

    KAMPALA = 'Kampala'
    MASAKA = 'Masaka'
    MUKONO = 'Mukono'
    JINJA = 'Jinja'
    MBARARA = 'Mbarara'
    KABALE = 'Kabale'
    ARUA = 'Arua'
    GULU = 'Gulu'
    MBALE = 'Mbale'
    LIRA = 'Lira'
    FORTPORTAL = 'Fortportal'

    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    MARITAL_CHOICES = [
        (MARRIED, 'Married'),
        (SINGLE, 'Single'),
        (WIDOWED, 'Widowed'),
        (DIVORCED, 'Divorced'),
    ]

    DISTRICT_CHOICES = [
        (KAMPALA, 'Kampala'),
        (MASAKA, 'Masaka'),
        (MUKONO, 'Mukono'),
        (JINJA, 'Jinja'),
        (MBARARA, 'Mbarara'),
        (KABALE, 'Kabale'),
        (ARUA, 'Arua'),
        (GULU, 'Gulu'),
        (MBALE, 'Mbale'),
        (LIRA, 'Lira'),
        (FORTPORTAL, 'Fortportal ')
    ]

    IMAGES = [
        'profile1.png', 'profile2.png', 'profile3.png', 'profile4.png', 'profile5.png', 
        'profile6.png', 'profile7.png', 'profile8.png', 'profile9.png', 'profile10.png', 
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    uniqueId = models.CharField(null=True, blank=True, max_length=200)
    image = models.FileField(default = 'default.jpg', upload_to='profile_images', null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    date_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(choices=SEX_CHOICES, default=OTHER, max_length=200)
    marital_status = models.CharField(choices=MARITAL_CHOICES, default=SINGLE, max_length=200)
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
    addressLine2 = models.CharField(null=True, blank=True, max_length=200)
    village = models.CharField(null=True,blank=True, max_length=200)
    city = models.CharField(null=True, blank=True, choices=DISTRICT_CHOICES, default=KAMPALA, max_length=200)
    district = models.CharField(choices=DISTRICT_CHOICES, default=KAMPALA, max_length=100)
    phoneNumber = models.CharField(null=True, blank=True, max_length=200)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(default= timezone.now)
    # last_updated = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(default=timezone.now)
    cover_letter = models.FileField( null=True, blank=True,)
    cv = models.FileField( null=True, blank=True,)
    

    
    def __str__(self):
        return '{} {} {}'.format(self.user.first_name, self.user.last_name, self.uniqueId)

    def get_absolute_url(self):
        return reverse('resume-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):

        # Creating a unique Identifier for the resume(useful for other things in future)
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[0]

            self.slug = slugify('{} {} {}'.format(self.user.first_name, self.user.last_name, self.uniqueId))
        # Creating the slugField for the URL - to detailed page
        
            
        # assign a default profile image
        # if self.image == 'default.jpg':
        #     self.image = random.choice(self.IMAGES)

        # keep track of everytime someone updates the resume, everytime the instance is saved, --this should update
        
        self.slug = slugify('{} {} {}'.format(self.user.first_name, self.user.last_name, self.uniqueId))
        super(Resume, self).save(*args, **kwargs)


class Education(models.Model):
    LEVEL5A = 'NQF 5 - Certificate'
    LEVEL5B = 'NQF 5 - Higher Certificate'
    LEVEL5C = 'NQF 5 - Diploma'
    LEVEL6A = 'NQF 6 - Bachelors Degree'
    LEVEL6B = 'NQF 6 - Honours Degree'
    LEVEL6C = 'NQF 6 - Postgraduate Diploma'
    LEVEL7A = 'NQF 7 - Postgraduate Degree'
    LEVEL7B = 'NQF 7 - Masters Degree'
    LEVEL7C = 'NQF 7 - Doctors Degree'

    LEVEL_CHOICES = [

        (LEVEL5A, 'NQF 5 - UBTEB Certificate'),
        (LEVEL5B, 'NQF 5 - A-Level Certificate'),
        (LEVEL5C, 'NQF 5 - Diploma'),
        (LEVEL6A, 'NQF 6 - Bachelors Degree'),
        (LEVEL6B, 'NQF 6 - Honours Degree'),
        (LEVEL6C, 'NQF 6 - Postgraduate Diploma'),
        (LEVEL7A, 'NQF 7 - Postgraduate Degree'),
        (LEVEL7B, 'NQF 7 - Masters Degree'),
        (LEVEL7C, 'NQF 7 - Doctors Degree'),

    ]

    institution = models.CharField(null=True, max_length=200)
    qualification = models.CharField(null=True, max_length=200)
    level = models.CharField(choices=LEVEL_CHOICES, default=LEVEL5A, max_length=200)
    start_date = models.DateField()
    graduated = models.DateField()
    major_subject = models.CharField(null=True, max_length=200)
    date_created = models.DateTimeField(default = timezone.now)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return '{} with {} at {}'.format(self.qualification, self.level, self.institution)



class Experience(models.Model):

    company = models.CharField(null = True, max_length=200)
    position = models.CharField(null = True, max_length=200)
    start_date = models.DateField()
    end_date  = models.DateField()
    experience = models.TextField()
    skills = models.TextField()
    resume = models.ForeignKey(Resume, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return '{} at {}'.format(self.position, self.company)



