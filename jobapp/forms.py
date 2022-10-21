from django import forms
from string import capwords
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class SearchForm(forms.ModelForm):
    title = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter Search Keyword'}),
    )

    class Meta:
        model = Jobs
        fields = ['title']




class JobForm(forms.ModelForm):

    FULL_TIME = 'Full Time'
    PART_TIME = 'Part Time'
    INTERNSHIP = 'Internship'

    TYPE_CHOICES = [
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
        (INTERNSHIP, 'Internship')
    ]

    # CATEGORY_CHOICES = []

    # CATEGORY = 'category'

    # categories = Category.objects.all()
    # for category in categories:
    #     cat = Category.objects.get(id=category.id)
    #     print(cat)
    #     CATEGORY_CHOICES.append((cat, capwords(category.title)))

    # CATEGORY_CHOICES = [
    #     (CATEGORY, 'category')
    # ]

    title = forms.CharField(
                required = True,
                widget =  forms.TextInput(attrs = {'class': 'form-control ', 'placeholder': 'e.g Software Engineer'}),
                )

    location = forms.CharField(
                required = True,
                widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Enter Location'}),
                )

    nature = forms.ChoiceField(
                choices = TYPE_CHOICES,
                required = True,
                widget = forms.Select(attrs = {'class': 'selectpicker border rounded', 'placeholder': ''}),
                )

    category = forms.ModelChoiceField(
                queryset=Category.objects.all(),
                required = True,
                widget = forms.Select(attrs = {'class': 'selectpicker border rounded', 'placeholder': 'select category'}),
                )

    salary = forms.CharField(
                required = False,
                widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'e.g 800,000'}),
                )

    description = forms.CharField(
                required = True,
                widget = forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Enter Job Description'}),
                )

    date_posted = forms.DateField(
                required = True,
                widget = DateInput(attrs = {'class': 'form-control', 'placeholder': 'Enter experience'}),
                )

    closing_date = forms.CharField(
                required = True,
                widget = DateInput(attrs = {'class': 'form-control', 'placeholder': 'Enter skills attained'}),
                )

    urlLink = forms.CharField(
                required = False,
                widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'e.g https://example.com'}),
                )

    
    class Meta:
        model = Jobs

        fields = [
            "title",
            "location",
            "nature",
            "category",
            "salary",
            "description",
            "date_posted",
            "closing_date",
            "urlLink"
        ]

class CompanyForm(forms.ModelForm):

    title = forms.CharField(
                required = True,
                widget =  forms.TextInput(attrs = {'class': 'form-control ', 'placeholder': 'Enter the name of your company'}),
                )

    description = forms.CharField(
                required = True,
                widget = forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'What does your company do?'}),
                )

    companyLogo = forms.ImageField(
                required = False,
                widget = forms.FileInput(attrs = {'class': 'form-control', 'placeholder': 'Choose file to upload'}),
                )

    
    class Meta:
        model = Company

        fields = [
            "title",
            "description",
            "companyLogo",
           
        ]
