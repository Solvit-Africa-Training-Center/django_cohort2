from django.contrib import admin
from django.urls import path, include  # <-- correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),  # include your accounts URLs
] 
