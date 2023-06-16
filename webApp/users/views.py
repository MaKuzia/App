from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('bid:index') #куда отправить после успешной регистрации
    template_name = 'users/signup.html'
