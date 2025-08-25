from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status

from .serializers import QuizCreateSerializer, QuizSerializer
from .models import Quiz


class QuizCreateView(generics.CreateAPIView):
    serializer_class = QuizCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = self.get_serializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        quiz = serializer.save(user=request.user)

        output_serializer = QuizSerializer(quiz)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


class QuizRetrieveView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Quiz.objects.filter(user=self.request.user)


class QuizHistoryView(generics.ListAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Quiz.objects.filter(user=self.request.user).order_by('-created_at')


class UpdateScoreView(generics.UpdateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Quiz.objects.filter(user=self.request.user)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
