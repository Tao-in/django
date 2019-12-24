from django.contrib import admin
from book.models import BookInfo,HeroInfo

# Register your models here.
admin.site.register(BookInfo)
admin.site.register(HeroInfo)