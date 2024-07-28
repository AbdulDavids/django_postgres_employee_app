from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm


def index(request):
	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = EmployeeForm()

	employees = Employee.objects.all()
	return render(request, 'index.html', {'form': form, 'employees': employees})


def employee_edit(request, pk):
	employee = get_object_or_404(Employee, pk=pk)
	if request.method == 'POST':
		form = EmployeeForm(request.POST, instance=employee)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = EmployeeForm(instance=employee)
	return render(request, 'index.html', {'form': form, 'employees': Employee.objects.all(), 'editing': pk})


def employee_delete(request, pk):
	employee = get_object_or_404(Employee, pk=pk)
	employee.delete()
	return redirect('index')
