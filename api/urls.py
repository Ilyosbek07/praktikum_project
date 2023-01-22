from django.urls import path

from api.views import BookReviewListAPIView, BookReviewDetailView

app_name = 'api'
urlpatterns = [
    path('reviews/', BookReviewListAPIView.as_view(), name='review-list'),
    path('reviews/<int:id>/', BookReviewDetailView.as_view(), name='review-detail')
]
