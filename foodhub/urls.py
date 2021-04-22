from django.urls import path
from.import views


urlpatterns = [
    path('',views.index,name="home"),
    path("signup",views.signup,name="signup"),
    path("login",views.loginUser,name="login"),
    path("logout",views.logoutUser,name="logout"),
    # path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    # path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    # path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    # path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    # path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    # path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]
