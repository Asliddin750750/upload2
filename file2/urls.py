from django.urls import path

from file2.views import AddPhoneView2, GetImageView

urlpatterns = [
    path('add/phone/', AddPhoneView2.as_view(), name='add-phone'),
    path('view/phones/', AddPhoneView2.as_view(), name='view-phones'),
    path('get/image/', GetImageView.as_view(), name='get-image')
]
