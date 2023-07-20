from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from educ8api.models import Language


class LanguageView(ViewSet):
    """Level up language view"""

    def retrieve(self, request, pk):

        language = Language.objects.get(pk=pk)
        serializer = LanguageSerializer(language)
        return Response(serializer.data)

    def create(self, request):
        """create language"""

        language = Language.objects.create(
        language=request.data["language"],
        )
        serializer = LanguageSerializer(language)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """"update language"""

        language = Language.objects.get(pk=pk)
        language.language = request.data["language"]
        language.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """delete language"""
        language = Language.objects.get(pk=pk)
        language.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class LanguageSerializer(serializers.ModelSerializer):
    """JSON serializer for language
    """
    class Meta:
        model = Language
        fields = ('id', 'name')
        depth = 1
