from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .api.views import *
router = DefaultRouter()
router.register('category',CategoryViewset)
router.register('test',TestViewset)
router.register('users',BotUserViewset)
router.register('testdone',TestDoneViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('withcategory/<int:id>/<int:telegram_id>/',TestFromCategory.as_view()),
    path('allcategory/',TestFromAllCategory.as_view()),
    path('daily/<int:telegram_id>/',DailyTestView.as_view()),
    path('daily/<int:telegram_id>/',DailyTestView.as_view()),
    path('dailycreate/<int:telegram_id>/', DailyTestCreateView.as_view())
]