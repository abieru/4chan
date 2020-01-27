from .views import ThreadView
from django.urls import path

urlpatterns = [
	path('', ThreadView.as_view(), name='thread'),
]
