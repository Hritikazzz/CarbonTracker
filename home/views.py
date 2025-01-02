from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.decorators import login_required
from .models import CarbonFootprint
from django.db.models import Sum
import datetime
from .utils.carbon_sutra import get_electricity_emission

# Create your views here.
def index(request):
    context={
        'variable':"this is sent"
    }
    return render(request, "index.html",context)
def about(request):
    return render(request, "about.html")
    #return HttpResponse("this is about page")

def save_carbon_footprint(request):
    if request.method == "POST":
        electricity = float(request.POST.get("electricity", 0))
        natural_gas = float(request.POST.get("natural_gas", 0))
        heating_oil = float(request.POST.get("heating_oil", 0))
        coal = float(request.POST.get("coal", 0))
        lpg = float(request.POST.get("lpg", 0))
        propane = float(request.POST.get("propane", 0))
        wood = float(request.POST.get("wood", 0))

        # Get estimated emissions from Carbon Sutra API
        electricity_emissions = get_electricity_emission(electricity)

        # Calculate total emissions
        total_emissions = (
            electricity_emissions +
            natural_gas * 0.2 +
            heating_oil * 2.5 +
            coal * 2.86 +
            lpg * 1.51 +
            propane * 1.54 +
            wood * 1.65
        )

        # Save to database
        CarbonFootprint.objects.create(
            user=request.user,
            electricity=electricity,
            natural_gas=natural_gas,
            heating_oil=heating_oil,
            coal=coal,
            lpg=lpg,
            propane=propane,
            wood=wood,
            total_footprint=total_emissions
        )

        messages.success(request, "Your carbon footprint has been calculated and saved!")
        return redirect("dashboard")
    return render(request, "services.html")

def dashboard(request):
    user = request.user

    # Aggregate monthly data
    monthly_data = (
        CarbonFootprint.objects.filter(user=user)
        .values("date__month")
        .annotate(total=Sum("total_footprint"))
    )

    # Aggregate yearly data
    yearly_data = (
        CarbonFootprint.objects.filter(user=user)
        .values("date__year")
        .annotate(total=Sum("total_footprint"))
    )

    # Latest carbon footprint data for chart
    latest_record = CarbonFootprint.objects.filter(user=user).last()
    carbon_data = {
        "electricity": latest_record.electricity if latest_record else 0,
        "natural_gas": latest_record.natural_gas if latest_record else 0,
        "heating_oil": latest_record.heating_oil if latest_record else 0,
        "coal": latest_record.coal if latest_record else 0,
        "lpg": latest_record.lpg if latest_record else 0,
        "propane": latest_record.propane if latest_record else 0,
        "wood": latest_record.wood if latest_record else 0,
        "total_footprint": latest_record.total_footprint if latest_record else 0,
    }

    return render(request, "dashboard.html", {
        "monthly_data": monthly_data,
        "yearly_data": yearly_data,
        "carbon_data": carbon_data
    })



def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")

    return render(request, "contact.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})