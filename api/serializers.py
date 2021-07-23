from rest_framework import serializers
from .models import Article

# basic serializers
# this is like models

# class ArticleSerializer(serializers.Serializer):
# 	title = models.CharField(max_length=200, blank=True)
# 	author = models.CharField(max_length=200, blank=True)
# 	email = models.EmailField(max_length=200, blank=True)
# 	date = models.DateTimeField()

# 	def create(self, validated_data):
# 		return Article.objects.create(validated_data)

# 	def update(self, instance, validated_data):
# 		instance.title = validated_data.get('title', instance.title)
# 		instance.author = validated_data.get('author', instance.author)
# 		instance.email = validated_data.get('email', instance.email)
# 		instance.date = validated_data.get('date', instance.date)
# 		instance.save()
# 		return instance

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = "__all__"