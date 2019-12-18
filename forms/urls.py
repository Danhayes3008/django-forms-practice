from django.conf.urls import url, include
from .views import home, addProfile

urlpatterns = [
    url(r'^$/', home, name="home"),
    url(r'^addProfile/', addProfile, name="addProfile"),
]
