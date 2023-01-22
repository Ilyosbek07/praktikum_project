from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from books.forms import BookReviewForm
from books.models import Book, Review


def landing_page(request):
    return render(request, 'landing.html')


class BooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        paginator = Paginator(books, 2)
        search_query = request.GET.get('q', '')
        if search_query:
            books = books.filter(title__icontains=search_query)
        page_num = request.GET.get('page', 1)
        page_object = paginator.get_page(page_num)
        return render(request, 'books/list.html', {"page_object": page_object, 'books': books})


# class BooksView(ListView):
#     template_name = 'books/list.html'
#     queryset = Book.objects.all()
#     context_object_name = 'book'


# class BooksDetailView(DetailView):
#     model = Book
#     template_name = 'books/detail.html'
#     pk_url_kwarg = 'id'

class BooksDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm()

        return render(request, 'books/detail.html', {'book': book, 'review_form': review_form})


class AddReviewView(View):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm(data=request.POST)

        if review_form.is_valid():
            Review.objects.create(
                user=request.user,
                book=book,
                stars_given=review_form.cleaned_data['stars_given'],
                comment=review_form.cleaned_data['comment']
            )
            return redirect(reverse('books:detail', kwargs={'id': book.id}))
        return render(request, 'books/detail.html', {'book': book, 'review_form': request})


class EditReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.bookreview_set.get(id=review_id)
        review_form = BookReviewForm(instance=review)
        return render(request, '', {'book': book, 'review': review, 'review_form': review_form})
