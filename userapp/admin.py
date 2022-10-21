from django.contrib import admin

# Register your models here.

from .models import Resume, Education, Experience, User

admin.site.register(User)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Resume)