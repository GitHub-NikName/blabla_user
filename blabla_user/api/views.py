from django.shortcuts import get_object_or_404
from django.http.response import FileResponse
from rest_framework.generics import CreateAPIView

from .utils import convert_to_mp3
from user.models import Audio, User
from .serializers import SignupSerializer, RecordSerializer


class Signup(CreateAPIView):
    """Создает пользователя."""
    queryset = User.objects.all()
    serializer_class = SignupSerializer


class Record(CreateAPIView):
    """Получает wav, конвертирует в mp3, сохраняет в бд.
     GET запрос отдает файл на скачивание."""

    queryset = Audio.objects.all()
    serializer_class = RecordSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.data['user'])
        file = self.request.data['file']
        file = convert_to_mp3(file)
        serializer.save(user=user, file=file)

    def get(self, request, *args, **kwargs):
        id = request.query_params.get('id')
        user_id = request.query_params.get('user')
        obj = get_object_or_404(Audio, id=id, user=user_id)
        return FileResponse(obj.file, as_attachment=True)
