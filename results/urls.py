from django.urls import path
from . import views
from .views import polling_unit_result

urlpatterns = [
    # path('', views.index, name= "index"),
    path('', views.polling_unit_result, name='polling_unit_result'),
    path('<result_id>', views.detail, name='results_detail'),
]