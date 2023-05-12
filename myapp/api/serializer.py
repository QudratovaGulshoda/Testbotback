from rest_framework import serializers
from myapp.models import *
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = '__all__'
class TestSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    answers = serializers.StringRelatedField(read_only=True)
    answers = serializers.SerializerMethodField(read_only=True)
    filesize = serializers.SerializerMethodField(read_only=True)
    category_id = serializers.SerializerMethodField(read_only=True)
    def get_filesize(self,obj):
        return obj.filesize
    def get_category_id(self,obj):
        return obj.category.id
    def get_answers(self,obj):
        data = {}
        answers = obj.answers.all()
        for index,answer in enumerate(answers,start=1):
            data[index] =answer.answer

        return data
    class Meta:
        model = Test
        fields =['id','code','uploaded','changed','category','answers','file','filesize','category_id']
class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'
class TestDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDone
        fields = '__all__'

