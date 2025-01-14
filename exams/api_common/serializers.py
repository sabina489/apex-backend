from rest_framework import serializers

from ..models import Exam


class ExamMiniSerializer(serializers.ModelSerializer):
    """Exam Mini Serializer."""

    class Meta:
        model = Exam
        fields = ("id", "name")
        read_only_fields = fields
