from django.contrib  import admin
from .models import Category


@admin.register(Category)

class Category(admin.ModelAdmin):
    list_display =('name', 'is_active' , 'created_at')
    list_filter= ('is_active',) 
    prepopulated_fields={'slug':  ('name', )}
    search_fields= ('name') 
      
    

