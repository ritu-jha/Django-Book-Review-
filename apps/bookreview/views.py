from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from apps.bookreview.models import User, Review, Book
from django.utils import timezone
from datetime import datetime

def index(request):
	print request.GET
	print request.method
	return render(request, 'bookreview/index.html')

def register(request):
	print "Registration"
	user = User.objects.filter(email= request.POST.get('email'), password=request.POST.get('password'))
	if len(user) > 0 and len(request.POST.get('email'))<3:
		return redirect('/')
	else:
		user = User()
		user.first_name = request.POST.get('first_name')
		user.last_name = request.POST.get('last_name')
		user.email = request.POST.get('email')
		user.description = request.POST.get('description')
		user.password = request.POST.get('password')
		user.created_at = timezone.now()
		user.save()
		print "Successful Registration"
		print user.first_name
		print user.last_name
		print user.email
		print user.password
		return redirect('/')

def login(request):
	print "Login"
	print request.POST.get('email')
	print request.POST.get('password')
	user = User.objects.filter(email=request.POST.get('email'))
	if len(user)<1:
		print "Failed"
		return redirect('/')
	else:
		print "Success"
		request.session['user_id'] = user[0].id
		print "Logging In.."
		return redirect('/dashboard')

def dashboard(request):
	print "User Dashboard"
	if "user_id" in request.session:
		user = User.objects.get(id=request.session['user_id'])
		current_user = User.objects.get(id=request.session['user_id'])
		reviews = Review.objects.all()
		context = {
			'current_user': current_user,
			'user': user,
			'reviews': reviews,
		}
		return render(request, 'bookreview/dashboard.html', context)
	else:
		del request.session
		return redirect('/')

def add(request):
	return render(request, 'bookreview/add.html')

def add_review(request):
	book = Book()
	review = Review()
	book.title = request.POST.get('title')
	book.author = request.POST.get('author')
	book.created_at = timezone.now()
	book.save()
	print book.author
	review.user = User.objects.get(id=request.session['user_id'])
	review.book = book
	review.review = request.POST.get('review')
	review.rating = request.POST.get('rating')
	review.created_at = timezone.now()
	review.save()
	return redirect('/dashboard')

def show_book(request, book_id):
	book = Book.objects.get(id=book_id)
	reviews = Review.objects.all().filter(book=book)
	context = {
	'book': book,
	'reviews': reviews
	}
	return render(request, 'bookreview/show.html', context)

def review_add(request, book_id):
	book = Book.objects.get(id=book_id)
	review = Review()
	review.rating = request.POST.get('rating')
	review.review = request.POST.get('review')
	review.created_at = timezone.now()
	review.user = User.objects.get(id=request.session['user_id'])
	review.book = book
	review.save()
	return redirect('/dashboard')

def delete_book(request, book_id):
	book = Book.objects.get(id=book_id)
	book.delete()
	return redirect('/dashboard')

def show_user(request, user_id):
	user = User.objects.get(id=user_id)
	reviews = Review.objects.all().filter(user=user)
	review = Review.objects.filter(user=user)
	context = {
	'user': user,
	'review': review,
	'reviews': reviews
	}
	return render(request, 'bookreview/showuser.html', context)

def logout(request):
	print "Logging Out"
	del request.session['user_id']
	return redirect('/')