from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from . import scraping

from scheduler.models import  User,Org


def index(request):
    #indexを読み込んでデフォルトの画面表示
    #暫定的にtest.htmlを読み込み中↓
    return render(request, "scheduler/test.html")

#execute function
def execute(request):
    if request.method=='POST':

        #サイトからの変数取得構造体とかにしていいかも
        id = request.POST["student_id"]
        team_id = request.POST["team_id"]
        pswd = request.POST["password"]
        Team_name = request.POST["display_name"]
        User_name = request.POST["username"]


        html = scraping.getPageSource(id, pswd) #don't commit leave the password
        dict_data = scraping.exportAsDict(html)

        if getTime() ==0:
            dict_data = dict_data['Spring']
            pre_class=be_rowdata(changedata(dict_data))
            aft_class=be_rowdata(changedata(dict_data))
            database_u = User(student_id = id ,q_pre = pre_class,q_aft = aft_class,name = User_name,team = team_id)
        else:
            """
            dict_data = dict_data['Autumn']
            personal_class=changedata(dict_data)
            database_u = User(student_id = ,q_pre=,q_aft = , name = ,) 
            """
            return render(request, "scheduler/index.html", dict_data)
 
    return render(request, "scheduler/index.html", dict_data)
