from django.urls import path
from . import views
from .views import polling_unit_result

urlpatterns = [
    # path('', views.index, name= "index"),
    path('', polling_unit_result, name='polling_unit_result'),
    path('polling_unit_result/', polling_unit_result, name='polling_unit_result'),
]