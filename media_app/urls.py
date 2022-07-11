from django.urls import path
from .views import form_uploads, homepage,sign_up,upload_file
urlpatterns = [
    path('',homepage),
    path('sign_up/',sign_up),
    path('upload/', upload_file),
    path('form_upload/',form_uploads)
]