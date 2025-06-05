from django.contrib import admin
from .models import Chat, Message

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('title', 'exam_name', 'user', 'created_at', 'updated_at')
    list_filter = ('exam_name', 'created_at', 'user')
    search_fields = ('title', 'exam_name', 'exam_details')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat', 'sender', 'text', 'created_at')
    list_filter = ('sender', 'created_at', 'chat')
    search_fields = ('text', 'chat__title')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
