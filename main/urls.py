from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('cart', views.cart, name='cart'),
    path('catalog', views.categories, name='catalog'),
    path('checkout', views.checkout, name='checkout'),
    path('auth', views.auth, name='auth'),
    path('create_card/', views.create_card),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('catalog/<int:pk>', views.XarakteristikiDetailView.as_view(), name='xaraketistiki')

]