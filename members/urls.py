from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_submit, name='form_submit'),
    # path('search.html',views.search,name='search')
]