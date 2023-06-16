from django.contrib import admin

from .models import Bid, Location, Unit, Device, Status, Worker, Level, Control

class ControlInLine(admin.StackedInline):
    model = Control
    extra = 1

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('pk','status','pub_date','device','text', 'user')
    search_fields = ('text',)
    list_editable = ('device',)
    list_filter = ('pub_date', 'status',)
    empty_value_display = '-пусто-' 
    inlines = [ControlInLine]
    fields = [('user','device'),'text', 'image','status']


@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
    list_display = ('pk', 'bid','worker', 'level', 'date', 'note')
    search_fields = ('bid',)
    list_editable = ('worker',)
    list_filter = ('date',)
    empty_value_display = '-пусто-'
    fields = ['bid', ('worker', 'level'), 'note']

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'last_name','name', 'fathers_name', 'dob')
    search_fields = ('last_name',)

admin.site.register(Location)
admin.site.register(Unit)
admin.site.register(Device)

admin.site.register(Status)
admin.site.register(Level)
