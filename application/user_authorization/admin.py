from django.contrib import admin
from .models import registrations
from .models import login
from .models import resumedata


# Register your models here.
admin.site.register(registrations)
admin.site.register(login)
admin.site.register(resumedata)

