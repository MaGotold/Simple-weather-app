from django.urls import path
from . import views
from weather.views import DaysView

urlpatterns = [
    path("", views.call_api),
    path("days",DaysView.as_view(), name="days")
]
