# JobPortal Web Application

## About the project
This is a project about a Job Portal where Employers can create accounts and post jobs that are then accessed by job seekers who have logged into the system. The job seekers can also create resumes that are visible only to them selves and potential employers.

## Dependencies
To install the dependencies on your machine run the following command in your terminal: pip install -r requirements
these are available in the requirements.txt file

## Migrate to the database
To migrate your models to the database. run the command: py manage.py makemigrations
follow this command with: py manage.py migrate

## For admin privileges
To access the django admin panel you'll have to create a superuser. run the command: py manage.py createsuperuser "enter the name of your admin here without the quotes"
and follow the steps that are hence required.

## File structure
To view the detailed file structure go to the test.txt file
For a breif summary FanyaJobs is the project folder and there are two apps: Jobapp and Userapp.

Folder PATH listing
|   all.py
|   db.sqlite3
|   manage.py
|   requirements.txt
|   TERMS AND CONDITIONS.docx
|   test.py
|   test.txt            
+---FanyaJobs
|   |   settings.py
|   |   testing.py
|   |   urls.py
|   |   wsgi.py
|   |   __init__.py
+---jobapp
+---static
+---userapp
    
 
