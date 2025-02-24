from django.shortcuts import render,HttpResponse
from .models import Musiclist
from math import *

# Create your views here.
def index(request):
    song=Musiclist.objects.all()
    print(song)
    n=len(song)
    nSlides=n//4+ceil((n/4)-(n//4))
    params={"no_of_slides":nSlides,'range':range(1,nSlides),'songs':song}
    
    # allProd=[]
    # catagaryprod=Musiclist.objects.values('song_catagary',"id")
    # catagary={item['song_catagary'] for item in catagaryprod}
    # for c in catagary:
    #     prod=Musiclist.objects.filter(song_catagary=c)
    #     n=len(prod)
    #     nSlides=n//4+ceil((n/4)-(n//4))
    #     allProd.append([prod,range(1,nSlides),nSlides])
    # params={"allProd":allProd}

    return render(request,"index.html",params)
def contact(request):
    return render(request,"contact.html")
def search(request):
    search1=request.POST.get("search","")
    print(type(search1))  
    song=Musiclist.objects.filter(song_name=search1)
    # name=song.values("song_name")
    # name1=name.filter{song_name:search1}
    print(song)
    n=len(song)
    nSlides=n//4+ceil((n/4)-(n//4))
    params={"no_of_slides":nSlides,'range':range(1,nSlides),'songs':song}
    return render(request,"search.html",params)