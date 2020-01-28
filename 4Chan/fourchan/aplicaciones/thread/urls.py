from .views import ThreadView, CategoryView, FilterView
from django.urls import path

urlpatterns = [
	path('', ThreadView.as_view(), name='thread'),
	path('category/', CategoryView.as_view(), name='categoria'),
]
