from django.contrib import admin

# Register your models here.
from .models import MovieModel

# Register your models here.
@admin.register(MovieModel)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
# Register your models here.