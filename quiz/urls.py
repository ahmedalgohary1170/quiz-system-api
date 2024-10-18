from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView





from .views import QuizListCreateView, QuestionListCreateView, QuizSubmissionView, GradeSubmissionView, SignUpView

urlpatterns = [
    path('api/signup/', SignUpView.as_view(), name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('quizzes/', QuizListCreateView.as_view(), name='quiz-list-create'),
    path('questions/', QuestionListCreateView.as_view(), name='question-list-create'),
    path('submissions/', QuizSubmissionView.as_view(), name='quiz-submission'),
    path('submissions/<int:submission_id>/grade/', GradeSubmissionView.as_view(), name='grade-submission'),
]
