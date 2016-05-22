from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from .models import FeedbackMessage
from .serializer import FeedbackSerializer


class FeedbackList(APIView):

    def get(self, request):
        snippets = FeedbackMessage.objects.all()
        serializer = FeedbackSerializer(snippets, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        if request.user.is_authenticated():
            user_data = User.objects.get(username=request.user)
            data = {'name': user_data.first_name,
                  'surname': user_data.last_name,
                  'email': user_data.email,
                  'text': request.data['text']}

            if 'attach' in request.data:
                data['attach'] = request.data['attach']
        else:
            data=request.data
        serializer = FeedbackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
