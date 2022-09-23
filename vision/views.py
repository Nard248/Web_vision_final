from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
from .script_1 import detect_text_my
from Web_vision_final.settings import MEDIA_ROOT


# Create your views here.
def image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('processed')
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})


def success_view(request):
    return HttpResponse('Successfully Uploaded')


def process_view(request):
    image = Image.objects.all().last()
    path = detect_text_my(word=image.search_word, path=f'{MEDIA_ROOT}/{image.image}', name=str(image.id))
    return render(request, 'image_view.html', {'path': path})
