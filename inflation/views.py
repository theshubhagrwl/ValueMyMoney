from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import random as re


def Home(request):
    return render(request, 'inflation/index.html')


def graph(request):

    def getRandomColour():
        color = 'hsl(' + str(re.randint(1, 360)) + ", 100%, 75%)"
        return color

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    amount = request.GET.get('amount')

    year_list = []
    color_list = []
    for i in range(int(start_date), int(end_date)+1):
        year_list.append(i)
        color_list.append(getRandomColour())
    principal_amt = float(amount)

    start_date = start_date + "-12-" + "31"
    end_date = end_date + "-12-" + "31"
    final_amount = 0

    df = pd.read_csv('static/india-cpi.csv')
    df = df.set_index("date")

    inflation_list = list(df.loc[start_date:end_date, " inflation-rate"])

    list_for_p = []
    for item in inflation_list:
        principal_amt += principal_amt*(item/100)
        list_for_p.append(principal_amt)

    final_amount += principal_amt

    zipped_date = zip(year_list, list_for_p, inflation_list)

    context = {
        'start_date': start_date,
        'end_date': end_date,
        'amount': amount,
        'final_amount': final_amount,
        'yearly_list': list_for_p,
        'year_list': year_list,
        'zipped_data': zipped_date,
        'inflation_list': inflation_list,
        'color_list': color_list,
    }
    return render(request, 'inflation/graph.html', context)
