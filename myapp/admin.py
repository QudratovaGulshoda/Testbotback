from django.contrib import admin
from .models import *
from django.contrib.auth.models import *
admin.site.unregister(Group)
# Register your models here.
class AnswerInline(admin.TabularInline):
    line_numbering = 0
    model = Answers
    max_num = 30
    min_num = 30
    can_delete = False
    radio_fields = {'answer':admin.VERTICAL}
    fields = ('line_number','answer',)
    readonly_fields = ('line_number',)
    def line_number(self, obj):
        self.line_numbering += 1
        return self.line_numbering

    line_number.short_description = '№'
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 10
    search_fields = ['name']
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['code','category','uploaded','filesize']
    list_filter = ['category','uploaded','changed']
    list_display_links = ['code']
    list_per_page = 10
    list_max_show_all = 15
    search_fields = ['code','categor__name']
    readonly_fields = ('code',)
    fields = ('category','file',)
@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['name','telegram_id']
    list_per_page = 10
    search_fields = ['name','telegram_id']
@admin.register(TestDone)
class TestDoneAdmin(admin.ModelAdmin):
    list_display = ['test_code','telegram_id','name','trues','falses']
    search_fields = ['name']
    list_filter = ['date','test_code']
    list_per_page = 10
    ordering = ['-true_answers']
    def trues(self,obj):
        return obj.true_answers
    trues.short_description = "✅ True Answers"
    def falses(self,obj):
        return obj.false_answers
    falses.short_description = "❌ False Answers"
@admin.register(DailyTest)
class DailyTestAdmin(admin.ModelAdmin):
    list_display = ['telegram_id','date']
    list_filter = ['date']
    list_per_page = 10


