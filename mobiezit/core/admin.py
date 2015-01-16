from django.contrib import admin
from core.models import Movie, UserMovie

# Register your models here.


# Register the model and the custom admin modification
admin.site.register(Movie)
admin.site.register(UserMovie)