from django.shortcuts import render
from .views import CustomerForm

# Create your views here.

def create_customer(request):
    form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form  })
