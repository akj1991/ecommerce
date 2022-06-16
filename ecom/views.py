from django.http import JsonResponse
from django.shortcuts import render
from ecom.models import mobile_details

def adminlogin(request):
    return render (request,'adminlogin.html')

def forgotpass(request):
    return render (request,'forgotpass.html')

def adminhomefun(request):
    return render (request,'admindashboard.html')

def registmobile(request):
    return render (request,'registmobile.html')

def managepro(request):
    return render (request,'manageproduct.html')

def regifun1(request):
    model=request.POST['model']
    brand=request.POST['brand']
    rate=request.POST['rate']
    image=request.POST['image']
    reg_details=mobile_details(model=model,brand=brand,rate=rate,image=image)
    reg_details.save()
    return JsonResponse({'message': "data inserted"})

def loaddata(request):
    tabledata=mobile_details.objects.all()
    data=[{'model':data.model, 'brand':data.brand, 'rate':data.rate, 'image':data.image, 'id':data.id}for data in tabledata]
    return JsonResponse({'datapass':data})

def deletebutton(request):
    id=request.POST['key']
    print(id)
    mobile_details.objects.get(id=id).delete()
    return JsonResponse({'message': 'data deleted'})

def updatebutton(request):
    id=request.POST['key']
    update_details=mobile_details.objects.get(id=id)
    update_data=[{'id':update_details.id, 'model':update_details.model,'brand':update_details.brand, 'rate':update_details.rate, 'image':update_details.image }]
    return JsonResponse({'jsonupdate': update_data})

def updatefun(request):
    id=request.POST['key']
    username=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    age=request.POST['age']
    mobile_details.objects.filter(id=id).update(username=username, password=password, email=email, age=age)
    return JsonResponse({'message': 'Data Updated'})
