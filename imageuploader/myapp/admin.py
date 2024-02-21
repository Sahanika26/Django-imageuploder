from django.contrib import admin
from .models import Image,Contact

# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display=['id','photo','date']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','message']