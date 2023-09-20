from datetime import datetime
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post_type = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'description', 'img', 'date', 'post_type', 'post_type_val']
        extra_kwargs = {
            'date': {'read_only': True},
            'post_type_val': {'source': 'post_type', 'write_only': True}
        }

    
    def get_post_type(self, obj):
        
        post_type = obj.post_type
        return {'value': post_type,'label': post_type}

