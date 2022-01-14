from django.shortcuts import render
from Lib.scrap_data import SP
from RegionSearch.models import total,Store
import pandas as pd
def scrap(request):
    C = [[1,2,3],[4,5,6],[7,8,9]]
    if request.method=="POST":
        AccountName = request.POST.getlist('AccountName')
        n_scroll = request.POST.getlist('Round')
        SP.add_store(Store.objects.all(),AccountName,Store)
        data = SP.scrap(n_scroll,AccountName)
        result = total.objects.all()
        data = SP.compare(result,data,AccountName)
        SP.Insert(post=total,data =data)

    round = [i+1 for i in range(20)]
    return render(request, 'base.html',{"round":round})

