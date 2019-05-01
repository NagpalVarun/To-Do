from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def homepage(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items=List.objects.all
			messages.success(request, ('Item Has Been Added To List!'))
			return render(request, 'homepage.html', {'all_items': all_items})
	else:		
		all_items=List.objects.all
		return render(request, 'homepage.html', {'all_items': all_items})

def about(request):
	return render(request, 'about.html', {})

def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	return redirect('homepage')

def cross_off(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('homepage')

def uncross(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('homepage')

def edit(request, list_id):
	if request.method == 'POST':
		item = List.objects.get(pk=list_id)
		form = ListForm(request.POST or None, instance=item)
		if form.is_valid():
			form.save()
			messages.success(request,('Item Has Been Edited!'))
			return redirect('homepage')
	else:		
		item=List.objects.get(pk=list_id)
		return render(request, 'edit.html', {'item': item})