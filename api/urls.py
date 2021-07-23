from django.urls import path
from .views import list_article, article_detail, list_article_2,\
 article_detail_2, ArticleAPIView, ArticleDetail, ArticleGenericAPIView,\
 DetailArticle, ListArticle

urlpatterns = [
	path('', list_article),
	path('list/', list_article_2, name='list'),
	path('detail/<int:pk>/', article_detail, name='detail'),
	path('detail_2/<int:pk>/', article_detail_2, name='detail_2'),
	# class base view
	path('cbv/', ArticleAPIView.as_view(), name='cbv'),
	path('cbv/<int:id>/', ArticleDetail.as_view(), name='cbv_detail'),
	# generic view
	path('generic/', ArticleGenericAPIView.as_view(), name='generic_view'),
	path('generic/<int:id>/', ArticleGenericAPIView.as_view(), name='generic_view'),
	path('generic/details/<int:pk>/', DetailArticle.as_view()),
	path('generic/list/', ListArticle.as_view())
]	

# //127.0.0.1:8000/api/v1/dj-rest-auth/logout/.
# //127.0.0.1:8000/api/v1/dj-rest-auth/login/.
# //127.0.0.1:8000/api/v1/dj-rest-auth/password/reset
# //127.0.0.1:8000/api/v1/dj-rest-auth/password/reset/confirm
