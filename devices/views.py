from django.shortcuts import render, get_object_or_404
from .models import Device, Category
from django import forms
from django.shortcuts import redirect
from .forms import ReviewForm

def device_list(request):
    devices = Device.objects.all()
    return render(request, 'devices/device_list.html', {'devices': devices})

def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    return render(request, 'devices/device_detail.html', {'device': device})

def device_by_category(request, category_id):
    devices = Device.objects.filter(category_id=category_id)
    return render(request, 'devices/device_list.html', {'devices': devices})


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'manufacturer', 'price', 'release_date', 'image', 'category', 'features']

def device_create(request):
    if request.method == "POST":
        form = DeviceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm()
    return render(request, 'devices/device_form.html', {'form': form})


def device_delete(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == "POST":
        device.delete()
        return redirect('device_list')
    return render(request, 'devices/device_confirm_delete.html', {'device': device})



def add_review(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.device = device
            review.save()
            return redirect('device_detail', pk=device.id)
    else:
        form = ReviewForm()
    return render(request, 'devices/add_review.html', {'form': form, 'device': device})