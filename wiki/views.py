from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy

from wiki.models import Page
from wiki.forms import PageForm

class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })

class PageAddView(CreateView):
    """"""
    model = Page
    form_class = PageForm
    template_name = 'add.html'

    def post(self, request):
        form = PageForm(request.POST)
        form.instance.author = self.request.user
        if form.is_valid():
            page = form.save(commit=False)
            return redirect('wiki-details-page', slug=page.slug)
