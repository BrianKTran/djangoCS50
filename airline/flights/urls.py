from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns =[
    # url(r'^$', views.index, name='index'),
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book")
]
