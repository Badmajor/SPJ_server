from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/user/', include('users.urls', namespace='user')),
    path('v1/customer/', include('customers.urls', namespace='castomer'))
]
