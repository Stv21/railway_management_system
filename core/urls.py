# core/urls.py
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name="home"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('Electronics/', views.Electronics, name='Electronics'),
    path('Fashion/', views.Fashion, name='Fashion'),
    path('Sports/', views.Sports, name='Sports'),
    path('signup/', views.signup, name='signup'),
    path('book_ticket/', views.book_ticket, name='book_ticket'),  # Add this line for booking ticket
    path('train_details/', views.train_details, name='train_details'),

    path('ticket_confirmation/', views.ticket_confirmation, name='ticket_confirmation'),
    #path('my_tickets/', views.my_tickets, name='my_tickets'),
    #path('my_tickets/', views.view_tickets, name='my_tickets')
    
]
