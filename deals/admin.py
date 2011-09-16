from django.contrib import admin
from testdeals.deals.models import Deal

class DealAdmin(admin.ModelAdmin):
	fields=('title', 'price', 'description', 'url', 'date',) 

admin.site.register(Deal)
