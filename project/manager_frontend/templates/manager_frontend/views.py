from django.shortcuts import render
from django.views.generic import TemplateView

# Vue basée sur une fonction
def home_view(request):
    request.breadcrumbs = [
        {"name": "Home", "url": "/"},
    ]
    return render(request, "home.html")

# Vue basée sur une classe
class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        request.breadcrumbs = [
            {"name": "Home", "url": "/"},
            {"name": "Dashboard", "url": "/dashboard/"},
        ]
        return super().get(request, *args, **kwargs)

