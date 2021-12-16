from django.urls import path

from file3.views import NotebookView

urlpatterns = [
    path('upload/image/', NotebookView.as_view(), name='upload-image')
]
