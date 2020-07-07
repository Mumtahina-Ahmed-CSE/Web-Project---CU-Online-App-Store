from django.urls import path
from first_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.index,name="index"),
    path('create/',views.create,name='create'),
    # path('dashboard/',views.dashboard,name="dashboard"),
    path('dashboard/<email>',views.dashboard,name="dashboard"),
    # path('myprofile/',views.myprofile,name="myprofile"),
    path('myprofile/<email>',views.myprofile,name="myprofile"),
    # path('upload/',views.upload,name="upload"),
    path('upload/<email>',views.upload,name="upload"),
    path('delete/<app_name>',views.delete,name="delete"),
    # path('wishlist/',views.wishlist,name="wishlist"),
    path('wishlist/<email>',views.wishlist,name="wishlist"),
    path('addtowishlist/<email>/<app_name>',views.addtowishlist,name="addtowishlist"),
    path('auth/',views.auth,name='auth'),
    # path('success/',views.success,name='success'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name="signup"),
    path('viewapp/<email>/<app_name>',views.viewapp,name="viewapp"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # path('',views.index,name='dashboard'),
    # path('',views.myprofile,name='myprofile'),
    # path('',views.upload,name='upload'),
    # path('dashboard/',include('first_app.urls')),
