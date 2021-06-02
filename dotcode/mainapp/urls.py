from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('log',views.main),
    
    # path('admin/', admin.site.urls),
]
