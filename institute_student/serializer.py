from rest_framework import serializers

class EmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'student_info'