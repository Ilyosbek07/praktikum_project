from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from api.serializers import BookReviewSerializer
from books.models import Review


class BookReviewListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookReviewSerializer
    queryset = Review.objects.all().order_by('-created_at')
    # def get(self, request):
    #     book_reviews = Review.objects.all().order_by('-created_at')

    # paginator = PageNumberPagination()
    # page_object = paginator.paginate_queryset(book_reviews, request)

    # serializer = BookReviewSerializer(page_object, many=True)

    # return paginator.get_paginated_response(serializer.data)
    #
    # def post(self, request):
    #     serializer = BookReviewSerializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
#
class BookReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookReviewSerializer
    queryset = Review.objects.all()
    lookup_field = 'id'

    # def get(self, request, id):
    #     book_review = Review.objects.get(id=id)
    #     serializer = BookReviewSerializer(book_review)
    #     return Response(serializer.data)
    #
    # def delete(self, request, id):
    #     book_review = Review.objects.get(id=id)
    #     book_review.delete()
    #
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #
    # def put(self, request, id):
    #     book_review = Review.objects.get(id=id)
    #     serializes = BookReviewSerializer(instance=book_review, data=request.data)
    #
    #     if serializes.is_valid():
    #         serializes.save()
    #         return Response(data=serializes.data, status=status.HTTP_200_OK)
    #
    #     return Response(data=serializes.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def patch(self, request, id):
    #     book_review = Review.objects.get(id=id)
    #     serializes = BookReviewSerializer(instance=book_review, data=request.data, partial=True)
    #
    #     if serializes.is_valid():
    #         serializes.save()
    #         return Response(data=serializes.data, status=status.HTTP_206_PARTIAL_CONTENT)
    #
    #     return Response(data=serializes.errors, status=status.HTTP_400_BAD_REQUEST)
