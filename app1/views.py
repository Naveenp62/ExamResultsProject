from django.shortcuts import render

# Create your views here.
d={'results': [
        {'rollno':'214G1A3257','name':'Nadeem','year':'2021-2025','subjects':40,'result':'PASS'}, 
        {'rollno':'214G1A3249','name':'Madumitha','year':'2021-2025','subjects':40,'result':'PASS'},
        {'rollno':'214G1A3251','name':'Mahitha','year':'2021-2025','subjects':40,'result':'PASS'},
        {'rollno':'214G1A3262','name':'Naresh','year':'2021-2025','subjects':40,'result':'PASS'}
    ]}

def fun1(request):
    result=None
    if request.method=="POST":
        a=request.POST.get('num')
        for record in d['results']:
            if record.get('rollno')==a:
                result=record
                break

    if result is not None:
        return render(request,'form.html',{'result':result})
    else:
        return render(request,'form.html')