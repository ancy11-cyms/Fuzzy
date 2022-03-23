from django.contrib import admin
from .models import category
from .models import skill
from .models import company
from .models import HR
from .models import user
from .models import FeedBack

# Register your models here.
admin.site.register(category)
admin.site.register(skill)
admin.site.register(company)
admin.site.register(HR)
admin.site.register(user)
admin.site.register(FeedBack)

