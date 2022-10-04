from multiprocessing import context
from django.shortcuts import render, HttpResponse
from .models import ReportDB
# Create your views here.
def reportHome(request):
    data = ReportDB.objects.all()
    context = {'data':data}
    return render(request, 'reportPage.html', context)

def reportEntry(request):
    if request.method == "POST":
        srno = request.POST['srNo']
        desc = request.POST['desc']
        finish = request.POST['finish']
        refImg = request.FILES['refImg']
        width = request.POST['width']
        height = request.POST['height']
        area = request.POST['area']
        uqm = request.POST['uqm']
        qty = request.POST['qty']
        rate = request.POST['rate']
        amount = request.POST['amount']
        report = ReportDB(srno=srno, desc=desc, finish=finish, refImg=refImg, width=width, height=height, area=area, uqm=uqm, qty=qty, rate=rate, amount=amount)
        report.save()
    return render(request, 'reportEntry.html')