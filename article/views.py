from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from article.models import Article
from article.serializers import ArticleSerializer

# Create your views here.


# Using APIviews
# Function base views @api_view(['reqeuest'])

@api_view(['GET','POST'])
def article_lists(request, format=None):
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def article_details(request, pk, format=None):
    if request.method == 'GET':
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serilizer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_article(request, pk, format=None):
    if request.method == 'PUT':
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serilizer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_article(request, pk, format=None):
    if request.method == 'DELETE':
        article = Article.objects.get(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Using Regular Django Views
# @csrf_exempt
# def article_list(request):
#     if request.method == "GET":
#         serializer = Article.objects.all()
#         serializer = ArticleSerializer(serializer, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExit:
#         return HttpResponse(status=404)
#
#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)
#
#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#     elif request.method == "DELETE":
#         article.delete()
#         return HttpResponse(status=204)
