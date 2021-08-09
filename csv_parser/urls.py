from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from service_app.views import ListCSVFileView

router = SimpleRouter()
router.register(r'api/objects', ListCSVFileView, basename='objects')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('service_app.urls')),
]

urlpatterns += router.urls
