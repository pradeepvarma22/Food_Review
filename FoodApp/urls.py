from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from FoodApp.views import Home



urlpatterns=[
    path('',Home,name='home')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)