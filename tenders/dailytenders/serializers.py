from rest_framework import serializers
from dailytenders.models import Tender, LANGUAGE_CHOICES, STYLE_CHOICES


class TenderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(required=False, allow_blank=True)
    tender_number = serializers.CharField(style={'base_template': 'textarea.html'})
    start_date = serializers.BooleanField(required=False)
    end_date = serializers.ChoiceField(choices=STYLE_CHOICES,required=False)
   
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.description = validated_data.get('description', instance.description)
        instance.tender_number = validated_data.get('tender_number', instance.tender_number)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()
        return instance