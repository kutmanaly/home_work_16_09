from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from review.models import Review


from review.serializers import ReviewListSerializer, ReviewDetailSerializer


class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer


class ReviewDetailView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer


class CreateReviewView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer


class UpdateReviewView(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer


class DeleteReviewView(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
