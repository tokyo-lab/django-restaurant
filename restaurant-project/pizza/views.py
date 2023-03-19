from django.shortcuts import render
from .forms import PizzaForm, CustomerForm


def home(request):
    return render(request, "pizza/home.html")


def order(request):
    if request.method == "POST":
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = "Thanks for ordering! Your %s %s crust pizza is on its way!" % (
                filled_form.cleaned_data["size"],
                filled_form.cleaned_data["crust"],
            )
        else:
            note = "Order was not created, please try again"
        new_form = PizzaForm()
        return render(
            request, "pizza/order.html", {"pizzaform": new_form, "note": note}
        )
    else:
        form = PizzaForm()
        return render(request, "pizza/order.html", {"pizzaform": form})


def customer(request):
    if request.method == "POST":
        filled_form = CustomerForm(request.POST)
        if filled_form.is_valid():
            note = "Name: %s Email: %s " % (
                filled_form.cleaned_data["name"],
                filled_form.cleaned_data["email"],
            )
        else:
            note = "Customer object is not working"
        new_customer = CustomerForm()
        return render(
            request, "pizza/order.html", {"customer": new_customer, "note": note}
        )
    else:
        form = CustomerForm()
        return render(request, "pizza/order.html", {"pizzaform": form})
