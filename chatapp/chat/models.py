from django.core.checks import messages
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_DEFAULT, SET_NULL



class GroupMessage(models.Model):

    sender = models.ForeignKey(User,on_delete=SET_DEFAULT,default='Deleted Account',null=True)
    content = models.TextField('Message Content')
    timestamp = models.DateTimeField('Time Sent',auto_now_add=True)

    def __str__(self):
        return self.sender.username


class ChatGroup(models.Model):

    name = models.CharField('Group Name',max_length=225)
    members = models.ManyToManyField(User,related_name='Members')
    messages = models.ManyToManyField(GroupMessage,verbose_name='Group Messages')
    created_by = models.OneToOneField(User,on_delete=SET_NULL,related_name='Created',null=True)
    date_created = models.DateTimeField('Date Created',auto_now_add=True)
    channel_link = models.CharField('Channel Link',max_length=225,null=True)
    online_members = models.ManyToManyField(User,related_name='Online')

    def __str__(self):
        return self.name

    def get_all_members(self):
        return self.members.all()


class Message(models.Model):

    sender =  models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='sender')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='receiver')
    content = models.TextField('Message Content',null=False,blank=False)
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message Sent From {self.sender} To {self.receiver}'


class DirectMessage(models.Model):
    
    user1 = models.ForeignKey(User,on_delete=SET_NULL,null=True,related_name='User1')
    user2 = models.ForeignKey(User,on_delete=SET_NULL,null=True,related_name='User2')
    messages = models.ManyToManyField(Message,verbose_name='Private Messages')
    lastmsgtimestamp = models.DateTimeField(null=True)
    channel_link = models.CharField('Channel Link',max_length=225,null=True)

    def __str__(self):
        return f'{self.user1.username}/{self.user2.username} Message Box'


class AllChat(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    private_chat = models.ForeignKey(DirectMessage,on_delete=models.CASCADE,null=True,blank=True)
    group_chat = models.ForeignKey(ChatGroup,on_delete=models.CASCADE,null=True,blank=True)
    timestamp = models.DateTimeField('Last Message Timestamp')

    def __str__(self):
        return f'{self.user.username} Chat'