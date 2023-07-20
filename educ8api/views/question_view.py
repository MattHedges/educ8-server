from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from educ8api.models import Question, Category, Language


class QuestionView(ViewSet):
    """Level up question view"""

    def retrieve(self, request, pk):

        question = Question.objects.get(pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def create(self, request):
        """create question"""
        language = Language.objects.get(pk=request.data["language"])
        category = Category.objects.get(pk=request.data["category"])

        question = Question.objects.create(
        question=request.data["question"],
        answer=request.data["answer"],
        example=request.data["example"],
        language=language,
        category=category
        )
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """"update question"""

        language = Language.objects.get(pk=request.data["language"])
        category = Category.objects.get(pk=request.data["category"])

        question = Question.objects.get(pk=pk)
        question.question = request.data["question"]
        question.answer = request.data["answer"]
        question.example = request.data["example"]
        language = language
        category = category
        question.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """delete question"""
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class QuestionSerializer(serializers.ModelSerializer):
    """JSON serializer for question
    """
    class Meta:
        model = Question
        fields = ('id', 'question', 'example', 'language', 'category' )
        depth = 1
