from django.shortcuts import render
from django.views import View
import requests
import operator
from functools import reduce

class Covid19(View):
    def getJsonData(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

        json_data = requests.get('https://api.covid19india.org/state_district_wise.json',headers=headers)
        dict_data = json_data.json()
        return dict_data

    def getFromDict(self,dict_data, mapList):
        return reduce(operator.getitem, mapList, dict_data)

    def get(self,request):
        data = self.getJsonData()
        return render(request,'index.html',{'response':data.keys()})

    def post(self,request,*args,**kwargs):

        x = request.POST.get('t1')
        y = request.POST.get('t2')

        data = self.getJsonData()
        l = []
        l.append(x)
        s = "districtData"
        l.append(s)
        map_data = self.getFromDict(dict_data=data, mapList=l)

        if y == None:
            return render(request,'index.html',{'response1':l[0],'response2':map_data})
        else :
            l.append(y)
            map_data1 = self.getFromDict(dict_data=data,mapList=l)
            print(map_data1)
            return render(request,'index.html',{'response1':l[0],'response2':map_data,'response3':l[2],'response4':map_data1})


