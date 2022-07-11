from datetime import datetime
import os
from PIL import Image
from django.conf import settings
from django.shortcuts import render
from .forms import LandLordForm, UploadForm,TenantForm
# Create your views here.
def homepage(request):
    return render(request,'base.html')

def sign_up(request):
    if request.method=='POST':
        form=LandLordForm(request.POST)
        p_pic=request.FILES['prof_pic']
    else:
        form=LandLordForm()
    return render(request,'media_app/sign_up.html',{'form':form})

def upload_file(request):
    if request.method=='POST':
        save_path=os.path.join(settings.MEDIA_ROOT, request.FILES['user-file'].name)
        with open(save_path,'wb') as output_file:
            for chunk in request.FILES['user-file'].chunks():
                output_file.write(chunk)
    return render(request,'media_app/upload_file.html')

def form_uploads(request):
    if request.method=='POST':
        form=UploadForm(request.POST, request.FILES)
        file_name=datetime.now().strftime('%Y%M%d%H%M%S')+'_'+str(request.FILES['user_file'].size)+'.'\
            +str(request.FILES['user_file'].name).split('.')[-1]
        save_path=os.path.join(settings.MEDIA_ROOT,file_name)
        if form.is_valid():
            image=Image.open(form.cleaned_data['user_file'])
            image.thumbnail((50,50))
            image.save(save_path)
    else:
        form=UploadForm()
    return render(request,'media_app/form_upload.html',{'form':form})

def tenant_upload(request):
    if request.method=="POST":
        form=TenantForm(request.POST,request.FILES)
        if form.is_valid():
            form.profile_pic=form.cleaned_data['profile_pic']
            form.save()
    else:
        form=TenantForm()
    return render(request,'media_app/tenant_upload.html',{'form':form})