from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . import models

class home(ListView):
    model = models.Produto
    template_name = 'home.html'
    context_object_name = 'produtos'

class produtoDetalhe(DetailView):
    model = models.Produto
    template_name = 'detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'
