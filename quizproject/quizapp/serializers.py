from rest_framework import serializers
from .models import Question, Quiz, DIFFICULTY_CHOICES
from django.db import transaction
from .ai import generate_mcq


class QuizCreateSerializer(serializers.Serializer):
    topic = serializers.CharField(max_length=255)
    number_of_questions = serializers.IntegerField(min_value=1, max_value=20)
    difficulty = serializers.ChoiceField(choices=DIFFICULTY_CHOICES)

    def validate(self, attrs):
        user = self.context['request'].user
        topic = attrs.get('topic')
        difficulty = attrs.get('difficulty')

        # Check for duplicate quiz
        if Quiz.objects.filter(user=user, topic=topic, difficulty=difficulty, completed=False, score=0).exists():
            raise serializers.ValidationError(
                "You already have an incomplete quiz for this topic and difficulty.")
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        topic = validated_data['topic']
        number_of_questions = validated_data['number_of_questions']
        difficulty = validated_data['difficulty']

        with transaction.atomic():
            quiz = Quiz.objects.create(user=user, topic=topic,
                                       number_of_questions=number_of_questions,
                                       difficulty=difficulty, score=0)

            # generate mcq based on the request using gemini
            questions = generate_mcq(topic, number_of_questions, difficulty)
            if not questions or not isinstance(questions, list):
                raise serializers.ValidationError(
                    "Failed to generate questions.")

            for q in questions:
                if not all(k in q for k in ['question', 'options', 'answer']):
                    raise serializers.ValidationError(
                        "Invalid question format.")

                Question.objects.create(
                    quiz=quiz,
                    text=q['question'],
                    option_a=q['options']['a'],
                    option_b=q['options']['b'],
                    option_c=q['options']['c'],
                    option_d=q['options']['d'],
                    correct_option=q['answer'].lower()
                )
        return quiz


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "text", "option_a", "option_b",
                  "option_c", "option_d", "correct_option"]


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ["id", "topic", "number_of_questions",
                  "difficulty", "created_at", "completed", "questions", "score"]
