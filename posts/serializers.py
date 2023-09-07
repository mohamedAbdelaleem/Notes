from datetime import datetime
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'description', 'img', 'date']
        extra_kwargs = {
            'date': {'read_only': True},
        }


