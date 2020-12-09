from django.contrib import admin

from institute.models import Country, City, State
from  .models import *
# Register your models here.

admin.site.register(Hostel)
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(HostelRoomStudent)
admin.site.register(Designation)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(State)