from django.urls import path
from wiki.views import PageListView, PageDetailView, PageAddView


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
    path('page/add/', PageAddView.as_view(), name='wiki-add-page')
]
