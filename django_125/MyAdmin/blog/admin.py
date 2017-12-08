from django.contrib import admin
from .models import BlogArticle,BlogPerson,SfhdPredictDataTest
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(BlogArticle)
# admin.site.register(Article_2,ArticleAdmin_2)
admin.site.register(BlogPerson)
admin.site.register(SfhdPredictDataTest)