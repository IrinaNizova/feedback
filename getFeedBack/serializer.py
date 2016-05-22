from .models import FeedbackMessage
from rest_framework import serializers
from django.contrib.auth.models import User


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = FeedbackMessage
        fields = ('owner', 'name', 'surname', 'email', 'phone', 'text', 'attach')

