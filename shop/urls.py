from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('newpurchase/', views.newpurchase, name='newpurchase' ),
    path('<int:id>/<slug:slug>/', views.purchase_detail, name='detail'),
]