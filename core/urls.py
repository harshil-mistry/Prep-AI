from django.urls import path
from . import views
from . import auth_views
from .auth_views import SignUpView, CustomLoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('quick-login/', auth_views.quick_login, name='quick_login'),
    path('logout/', auth_views.logout_view, name='logout'),
    path('chat/', views.chatbot_view, name='chat'),
    path('chat/<uuid:chat_id>/', views.chatbot_view, name='chat'),
    path('create_chat/', views.create_chat, name='create_chat'),
    path('delete_chat/<uuid:chat_id>/', views.delete_chat, name='delete_chat'),
    path('download_message_pdf/<int:message_id>/', views.download_message_pdf, name='download_message_pdf'),
]
