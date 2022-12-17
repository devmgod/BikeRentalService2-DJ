from django.contrib import admin
from .models import Role, User, Rating, Reservation, Bike

# Register your models here.


admin.site.register(User)
admin.site.register(Role)
admin.site.register(Rating)
admin.site.register(Reservation)
admin.site.register(Bike)
