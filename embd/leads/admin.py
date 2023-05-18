from django.contrib import admin

# Register your models here.
from .models import Lead,Resource,User,Upcoming_Lead,LeadAction
admin.site.register(Lead)
admin.site.register(Resource)
admin.site.register(User)
admin.site.register(Upcoming_Lead)
admin.site.register(LeadAction)
