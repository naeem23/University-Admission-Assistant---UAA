from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from .models import InterestedUni
from appliedunis.models import Notification
from universities.models import Unit
from datetime import datetime, timezone


# interested university list
def interestedUnis(request, username):
    user = get_object_or_404(User, username=username)
    interestedUnis = InterestedUni.objects.get(user=user)
    unread_notification = Notification.objects.filter(receiver=request.user, is_read=False).count()

    context = {
        'object': interestedUnis,
        'count': unread_notification
    }
    return render(request, 'interestedunis/list.html', context)


# apply function
def ApiRemoveInterested(request):
    if request.user.is_authenticated:
        user = request.user
        interested_unis = InterestedUni.objects.get(user=user)

        data = dict()
        if request.GET.get('unit_id'):
            unit_id = request.GET.get('unit_id')
            unit_obj = Unit.objects.get(id=unit_id)
            
            if unit_obj in interested_unis.units.all():
                interested_unis.units.remove(unit_obj)
                data['remove'] = 'success'
                interested_unis = InterestedUni.objects.get(user=user)
                data['html_interested_list'] = render_to_string(
                    'interestedunis/interested_list.html', {'object': interested_unis}
                    )

            return JsonResponse(data)


    return JsonResponse({
        'remove': 'error'
    })



# apply function
def AddInterestedApi(request):
    if request.user.is_authenticated:
        user = request.user
        interested_unis = InterestedUni.objects.get(user=user)

        if request.GET.get('unit_id'):
            unit_id = request.GET.get('unit_id')
            unit_obj = Unit.objects.get(id=unit_id)
            
            if unit_obj not in interested_unis.units.all():
                interested_unis.units.add(unit_obj)

            json_data = {
                "added": 'success'
            }

            return JsonResponse(json_data)


    return JsonResponse({
        'added': 'error'
    })

