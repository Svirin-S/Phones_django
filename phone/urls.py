
from django.contrib import admin
from django.urls import path
import app.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.index),
    path('catalog/', app.views.show_catalog, name='catalog'),
    path('catalog/<slug:slug>/', app.views.show_product, name='phone'),
    
]

