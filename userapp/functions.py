from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template



class ForgotEmail():
    def __init__(self, new_pass):
        self.new_pass = new_pass

    subject = '[FanyaJobs] Forgot your password'

    def email(self):
        return{
            "title": "Your password has been reset",
            "shortDescription": "you have requested a new password",
            "subtitle": "Please find your new password attached for FanyaJobs",
            "message": "your new password us {}. If you did not request this new password, please contact fanyajobs256@gmail.com immediately. Otherwise, kindly login to your profile with your new password and change it online".format(self.new_pass)
        }


class WelcomeEmail():
    subject = '[FanyaJobs] welcome to FanyaJobs'
    email = {
        "title": "Thank you for registering with FanyaJobs",
        "shortDescription": "Welcome to FanyaJobs, Uganda's Leading Job Search Engine. These are the next steps.",
        "subtitle" : "FanyaJobs - Start your job search process today",
        "message": "You have successfully registered with FanyaJobs. You can now login to your profile and start creating a profile. We have thousands of jobs just waiting for you to apply. If you experienceany difficulties with our portal, simply email our support team at fanyajobs256@gmail.com "
    }



def sendEmail(email, subject, to_email):

    from_email = settings.EMAIL_HOST_USER

    text_content = """
    {}
    
    {}
    
    {}
    
    regards,
    FanyaJobs Support
    """.format(email['shortDescription'], email['subtitle'], email['message'])

    html_c = get_template('basic-email.html')
    d = {'email': email}
    html_content = html_c.render(d)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

    # return render(request, 'basic-email.html', {})
      