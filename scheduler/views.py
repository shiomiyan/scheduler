from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .scraping import getPageSource, getTime, exportAsDict, makeList, changeData, beRowData
from scheduler.models import  User, Org


def index(request):
    #indexを読み込んでデフォルトの画面表示
    return render(request, "scheduler/index.html")


def makeuser(request):
    if request.method == 'POST':
        # ユーザー登録に必要なデータ軍の定義
        id = request.POST["school_number"]
        pswd       = request.POST["password"]
        
        # ユーザーの講義データを取得
        html      = getPageSource(id, pswd)
        dict_data = exportAsDict(html)
        dict_data = dict_data['Spring']
        pre_class, aft_class = changeData(dict_data)

        # 講義データのバイナリ変換
        pre_class = beRowData(pre_class)
        aft_class = beRowData(aft_class)

        # 書き出しサイズがオーバーフローを起こすため10進数に変換して書き込む
        db_user = User(
            student_id = id,
            team = None,
            qtr_pre = int(pre_class, 2),
            qtr_aft = int(aft_class, 2),
        )
        db_user.save()
    return render(request, "scheduler/makeuser.html")


def makeorg(request):#チームID作成
    if request.method == 'POST':
        team_id = request.POST["team_id"] # 任意のteam_id
        db_org = Org(team_id=team_id,)
        db_org.save()

    return render(request, "scheduler/makeorg.html")


def joinorg(request):
    if request.method == 'POST':
        if request.filter(Org.objects.get("team_id").exists()):
            print("ok")
        team_id_post = request.POST["org"] # 参加するチームのteam_id
        team_id_org = Org.objects.get(team_id=team_id_post)
        school_number =request.POST["school_number"]
        password    =request.POST["password"]

        db_usr = User(team_id=team_id_org,team_pre = 1,team_aft= 1)#Database更新
        db_usr.save()

    return render(request, "scheduler/join.html")

