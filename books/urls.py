from django.urls import path

from books.views import BooksView, BooksDetailView, AddReviewView, EditReviewView

app_name = 'books'
urlpatterns = [
    path('', BooksView.as_view(), name='list'),
    path('<int:id>/', BooksDetailView.as_view(), name='detail'),
    path('<int:id>/reviews/', AddReviewView.as_view(), name='reviews'),
    path('<int:book_id>/reviews/<int:review_id>/edit/', EditReviewView.as_view(), name='edit-review')
]
