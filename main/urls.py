from django.urls import path

from main.views import CountryView

urlpatterns = [
    path('country/', CountryView.as_view())
]