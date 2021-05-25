from django.contrib import admin
from .models import ChatGroup,GroupMessage,Message,DirectMessage,AllChat


admin.site.register(ChatGroup)
admin.site.register(GroupMessage)
admin.site.register(Message)
admin.site.register(DirectMessage)
admin.site.register(AllChat)
