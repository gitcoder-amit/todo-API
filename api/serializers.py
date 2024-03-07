from api.models import Todo
from rest_framework import serializers
import re

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ['uid','title', 'description', 'is_done']
    

    def validate(self, validated_data):
        print(validated_data)  #OrderedDict([('title', 'title1'), ('description', 'description1')])
        if validated_data.get('title'):
            title = validated_data.get('title')
            regex = re.compile('[@!#]')
            if not regex.search(title) == None:
                raise serializers.ValidationError("title can't contain special character")
        return validated_data

    def validate_description(self, data):
        if data:
            description = data
            if len(description) > 4:
                raise serializers.ValidationError("description can't be greater tha 4")
        return data
        
