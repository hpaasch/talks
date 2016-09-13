from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class PrepareView(TemplateView):
    template_name = 'prepare.html'


class FederalView(TemplateView):
    template_name = 'federal.html'


class StateView(TemplateView):
    template_name = 'state.html'


class ResourceView(TemplateView):
    template_name = 'resource.html'
