from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest
from interface.interface import AIInterface


class HomePage(TemplateView):
    template_name = "base.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        # query_params = request.GET
        # print(query_params)

        # ai_interface = AIInterface()
        # ai_interface.process_data(query_params)

        return super().get(request, *args, **kwargs)
