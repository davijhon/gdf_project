from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class TestView(LoginRequiredMixin, TemplateView):
   template_name = 'index_test.html'
