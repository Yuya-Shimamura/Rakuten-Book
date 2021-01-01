from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SearchForm

# Create your views here.
class Index(TemplateView):
    def get(sef, request, *args, **kwargs):
        form = SearchForm(request.POST or None)
        return render(request, 'app/index.html', {
            'form': form
        })
