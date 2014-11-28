# -*- coding: utf8 -*-
from django.contrib import admin
from models import Question,Choice

# Register your models here.

#Question的管理界面，设置两块内容
#(控件类型，{‘fields’:元组})
#HTML class是可选的，可定义样式
#collapse是隐藏表单，这个在你表单内容很多的时候，可用

#（方法二）关联Choice和Question
class ChoiceInline(admin.TabularInline): #admin.StackedInline 前面的比较节省空间
    model = Choice
    extra = 0 #这个如果不设置的话，默认是3，就是说每次进入Question都会有三条空白

class QuestionAdmin(admin.ModelAdmin):

    list_display = ('question_text','pub_data','was_published_recently')
    list_filter = ['pub_data','question_text']
    search_fields = ['pub_data']
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('Date information',{'fields':['pub_data'],'classes':['collapse']}),
        ]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice) （方法一）添加Choice到管理后台
#方法一有弊端：就是都要特地去添加Choice去关联Question，不能做到，添加问题的时候就添加选择
