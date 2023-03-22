from django.shortcuts import render
from .forms import PizzaForm, CustomerForm, MultiplePizzaForm
from django.forms import formset_factory


def home(request):
    return render(request, "pizza/home.html")


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == "POST":
        filled_pizza_form = PizzaForm(request.POST)
        if filled_pizza_form.is_valid():
            filled_pizza_form()
            note = "Thanks for ordering! Your %s %s crust pizza is on its way!" % (
                filled_pizza_form.cleaned_data["size"],
                filled_pizza_form.cleaned_data["crust"],
            )
            new_pizza_form = PizzaForm()
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
            {
                "pizzaform": form,
                "customerform": cust_form,
                "multiple_form": multiple_form,
            },
        )


def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data["number"]
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == "POST":
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data["topping1"])
            note = "Pizzas have been ordered!"
        else:
            note = "Order was not created, please try again"
        return render(request, "pizza/pizzas.html", {"note": note, "formset": formset})
    else:
        return render(request, "pizza/pizzas.html", {"formset": formset})
