from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .scraping import getPageSource, getTime, exportAsDict, makeList, changeData, beRowData

from scheduler.models import  User, Org


def index(request):
    #indexを読み込んでデフォルトの画面表示
    #暫定的にtest.htmlを読み込み中↓
    return render(request, "scheduler/test.html")

#execute function
def execute(request):
    if request.method == 'POST':
        # ユーザー登録に必要なデータ軍の定義
        student_id = request.POST["student_id"]
        team_id = request.POST["team_id"]
        pswd = request.POST["password"]
        team_name = request.POST["display_name"]
        user_name = request.POST["username"]


        html = getPageSource(id, pswd) #don't commit leave the password
        dict_data = exportAsDict(html)
        print(1)
        print(2)
        dict_data = dict_data['Spring']
        pre_class, aft_class = changeData(dict_data)

        pre_class = beRowData(pre_class)
        aft_class = beRowData(aft_class)
        """
        書き出しサイズがオーバーフローを起こすため10進数に変換して書き込む
        """
        database_p = Org(
            team_id = team_id,
            share_pre = int(pre_class, 2),
            share_aft = int(aft_class, 2),
            team_name = team_name,
        )
        database_p.save()
        database_u = User(
            student_id = student_id,
            qtr_pre = pre_class,
            qtr_aft = aft_class,
            display_name = user_name,
        )
        database_u.save()

    return render(request, "scheduler/index.html")


def makeOrg(request):
    if request.method == 'POST':
        team_id = request.POST["team_id"] # 任意のteam_id
        db_org = Org(team_id=team_id)
        db_org.save()

    return render(request, "scheduler/makeorg.html")


def joinOrg(request):
    if request.method == 'POST':
        team_id = request.POST["team_id"] # 参加するチームのteam_id
        display_name = request.POST["display_name"] #チーム内での任意の表示名

        db_usr = User(
            #org = team_id,
            display_name = display_name,
        )
        db_usr.save()

    return render(request, "scheduler/join.html")