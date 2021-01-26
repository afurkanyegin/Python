from django.shortcuts import render
import requests,json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "c2c2ddc476mshade8b9011586066p1c4ba0jsn48f6fe3b3ef1",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.

def helloworldview(request):
    n=int(response['results'])
    countrylist=[]
    for a in range(0,n):
        countrylist.append(response['response'][a]['country'])
    if request.method=="POST":
        selectedcountry=request.POST["selectedcountry"]
        
        for r in range(0,n):
            if selectedcountry == response['response'][r]['country']:
                population=response['response'][r]['population']
                new=response['response'][r]['cases']['new']
                active=response['response'][r]['cases']['active']
                critical=response['response'][r]['cases']['critical']
                recovered=("None" if response['response'][r]['cases']['recovered']==None else response['response'][r]['cases']['recovered'])
                total=response['response'][r]['cases']['total']
                death=("None" if response['response'][r]['cases']['total']==None or response['response'][r]['cases']['active']==None or response['response'][r]['cases']['recovered']==None else int(total)-int(active)-int(recovered))
        content={'countrylist':countrylist,'population':population,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'death':death,'selectedcountry':selectedcountry}
        return render(request,'covidapp/helloworld.html',content)
    content={'countrylist':countrylist}
    return render(request,'covidapp/helloworld.html',content)