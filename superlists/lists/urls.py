from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path(r"lists/new",
         views.new_list, name="new_list"),
    path(r"lists/the-only-list-in-the-world/",
         views.view_list, name="view_list")

]
# TODO:
#   add unique URLs for each lists
#   add URLs for adding a new item to an existing list via POST
