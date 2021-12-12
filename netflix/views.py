from .forms import CustomerForm
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'netflix/index.html')

def create_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer added successfully")
            return redirect('index')
        messages.error(request, "Validation failed")
    context = {
        'form': form
    }
    return render(request, 'netflix/customer.html',context)
