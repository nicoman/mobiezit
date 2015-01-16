from django.contrib import admin
from core.models import Movie, UserMovie, Recommend, Followers

# Register your models here.


# Register the model and the custom admin modification
admin.site.register(Movie)
admin.site.register(UserMovie)
admin.site.register(Recommend)
admin.site.register(Followers)