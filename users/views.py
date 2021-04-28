from django.views.generic import (
    FormView,
    ListView,
    DetailView,
    View,
)

from django.contrib.auth import get_user_model

from django.urls import reverse_lazy

from users import forms
from photos.models import Photo


class RegisterView(FormView):
    form_class = forms.UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users')

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form=form)

        return response


class UserListView(ListView):
    model = get_user_model()


class UserDetailView(DetailView):
    model = get_user_model()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['photos'] = Photo.objects.filter(user=self.object)

        return context
