from django.contrib import admin
from .models import *


admin.site.register(Booking)
admin.site.register(Ticket)
admin.site.register(Ticket_flight)
admin.site.register(Boarding_passes)
admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(Seats)

