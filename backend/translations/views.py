from rest_framework.views import APIView
from rest_framework.response import Response
# WRACAMY do Twojego autorskiego importu:
from .models import Translation, User 
from .serializers import TranslationSerializer

class TranslateAPIView(APIView):
    def post(self, request):
        source_text = request.data.get('text')
        target_lang = request.data.get('lang')

        if not source_text or not target_lang:
             return Response({"error": "Brak tekstu lub języka w zapytaniu!"}, status=400)

        # Szukamy pierwszego użytkownika z Twojej własnej tabeli
        user = User.objects.first()

        if not user:
            return Response({"error": "Baza jest pusta! Dodaj swojego własnego Usera w panelu Admina."}, status=400)

        translation = Translation.objects.create(
            user=user,
            source_text=source_text,
            translated_text=f"Przetłumaczono: {source_text}",
            target_lang=target_lang
        )

        serializer = TranslationSerializer(translation)
        return Response(serializer.data)