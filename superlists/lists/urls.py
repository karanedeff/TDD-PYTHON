from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name="home")
]
# TODO:
#   add unique URLs for each lists
#   add URL for creating new list via POST
#   add URLs for adding a new item to an existing list via POST
