from rest_framework import serializers

from .models import Questions


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ("id", "title", "text", "option_1", "option_2", "option_3", "option_4", "correct_option",
                  "question_type", "difficulty", "from_tizhooshan_exam", "grade", "chapter_no")

    def create(self, validated_data):
        return Questions.objects.create(
            accepted=False,
            **validated_data
        )
