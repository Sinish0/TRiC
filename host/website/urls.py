from django.urls import path
from model_card import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path("generate_text/", views.generate_text, name="generate_text"),
    path("about/", views.about, name="about")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
