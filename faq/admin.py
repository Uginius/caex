from django.contrib import admin
from django import forms
from faq.models import Ques
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
#
#
#
# class PostAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorUploadingWidget())
#
#     class Meta:
#         model = Ques
#         fields = '__all__'


@admin.register(Ques)
class QuesAdmin(admin.ModelAdmin):
    list_display = 'pk', 'order', 'question', 'note', 'answer_short', 'published', 'updated'
    list_display_links = 'order', 'question', 'note', 'answer_short'
    # form = PostAdminForm
