from django.contrib import admin
from blog.models import Post,BlogComment,Paint
# Register your models here.

# Registering Post model here

admin.site.register((Post,BlogComment,Paint))