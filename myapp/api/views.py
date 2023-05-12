from django.shortcuts import render
from .serializer import *
from myapp.models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
import random
from rest_framework import status
# Create your views here.
# Category Viewset
class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
# Test Viewset
class TestViewset(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
# Get Test From Choose Category
class TestFromCategory(APIView):
    def get(self,request,id,telegram_id):
        test_codes = []
        tests = TestDone.objects.filter(telegram_id=telegram_id)
        for test in tests:
            test_codes.append(test.test_code)
        test_codes = list(dict.fromkeys(test_codes))
        category = Category.objects.get(id=id)
        tests = list(Test.objects.filter(category=category).exclude(code__in=test_codes))
        if tests==[]:
            return Response({"status":"Not Found"},status=status.HTTP_204_NO_CONTENT)
        else:
            test = random.choice(tests)
            serializer = TestSerializer(instance=test, partial=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
# Test from all category
class TestFromAllCategory(APIView):
    def get(self,request):
        tests = list(Test.objects.all())
        if tests == []:
            return Response({"status": "Not Found"}, status=status.HTTP_204_NO_CONTENT)
        else:
            test = random.choice(tests)
            serializer = TestSerializer(instance=test, partial=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
# Bot User Viewset
class BotUserViewset(ModelViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
# Test Done Viewset
class TestDoneViewset(ModelViewSet):
    queryset = TestDone.objects.all()
    serializer_class = TestDoneSerializer
    filter_backends = [SearchFilter]
    search_fields = ['=telegram_id']
# Daily Test View
class DailyTestView(APIView):
    def get(self,request,telegram_id):
        from datetime import datetime
        today  = datetime.now().date()
        daily_tests = DailyTest.objects.filter(telegram_id=telegram_id).filter(date=today)
        if len(daily_tests)>=3:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            # daily_test = DailyTest.objects.create(telegram_id=6227197910)
            return Response(status=status.HTTP_201_CREATED)
# Daily Test Create View
class DailyTestCreateView(APIView):
    def get(self,request,telegram_id):
        from datetime import datetime
        today  = datetime.now().date()
        daily_tests = DailyTest.objects.filter(telegram_id=telegram_id).filter(date=today)
        if len(daily_tests)>=3:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            daily_test = DailyTest.objects.create(telegram_id=telegram_id)
            return Response(status=status.HTTP_201_CREATED)

