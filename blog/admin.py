from django.contrib import admin
from blog.models import PostModel

# Register your models here.

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','created_date','modified_date','published_date','is_published']
