from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,UserInfo
# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}

    return render(request, 'first_app/index.html', context=date_dict)

def users(request):
    user_list = UserInfo.objects.order_by()
    user_dict = {'user_info':user_list}
    return render(request, 'first_app/users.html', context=user_dict)
