from django.contrib import admin

# Register your models here.
from .models import NewsPaper

from django.contrib import messages

import nltk

class CustomNewsPaper(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('time', 'title', 'thumbnail', 'description', 'author', 'created_at')

    def save_model(self, request, obj, form, change):
        value_title = obj.title
        titles = NewsPaper.objects.all()
        flag = True

        sent = set(value_title)

        for item in titles:
            sent_item = set(item.title)

            distance = nltk.jaccard_distance(sent, sent_item)
            if(distance < 0.2):
                flag = False

        if(flag):
            super().save_model(request, obj, form, change)
        else:
            return messages.add_message(request, messages.INFO, 'Bài viết của bạn không được chấp nhận')

admin.site.register(NewsPaper, CustomNewsPaper)