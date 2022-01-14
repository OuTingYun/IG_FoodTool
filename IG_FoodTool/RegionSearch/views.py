from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import pandas as pd
from RegionSearch.models import total,Store
from Lib.mylib import RS
from django.db import connection
from django.db.models import Q
# Create your views here.
# IG_Acccount = ['Foody_tw','kangol_eat.foodie','cathyfoodie_150']
Sort = {"逆時針":1,"順時針":2}
Region = {"全台":0,"基隆":1,"台北":2,"新北":3,"桃園":4,"新竹":5,"苗栗":6,"台中":7,"彰化":8,"南投":9,"雲林":10,"嘉義":11,"台南":12,"高雄":13,"屏東":14,"台東":15,"花蓮":16,"宜蘭":17,"澎湖":18,"金門":19}

def regionsearch(request):
    # 拿資料庫所有東西
    Nothing = False
    result = total.objects.all()
    IG_Acccount = Store.objects.all()
    
    if request.method=='GET':
        result = RS.data_processing(result)
    elif request.method=='POST':
        print("============================",request.POST.getlist("Region"))
        print("============================",request.POST.getlist("Account"))
        print("============================",request.POST.getlist("Sort"))
        
        condition = RS.get_condition(request)
        print(condition)
        result = RS.filter_condition(result,condition = condition)
        print(result)
        result = RS.sort(result,request)

        result = RS.data_processing(result)
        print(result[0])
        if len(result[0])==0:
            Nothing=True
    return render(request, 'region.html' , {'IG_Acccount' : IG_Acccount,'Region':Region,"Sort":Sort,"result":result,'nothing':Nothing})

    
    # C = total.objects.all()
    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM regionsearch_total WHERE PlaceID=1 ')
    # C = cursor.fetchall()

        # print(len(result))
    # C = [[1,2,3],[4,5,6],[7,8,9]]
    # return render(request, 'base.html' , {'C':C})