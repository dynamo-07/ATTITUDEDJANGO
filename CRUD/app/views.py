from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee_Data
def form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        joining_date = request.POST.get('joining_date')
        emp = Employee_Data(
            full_name=name,
            email=email,
            phone=phone,
            department=department,
            joining_date=joining_date
        )
        emp.save()
        return redirect('list1')
    return render(request, 'form.html')
def list1(request):
    employees = Employee_Data.objects.order_by('joining_date')
    return render(request, 'list.html', {'data': employees})
def Edit_Data(request, full_name):
    employee = get_object_or_404(Employee_Data, full_name=full_name)
    if request.method == "POST":
        employee.full_name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.phone = request.POST.get('phone')
        employee.department = request.POST.get('department')
        employee.joining_date = request.POST.get('joining_date')
        employee.save()
        return redirect('list1')  
    return render(request, 'Edit.html', {'data': employee})
def Delete_Data(request,full_name):
    employee = get_object_or_404(Employee_Data, full_name=full_name)
    employee.delete()
    return redirect('list1')
def viewme(request,full_name):
    employee = get_object_or_404(Employee_Data, full_name=full_name)
    return render(request ,'viewme.html' ,{'data': employee})