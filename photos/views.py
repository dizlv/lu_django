from django.shortcuts import render
from django.http import HttpResponse

from photos import (
    forms,
    models,
)


def upload_photo(request):
    if request.method == 'POST':
        form = forms.PhotoUploadForm(
            data=request.POST,
            files=request.FILES,
        )

        if form.is_valid():
            form.save()

            return HttpResponse('File uploaded')

    else:
        form = forms.PhotoUploadForm()

    return render(
        request=request,
        template_name='photos/upload.html',

        context={
            'form': form,
        }
    )


def view_photo(request, photo_id):
    photo = models.Photo.objects.filter(id=photo_id)

    return HttpResponse(f'Picture path: {photo.picture}')
