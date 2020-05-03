from django.contrib import admin
# from apiDatabase.models import City, Languages, AccessCounts
# from apiDatabase.models import Topic, Webpage, AccessRecords
from apiDatabase.models import City, Languages

# Register your models here.
admin.site.register(City)
admin.site.register(Languages)
# admin.site.register(AccessCounts)

# admin.site.register(Topic)
# admin.site.register(Webpage)
# admin.site.register(AccessRecords)