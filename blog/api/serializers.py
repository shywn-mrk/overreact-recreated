from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'summary', 'date', 'reading_time', 'description']
        