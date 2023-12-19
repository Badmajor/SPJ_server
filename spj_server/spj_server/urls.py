from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from customers.views import CustomerViewSet, TaskViewSet, VacancyViewSet
from users.views import UserViewSet

route_with_view = (
    (r'users', UserViewSet),
    (r'customers', CustomerViewSet),
    (r'tasks', TaskViewSet),
    (r'vakancies', VacancyViewSet),
)

router_v1 = DefaultRouter()
for i in route_with_view:
    router_v1.register(*i)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router_v1.urls))
]
