from django.shortcuts import render

# Create your views here.

def Intrestcalculateview(request):
    if request.method=='GET':
        return render(request,'base.html')
def Intrestview(request):
    if request.method=='GET':
        return render(request,'IntrestApp/Intrest.html')
    if request.method=='POST':
        et1=int(request.POST['t1'])
        et2=float(request.POST['t2'])
        et3=int(request.POST['t3'])
        res=et1*et2*et3
        principle=et1
        return render(request,'IntrestApp/Intrest.html',{'msg':res,'principle':principle})
    
def compoundview(request):
    if request.method=='GET':
        return render(request,'IntrestApp/compound.html')
    if request.method=='POST':
        t1=int(request.POST['et1'])
        t2=float(request.POST['et2'])
        t3=int(request.POST['et3'])
        res=t1(1+(t2/100))^t3
        principle=t1
        return render(request,'IntrestApp/compound.html',{'msg':res,'principle':principle})
