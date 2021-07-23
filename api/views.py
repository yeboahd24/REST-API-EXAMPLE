from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication\
, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#functional base view

@csrf_exempt
def list_article(request):
	if request.method == 'GET':
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ArticleSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		else:
			return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def article_detail(request, pk):
	try:
		articles = Article.objects.get(pk=pk)
	except Article.DoesNotExist:
		raise HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ArticleSerializer(articles)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ArticleSerializer(articles, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		else:
			return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		articles.delete()
		return HttpResponse(status=204)




# api_view

@api_view(['GET', 'POST'])
def list_article_2(request):
	if request.method == 'GET':
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ArticleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['PUT', 'DELETE', 'GET'])
def article_detail_2(request, pk):
	try:
		articles = Article.objects.get(pk=pk)
	except Article.DoesNotExist:
		raise HttpResponse(status=status.HTTP_400_NOT_FOUND)

	if request.method == 'GET':
		serializer = ArticleSerializer(articles)
		return Response(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ArticleSerializer(articles, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		articles.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



# class base view

class ArticleAPIView(APIView):
	def get(self, request):
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)

	def post(self, request):
		data = JSONParser().parse(request)
		serializer = ArticleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
	def get_object(self, id):
		try:
			return Article.objects.get(id=id)
		except Article.DoesNotExist:
			raise HttpResponse(status=status.HTTP_400_NOT_FOUND)

	def get(self, request, id):
		articles = self.get_object(id)
		serializer = ArticleSerializer(articles)
		return Response(serializer.data)

	def put(self, request, id):
		articles = self.get_object(id)
		serializer = ArticleSerializer(articles, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def delete(self, request, id):
		articles = self.get_object(id)
		articles.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



# generic view
class ArticleGenericAPIView(generics.GenericAPIView\
	, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,\
	mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
	serializer_class = ArticleSerializer
	queryset = Article.objects.all()
	lookup_field = 'id'
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	# authentication_classes = [TokenAuthentication]
	permissions_classes = [IsAuthenticated]

	def get(self, request, id=None):
		if id:
			return self.retrieve(request)
		else:
			return self.list(request)

	def post(self, request):
		return self.create(request)


	def put(self, request, id=None):
		return self.update(request, id)

	def delete(self, request, id):
		return self.destroy(request, id)




# class DetailArticle(generics.RetrieveAPIView):
# 	queryset = Article.objects.all()
# 	serializer_class = ArticleSerializer

class DetailArticle(generics.RetrieveUpdateDestroyAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer


class ListArticle(generics.ListCreateAPIView):
	permissions_classes = [IsAuthenticated]
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer