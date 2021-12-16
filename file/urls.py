from django.urls import path

from file.views import AddPhoneView

urlpatterns = [
    path('add/phone/', AddPhoneView.as_view(), name='add-phone'),
    path('view/phones/', AddPhoneView.as_view(), name='view-phones')
]
