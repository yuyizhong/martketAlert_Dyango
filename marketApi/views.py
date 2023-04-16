from django.shortcuts import render, redirect

from .models import Trade
from .forms import TickerForm

# read


def get_ticker(request):
    context = {'data_read': Trade.objects.all()}
    return render(request, 'marketApi/market_ticker_read.html', context)

# create


def create_ticker(request):
    if request.method == "POST":
        form = TickerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = TickerForm()
        return render(request, "marketApi/market_ticker_form.html", {'form': form})
