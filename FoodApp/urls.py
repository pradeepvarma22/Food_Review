from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from FoodApp.views import Home,createReview,LogOut,LogIn,register,AllReviews

from django.views.static import serve
from django.conf.urls.static import url,static


urlpatterns=[
    path('',Home,name='home'),
   path('create/<str:pk>/',createReview,name='review'),
   path('login/',LogIn,name='login'),
   path('logout/',LogOut,name='logout'),
   path('register/',register,name='register'),
   path('allreviews/',AllReviews,name='allreviews'),


    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)