from django.contrib import admin
from .models import MovieUser, Movie, CheckoutDB


admin.site.register(MovieUser)
admin.site.register(Movie)
admin.site.register(CheckoutDB)