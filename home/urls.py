from django.urls import path
from.import views

app_name='home'
urlpatterns=[
    path('', views.home, name='home'),
    path('products/' , views.all_products, name='products'),
    path('ozviat/' , views.ozviat_user, name='ozviat'),
]