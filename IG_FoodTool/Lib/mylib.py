class RS():
    def __init__(self) -> None:
        pass
    
    def data_processing(result):
        
        data = list()
        buf = list()
        for i in range(len(result)):
            if i%3==0 and i/3>0:
                data.append(buf)
                buf = []
            buf.append(result[i])
        data.append(buf) 
        return data
    
    def mylib(n):
        print("success",n)
        return 2
    
    def get_condition(request):
        account_condi = request.POST.getlist("Account")
        region = request.POST.getlist("Region")
        if account_condi and region: return [{"PlaceID":int(item),"AccountName":acc} for item in  region for acc in account_condi ]
        elif region: return [{"PlaceID":int(item)} for item in request.POST.getlist("Region")]
        elif account_condi: return [{"AccountName":acc} for acc in account_condi ]
        else: return []
    def filter_condition(result,condition=[]):
        buf = []
        if condition:
            for condi in condition:
                for item in result.filter(**condi):
                    buf.append(item)
        else:
            for item in result:
                buf.append(item)
        return buf

    def sort(result,request):
        sort_condi = request.POST.getlist("Sort")
        if sort_condi and int(sort_condi[0])==2:
            reverse = True
        else:
            reverse = False
        return sorted(result,key=lambda item:item.PlaceID,reverse=reverse)
