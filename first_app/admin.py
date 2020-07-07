from django.contrib import admin
# from first_app.models import AccessRecord,Topic,WebPage
# Register your models here.
# admin.site.register(AccessRecord)
# admin.site.register(Topic)
# admin.site.register(WebPage)

from first_app.models import Profile,App_Profile,MyWishList

admin.site.register(Profile)
admin.site.register(App_Profile)
admin.site.register(MyWishList)
# wrong
# from first_app.models import Profile
#
# admin.site.register(Profile)
