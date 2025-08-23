from django.urls import path
from .views import QuizCreateView, QuizHistoryView, QuizRetrieveView, UpdateScoreView

urlpatterns = [
    path('quiz/create', QuizCreateView.as_view(), name='quiz-create'),
    path('quiz/take/<int:id>', QuizRetrieveView.as_view(), name='quiz-retrieve'),
    path('quizzes/user', QuizHistoryView.as_view(), name='quiz-history'),
    path('quiz/<int:id>/update-score', UpdateScoreView.as_view(), name='update-score')]
