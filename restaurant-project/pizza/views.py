from django.shortcuts import render
from .forms import PizzaForm, CustomerForm


def home(request):
    return render(request, "pizza/home.html")


def order(request):
    if request.method == "POST":
        filled_pizza_form = PizzaForm(request.POST)

        if filled_pizza_form.is_valid():
            note = "Thanks for ordering! Your %s %s crust pizza is on its way!" % (
                filled_pizza_form.cleaned_data["size"],
                filled_pizza_form.cleaned_data["crust"],
            )
        else:
            note = "Order was not created, please try again"
        new_pizza_form = PizzaForm()

        return render(
            request,
            "pizza/order.html",
            {
                "pizzaform": new_pizza_form,
                "note": note,
            },
        )
    else:
        form = PizzaForm()
        cust_form = CustomerForm()

        return render(
            request,
            "pizza/order.html",
            {"pizzaform": form, "customerform": cust_form},
        )
