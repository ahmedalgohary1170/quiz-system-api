from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Quiz, Question, Choice, StudentQuizSubmission, Answer
from .serializers import QuizSerializer, QuestionSerializer, ChoiceSerializer, StudentQuizSubmissionSerializer, AnswerSerializer





from django.contrib.auth import get_user_model
from .serializers import UserSerializer

class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]


class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class QuizSubmissionView(generics.ListCreateAPIView):
    queryset = StudentQuizSubmission.objects.all()
    serializer_class = StudentQuizSubmissionSerializer
    permission_classes = [IsAuthenticated]




class GradeSubmissionView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        submission = StudentQuizSubmission.objects.get(id=kwargs['submission_id'])
        correct_answers = 0
        total_questions = submission.quiz.questions.count()

        for answer in submission.answers.all():
            if answer.choice.is_correct:
                correct_answers += 1

        submission.score = (correct_answers / total_questions) * 100
        submission.save()

        return Response({'score': submission.score})

