from django.contrib import admin
from RMB.models import UserProfile,Comments,Images,Likes,Categories

# Register our models into admin.
admin.site.register(UserProfile)
admin.site.register(Categories)
admin.site.register(Images)
admin.site.register(Likes)
admin.site.register(Comments)