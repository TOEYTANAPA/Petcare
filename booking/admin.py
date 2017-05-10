from django.contrib import admin
from booking.models import Car1,Car2,Booking


# Register your models here.
class Car1Admin(admin.ModelAdmin):
	list_display=[f.name for f in Car1._meta.fields]

admin.site.register(Car1,Car1Admin)


class Car2Admin(admin.ModelAdmin):
	list_display=[f.name for f in Car2._meta.fields]

admin.site.register(Car2,Car2Admin)

class BookingAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Booking._meta.fields]

admin.site.register(Booking,BookingAdmin)