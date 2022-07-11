from django.urls import path
from .views import form_uploads, homepage,sign_up,upload_file,tenant_upload
urlpatterns = [
    path('',homepage),
    path('sign_up/',sign_up),
    path('upload/', upload_file),
    path('form_upload/',form_uploads),
    path('tenant_upload/',tenant_upload)
]