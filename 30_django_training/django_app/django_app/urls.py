
from django.urls import path, re_path
from response_main import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index),
    path('about/', TemplateView.as_view(template_name="about.html",
                                        extra_context={"header": "О сайте"})),
    path('extended/', TemplateView.as_view(template_name="extended.html")),
    path('contact/', TemplateView.as_view(template_name="contact.html")),
    path('details/', views.details),
    path('dates/', TemplateView.as_view(template_name="format_dates.html")),
    path('context/', TemplateView.as_view(template_name="format_context.html")),
    path('cnds/', views.conditions),
    path('iters/', views.iterators),
    path('forms/', views.user_form),
]
