from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from .models import Resume, Education, Experience, User

class DateInput(forms.DateInput):
    input_type = 'date'


class RegisterForm(UserCreationForm):

    JOB_SEEKER = "JOB SEEKER"
    EMPLOYER = "EMPLOYER"

    ROLE_CHOICES = [
        (JOB_SEEKER, "JOB SEEKER"),
        (EMPLOYER, "EMPLOYER")
    ]

    check = forms.BooleanField(required = True)
    role = forms.ChoiceField(
        required=True,
        choices=ROLE_CHOICES,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            'required':'',
            'placeholder':'Enter Username',
            'class': 'form-control',
            'maxlength':'30',
            'minlength':'5',
            'type':'text',
            'name':'username',
            'id':'username'
        })

        self.fields["email"].widget.attrs.update({
            'required':'',
            'placeholder':'Enter Email address',
            'class': 'form-control',
            'maxlength':'30',
            'minlength':'5',
            'type':'email',
            'name':'email',
            'id':'email'
        })

        self.fields["first_name"].widget.attrs.update({
            'required':'',
            'placeholder':'e.g Mary',
            'class': 'form-control',
            'maxlength':'20',
            'minlength':'2',
            'type':'text',
            'name':'first_name',
            'id':'first_name'
        })

        self.fields["last_name"].widget.attrs.update({
            'required':'',
            'placeholder':'e.g Jane',
            'class': 'form-control',
            'maxlength':'20',
            'minlength':'2',
            'type':'text',
            'name':'last_name',
            'id':'last_name'
        })



        self.fields["password1"].widget.attrs.update({
            'required':'',
            'placeholder':'Enter password',
            'class': 'form-control',
            'maxlength':'22',
            'minlength':'8',
            'type':'password',
            'name':'password1',
            'id':'password1'
        })

        self.fields["password2"].widget.attrs.update({
            'required':'',
            'placeholder':'confirm password',
            'class': 'form-control',
            'maxlength':'22',
            'minlength':'8',
            'type':'password',
            'name':'password2',
            'id':'password2'
        })

        

        self.fields["check"].widget.attrs.update({
            'required':'True'
            
        })

        self.fields["role"].widget.attrs.update({
            'required':'',
            'placeholder':'Select role',
            'class': 'selectpicker border rounded',
            'type': 'text',
            'name': 'role',
            'id': 'role'
        })

    
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1','password2', 'check', 'role')
    #     email = forms.EmailField(
    #         max_length=100,
    #         required = True,
    #         help_text='Enter Email Address',
    #         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    #     )

    #     first_name = forms.CharField(
    #         max_length=100,
    #         required = True,
    #         help_text='Enter First Name',
    #         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first Name'}),
    #     )

    #     last_name = forms.CharField(
    #         max_length=100,
    #         required = True,
    #         help_text='Enter Last Name',
    #         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    #     )

    #     username = forms.CharField(
    #         max_length=200,
    #         required = True,
    #         help_text='Enter Username',
    #         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    #     )

    #     password1 = forms.CharField(
    #         help_text='Enter Password',
    #         required = True,
    #         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    #     )

    #     password2 = forms.CharField(
    #         help_text='Enter Password',
    #         required = True,
    #         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
    #     )

        # check = forms.BooleanField(required = True)


    # class Meta:
    #     model = User
    #     fields = [
    #         'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'check',
    #     ]


class ForgotForm(forms.ModelForm):
    email = forms.EmailField(
        max_length = 100,
        required = True,
        help_text = 'Enter Email Address',
        widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Enter Email'}),
    )


    class Meta:
        model = User
        fields = [
            'email',
            ]




class ResumeForm(forms.ModelForm):
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

    image = forms.ImageField(
        required = False,
        widget = forms.FileInput(attrs={'class': 'form-control'}),
    )

    date_birth = forms.DateField(
        required=True,
        widget=DateInput(attrs={'class': 'form-control', 'placeholder': 'Enter a date'}),
    )

    sex = forms.ChoiceField(
        choices = SEX_CHOICES,
        widget=forms.Select(attrs={'class': 'nice-select rounded'}),
    )

    marital_status = forms.ChoiceField(
        choices= MARITAL_CHOICES,
        widget=forms.Select(attrs={'class': 'nice-select rounded'}),
    )

    addressLine1 = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Address Line 1'}),
    )

    addressLine2 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Address Line 2'}),
    )

    village = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Village'}),
    )

    city = forms.ChoiceField(
         choices = DISTRICT_CHOICES,
         required=True,
         widget=forms.Select(attrs={'class': 'form-control resume', 'placeholder': 'Enter City'}),
    )

    district = forms.ChoiceField(
        choices = DISTRICT_CHOICES,
        widget = forms.Select(attrs={'class': 'nice-select rounded'}),
    )

    phoneNumber = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control resume', 'placeholder': 'Enter Phone Number'}),
    )

    cover_letter = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}),
    )

    cv = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Resume
        fields = [
            'image',
            'date_birth',
            'sex',
            'marital_status',
            'addressLine1',
            'addressLine2',
            'village',
            'city',
            'district',
            'phoneNumber',
            'cover_letter',
            'cv', 
        ]




class ExperienceForm(forms.ModelForm):
    company = forms.CharField(
                required = True,
                widget =  forms.TextInput(attrs = {'class': 'form-control resume', 'placeholder': 'company Worked For'}),
                )

    position = forms.CharField(
                required = True,
                widget = forms.TextInput(attrs = {'class': 'form-control resume', 'placeholder': 'Position/Role'}),
                )

    start_date = forms.DateField(
                required = True,
                widget = DateInput(attrs = {'class': 'form-control', 'placeholder': 'Enter a date'}),
                )

    end_date = forms.DateField(
                required = True,
                widget = DateInput(attrs = {'class': 'form-control', 'placeholder': 'Enter a date:'}),
                )

    experience = forms.CharField(
                required = True,
                widget = forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Enter experience'}),
                )

    skills = forms.CharField(
                required = False,
                widget = forms.TextInput(attrs = {'class': 'form-control resume', 'placeholder': 'Enter skills attained'}),
                )

    
    class Meta:
        model = Experience
        fields = [
            'company',
            'position',
            'start_date',
            'end_date',
            'experience',
            'skills',
        ]


class EducationForm(forms.ModelForm):


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


    institution = forms.CharField(
                required = True,
                widget =  forms.TextInput(attrs = {'class': 'form-control ', 'placeholder': 'Institution Attended'}),
                )

    qualification = forms.CharField(
                required = True,
                widget = forms.TextInput(attrs = {'class': 'form-control ', 'placeholder': 'Qualification'}),
                )

    level = forms.ChoiceField(
                choices = LEVEL_CHOICES,
                widget = forms.Select(attrs = {'class': 'nice-select rounded'}),
                )

    start_date = forms.DateField(
                required = True,
                widget = DateInput(attrs = {'class': 'form-control', 'placeholder': 'Enter a date'}),
                )

    graduated = forms.DateField(
                required = True,
                widget = DateInput(attrs = {'class': 'form-control', 'placeholder': 'Enter graduation date:'}),
                )

    major_subject = forms.CharField(
                required = False,
                widget = forms.TextInput(attrs = {'class': 'form-control resume', 'placeholder': 'Enter subject majored'}),
                )

    
    
    class Meta:
        model = Education
        fields = [
            'institution',
            'qualification',
            'level',
            'start_date',
            'graduated',
            'major_subject',
            
        ]
