from django.urls import path
from .views import submit_review, review_success

urlpatterns = [
    path('submit/', submit_review, name='submit_review'),
    path('success/<int:review_id>/', review_success, name='review_success'),
]
