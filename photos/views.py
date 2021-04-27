from django.shortcuts import redirect
from django.views.generic import FormView, DetailView


from photos import (
    forms,
    models,
)


class PhotoUploadFormView(FormView):
    form_class = forms.PhotoUploadForm
    template_name = 'photos/upload.html'

    def form_valid(self, form):
        photo = form.save()

        return redirect(
            to='photo-detail',
            pk=photo.id,
        )


class PhotoDetailView(DetailView):
    model = models.Photo
