from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('good_detail/<int:good_id>/', views.good_detail, name='good_detail'),
    path('good_list/', views.good_list, name='good_list'),
    path('review_detail/<int:review_id>/', views.review_detail, name='review_detail'),
    path('review_list/', views.review_list, name='review_list'),
    path('good_review_list/<int:good_id>/', views.good_review_list, name='good_review_list'),
    path('add_good/', views.add_good, name='add_good'),
    path('edit_good/<int:good_id>/', views.edit_good, name='edit_good'),
    path("register_user/", views.register_user, name="register_user"),
    path("login_user/", views.login_user, name="login_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path('add_review/<int:good_id>/', views.add_review, name='add_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),

]