
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # our url routing for the api 
    path('api/', include('base.api.urls')),
]
