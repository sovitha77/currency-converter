from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("create/", views.create_conversion),
    path("all/", views.get_all_conversion),
    path("<int:id>/", views.get_single_conversion),
    path("update/<int:id>/", views.update_conversion),
    path("delete/<int:id>/", views.delete_conversion),
]
