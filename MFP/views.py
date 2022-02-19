from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from MFP.models import Meal, Total
from MFP.serializers import TotalSerializer, MealSerializer
from rest_framework.decorators import api_view

from MFP.apps import client

import datetime
import myfitnesspal

@api_view(['GET'])
def totals_list(request):
    totals = Total.objects.all()

    # datefrom = request.GET.get('datefrom', None)
    # if datefrom is not None:
    #     totals = totals.filter()

    totals_serializer = TotalSerializer(totals, many=True)
    return JsonResponse(totals_serializer.data, safe=False)

@api_view(['GET'])
def totals_date(request, date):
    parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    refresh_data = False
    refresh = request.GET.get('refresh_data', None)
    if refresh is not None:
        if refresh.lower() == 'true':
            refresh_data = True
    try:
        totals = Total.objects.get(date=parsed_date)
        if refresh_data:
            day = client.get_date(parsed_date.year, parsed_date.month, parsed_date.day)
            day_totals = day.totals
            total_serializer = TotalSerializer(totals, data=day_totals)
            if total_serializer.is_valid():
                total_serializer.save()
                return JsonResponse(total_serializer.data)
        else:
            total_serializer = TotalSerializer(totals)
            return JsonResponse(total_serializer.data)
    except Total.DoesNotExist:
        day = client.get_date(parsed_date.year, parsed_date.month, parsed_date.day)
        totals = day.totals
        totals['date'] = parsed_date
        total_serializer = TotalSerializer(data=totals)
        if total_serializer.is_valid():
            total_serializer.save()
            return JsonResponse(total_serializer.data)
        return JsonResponse({'message': 'Totals not stored for the date'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def meals_date(request, date):
    parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    inds = ['Breakfast', 'Lunch', 'Dinner', 'Snacks', 'Drinks']
    refresh_data = False
    refresh = request.GET.get('refresh_data', None)
    if refresh is not None:
        if refresh.lower() == 'true':
            refresh_data = True
    meal_type = request.GET.get('type', None)
    try:
        meals = Meal.objects.filter(date=parsed_date)
        if len(meals) > 0:
            if refresh_data:
                day = client.get_date(parsed_date.year, parsed_date.month, parsed_date.day)
                day_meals = day.meals
                data = []
                for i in range(len(day_meals)):
                    day_meal = day_meals[i]
                    print(day_meal)
                    meal_type = inds[i]
                    meal = meals.filter(type__icontains=meal_type)
                    if len(meal) > 0:
                        meal = meal[0]
                        totals = day_meal.totals
                        totals['date'] = parsed_date
                        totals['type'] = meal_type
                        meal_serializer = MealSerializer(meal, data=totals)
                        if meal_serializer.is_valid():
                            meal_serializer.save()
                            print(meal_serializer)
                            data.append(meal_serializer.data)
                    else:
                        totals = day_meal.totals
                        totals['date'] = parsed_date
                        totals['type'] = meal_type
                        meal_serializer = MealSerializer(data=totals)
                        if meal_serializer.is_valid():
                            meal_serializer.save()
                            data.append(meal_serializer.data)
                    print(data)
                return JsonResponse(data, safe=False)
            else:
                meal_serializer = MealSerializer(meals, many=True)
                return JsonResponse(meal_serializer.data, safe=False)
        else:
            day = client.get_date(parsed_date.year, parsed_date.month, parsed_date.day)
            day_meals = day.meals
            data = []
            for i in range(len(day_meals)):
                print(day_meals[i])
                totals = day_meals[i].totals
                print(totals)
                totals['date'] = parsed_date
                totals['type'] = inds[i]
                data.append(totals)
            # totals = day.totals
            # totals['date'] = parsed_date
            print(data)
            meal_serializer = MealSerializer(data=data, many=True)
            if meal_serializer.is_valid():
                meal_serializer.save()
                return JsonResponse(meal_serializer.data, safe=False)
    except Meal.DoesNotExist:
        return JsonResponse({'message': 'Totals not stored for the date'}, status=status.HTTP_404_NOT_FOUND)