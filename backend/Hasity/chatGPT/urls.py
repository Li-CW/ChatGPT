from django.urls import path, re_path
from chatGPT.views import ChatView

urlpatterns = [
    path("", ChatView.as_view(), name="ChatView"),
]

