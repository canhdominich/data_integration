from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import datetime
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from myapp.models import NewsPaper

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json

def clearDatabase(request):
    newspaper = NewsPaper.objects.all()
    newspaper.delete()

def storeNewsPaper(request):
    # clear data
    # clearDatabase(request)

    # open file json
    # myfile = open('/home/canhdominich/PycharmProjects/first_project/sukien.json', 'r')
    # myfile = open('/home/canhdominich/PycharmProjects/first_project/thegioi.json', 'r')
    # myfile = open('/home/canhdominich/PycharmProjects/first_project/suckhoe.json', 'r')
    # myfile = open('/home/canhdominich/PycharmProjects/first_project/giaoduc.json', 'r')
    # myfile = open('/home/canhdominich/PycharmProjects/first_project/sohoa.json', 'r')
    myfile = open('/home/canhdominich/PycharmProjects/first_project/sohoa.json', 'r')
    data = myfile.read()

    # parse file
    obj = json.loads(data)

    # count object
    json_size = len(obj)

    # insert data
    for i in range(0, json_size):
        value_time = obj[i]['time']
        value_title = obj[i]['title']
        value_slug = value_title+get_random_string(length=16)
        value_slug = value_slug.strip()
        value_slug = value_slug.replace(" ", "-")
        value_slug = slugify(value_slug)
        value_thumbnail = obj[i]['thumbnail']
        value_description = obj[i]['description']
        value_content = obj[i]['content']
        value_author = obj[i]['author']

        newpaper = NewsPaper(
                             time = value_time,
                             title= value_title,
                             slug = value_slug,
                             category = 5,
                             thumbnail = value_thumbnail,
                             description = value_description,
                             content = value_content,
                             author = value_author,
                             created_at = datetime.now(),
                             updated_at=datetime.now()
                             )
        newpaper.save()
    return home(request)

def index(request):
    # storePaper(request)
    newspaper = NewsPaper.objects.all()
    total = NewsPaper.objects.count()
    return render(request, 'appdemo/index.html', {"data" : newspaper, "total" : total})

def detail(request, id):
    newpaper = NewsPaper.objects.get(id = id)
    return render(request, 'appdemo/detail.html', {'data' : newpaper})

def update(request, id, title):
    newpaper = NewsPaper.objects.get(id = id)
    newpaper.title = title
    newpaper.save()
    return index(request)

def delete(request, id):
    newpaper = NewsPaper.objects.get(id = id)
    newpaper.delete()
    return index(request)

def home(request):
    feature_eve = NewsPaper.objects.filter(category=1).order_by('-title').first()
    eve = NewsPaper.objects.filter(category=1).order_by('-created_at')[:2]

    feature_wod = NewsPaper.objects.filter(category=2).order_by('-title').first()
    wod = NewsPaper.objects.filter(category=2)[:2]

    feature_heh = NewsPaper.objects.filter(category=3).order_by('-title').first()
    heh = NewsPaper.objects.filter(category=3)[:2]

    feature_edu = NewsPaper.objects.filter(category=4).order_by('-title').first()
    edu = NewsPaper.objects.filter(category=4)[:2]

    feature_tec = NewsPaper.objects.filter(category=5).order_by('-title').first()
    tec = NewsPaper.objects.filter(category=5)[:2]

    firstnewpaper = NewsPaper.objects.order_by().first()
    featurenewspaper = NewsPaper.objects.all().order_by('-created_at')[:8]
    interestnewspaper = NewsPaper.objects.all().order_by()[:20]

    newspaper = NewsPaper.objects.all()
    return render(
        request,
        'appnews/home.html',
        {
            "data" : newspaper,
            "firstnewpaper" : firstnewpaper,
            "featurenewspaper" : featurenewspaper,
            "interestnewspaper" : interestnewspaper,
            "eve": eve,
            "wod": wod,
            "heh": heh,
            "edu": edu,
            "tec": tec,
            "feature_eve": feature_eve,
            "feature_wod": feature_wod,
            "feature_heh": feature_heh,
            "feature_edu": feature_edu,
            "feature_tec": feature_tec
        })

def listNewPaperByCategory(request, category_id):
    firstnewpaper = NewsPaper.objects.filter(category = category_id)[:1].get()
    featurenewsleft = NewsPaper.objects.order_by('-created_at').filter(category=category_id)[:2]
    featurenewsright = NewsPaper.objects.order_by('title').filter(category=category_id)[:2]

    # newspaper_list = NewsPaper.objects.filter(category = category_id)
    newspaper_list = NewsPaper.objects.all()

    paginator = Paginator(newspaper_list, 15)  # Show 25 contacts per page

    page = request.GET.get('page')
    newspaper = paginator.get_page(page)

    interestnewspaper = NewsPaper.objects.order_by()[:30]

    return render(
        request,
        'appnews/category.html',
        {
            "firstnewpaper": firstnewpaper,
            "featurenewsleft": featurenewsleft,
            "featurenewsright": featurenewsright,
            "newspaper": newspaper,
            "interestnewspaper": interestnewspaper
        })

def detailNewPaper(request, slug):
    newpaper = NewsPaper.objects.get(slug = slug)
    interestnewspaper = NewsPaper.objects.all().order_by()[:8]
    if newpaper != None:
        relationnewpaper = NewsPaper.objects.filter(category = newpaper.category).order_by('created_at')[:3]
        return render(
            request,
            'appnews/detail.html',
            {
                "newpaper": newpaper,
                "relationnewpaper": relationnewpaper,
                "interestnewspaper": interestnewspaper
            })
    return home(request)


