from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    # Основные URL
    path('', views.GameListView.as_view(), name='game_list'),
    path('genre/<slug:genre_slug>/', views.GameListView.as_view(), name='game_list_by_genre'),
    path('game/<int:pk>/<slug:slug>/', views.GameDetailView.as_view(), name='game_detail'),

    # Корзина
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:game_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:game_id>/', views.cart_remove, name='cart_remove'),
    path('cart/update/<int:game_id>/', views.cart_update, name='cart_update'),

    # Избранное
    path('game/<int:pk>/<slug:slug>/', views.GameDetailView.as_view(), name='game_detail'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/add/<int:game_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:game_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    # Заказы
    path('order/create/', views.order_create, name='order_create'),

    # API
    path('api/games/', views.api_games, name='api_games'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]