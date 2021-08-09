from django.urls import path
from .views import UploadCSVFileView

app_name = 'service_app'
urlpatterns = [
    path('upload_csv_file/', UploadCSVFileView.as_view(), name='upload_csv_file'),
]
