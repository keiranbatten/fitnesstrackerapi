from django.conf.urls import url
from MFP import views

urlpatterns = [
    url(r'^api/totals$', views.totals_list),
    url(r'^api/totals/(?P<date>\d{4}-\d{1,2}-\d{1,2})$', views.totals_date),
    url(r'^api/meals/(?P<date>\d{4}-\d{1,2}-\d{1,2})$', views.meals_date)
]