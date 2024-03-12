from django.urls import path
from .views import *


urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("polling_result/<int:pu_id>", ResultView.as_view(), name="polling_result"),
    path("polling_result/lga/", LgaPollingView.as_view(), name="polling_by_lga")
]
