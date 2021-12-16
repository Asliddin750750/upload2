from django.urls import path

from upload.views import UploadFileView, FilesView, FileResponseView

urlpatterns = [
    path('file/', UploadFileView.as_view(), name='upload-file'),
    path('view/', FilesView.as_view(), name='upload-view'),
    path('file/download/', FileResponseView.as_view(), name='file-download')
]
