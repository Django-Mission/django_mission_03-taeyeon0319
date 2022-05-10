from django.contrib import admin
from .models import *
# Register your models here.

class AnswerInLine(admin.TabularInline):
    #inquiry 모델에 인라인 모델로 추가
    model = Answer
    extra = 5

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'updated_at',
    )
    search_fields = (
        'title',
    )
    fields = ['category']

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = (
        'Inquiry_title',
        'Inquiry_category',
        'Inquiry_updated_at',
        'Inquiry_writer',
    )
    search_fields = (
        'Inquiry_title',
        'Inquiry_email',
        'Inquiry_number',
    )
    fields = ['Inquiry_category']
    inlines = [
        AnswerInLine,
    ]
