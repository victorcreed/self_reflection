from django.contrib import admin
from django.urls import path, include
from journal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('journal.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
