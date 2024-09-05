from django.contrib import admin

# Register your models here.


# import a model 
# . - orders to find models.py in admin.py
from .models import Topic, Entry

# orders Django to let those models manage the admin web
admin.site.register(Topic)
admin.site.register(Entry)