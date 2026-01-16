from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100  , unique=True)
    slug =models.SlugField(max_length=120 , unique= True, blank=True)
    is_active =models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)
    Update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering =['name'],
        verbose_name_plural ='categories'
        
        def save(self, *args, **kwargs):
            if not self: 
                self.slug = slugify (self.name)
                super().save( *args, **kwargs)
                
    def __str__(self):
        return self.name            