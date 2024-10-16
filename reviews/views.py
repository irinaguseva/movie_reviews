from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import MovieReview
import joblib 
import cv

model = joblib.load('model.pkl')

def analyze_sentiment(text):
    analysis = model.predict(cv.transform([text]))[0])
    return analysis

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.rating = analyze_sentiment(review.text)
            review.save()
            return redirect('review_success', review.id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})

def review_success(request, review_id):
    review = MovieReview.objects.get(id=review_id)
    return render(request, 'reviews/review_success.html', {'review': review})

