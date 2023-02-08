from django.contrib import admin

from app.models import *

# Register your models here.
admin.site.register(Services)




class PlanAdmin(admin.ModelAdmin):
    list_display = ('name','maxprice','price')
admin.site.register(Plan,PlanAdmin)


class PlanDetailAdmin(admin.ModelAdmin):
    list_display = ('id','plan','detail')
admin.site.register(PlanDetail,PlanDetailAdmin)

admin.site.register(ContactDetail)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name','desc')

admin.site.register(Review,ReviewAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('plan','name','mobile','desc')

admin.site.register(Booking,BookingAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','message')

admin.site.register(Message,MessageAdmin)

