from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from .models import *
from universities.models import Unit



# --------------------------------------------------
# ----------- Application Request views ------------
# --------------------------------------------------
def application(request, username):
    user = get_object_or_404(User, username=username)
    application_list = ApplyApplication.objects.filter(user=user).order_by('-creation_date')
    count = ApplyApplication.objects.filter(user=user).order_by('-creation_date').count()
    unread_notification = Notification.objects.filter(receiver=request.user, is_read=False).count()
   
    # paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(application_list, 6)
    try:
        application = paginator.page(page)
    except PageNotAnInteger:
        application = paginator.page(6)
    except EmptyPage:
        application = paginator.page(paginator.num_pages)

    context = {
        'object': application,
        'count': unread_notification,
        'apply_count': count,
    }
    return render(request, 'appliedunis/application_card.html', context)



# --------------------------------------------------
# ----------- Delete Application Request------------
# --------------------------------------------------
def cancelApi(request):
    if request.user.is_authenticated:
        if request.GET.get('unit_id'):
            user = request.user
            unit_id = request.GET.get('unit_id')
            unit_obj = Unit.objects.get(id=unit_id)
            object, created = ApplyApplication.objects.get_or_create(user=user, unit=unit_obj)

            data = dict()
            if not created:
                object.delete()
                data['delete'] = 'success'
                application_list = ApplyApplication.objects.filter(user=user).order_by('-creation_date')
                count = ApplyApplication.objects.filter(user=user).order_by('-creation_date').count()
                unread_notification = Notification.objects.filter(receiver=request.user, is_read=False).count()

                # paginator
                page = request.GET.get('page', 1)
                paginator = Paginator(application_list, 6)
                try:
                    application = paginator.page(page)
                except PageNotAnInteger:
                    application = paginator.page(6)
                except EmptyPage:
                    application = paginator.page(paginator.num_pages)

                data['html_application_list'] = render_to_string(
                    'appliedunis/application_card_list.html', {'object': application}
                    )

            return JsonResponse(data)

    return JsonResponse({'delete': 'error'})



# --------------------------------------------------
# ----------- Add unit to Application --------------
# --------------------------------------------------
def applyApi(request):
    if request.user.is_authenticated:
        if request.GET.get('unit_id'):
            user = request.user

            unit_id = request.GET.get('unit_id')
            unit_obj = Unit.objects.get(id=unit_id)


            object, created = ApplyApplication.objects.get_or_create(user=user, unit=unit_obj)

            json_data = {
                "status": 'success'
            }

            return JsonResponse(json_data)


    return JsonResponse({
        'status': 'error'
    })



# ---------------------------------------------------
# --------Student Profile Notifications Views--------
# ---------------------------------------------------
def notifications(request, username):
    notifications = Notification.objects.filter(receiver=request.user).order_by('-created')
    unread_notification = Notification.objects.filter(receiver=request.user, is_read=False).count()

    context = {
        'notifications': notifications,
        'count': unread_notification,
    }

    return render(request, 'appliedunis/notifications.html', context)


# -------------------------------------------------
# --------- Notification mark as read view --------
# -------------------------------------------------
def markAsRead(request): 
    if request.user.is_authenticated:   
        if request.GET.get('notification_id'):
            notification_id = request.GET.get('notification_id')
            notification_obj = Notification.objects.get(id=notification_id)

            if notification_obj in Notification.objects.all():
                notification_obj.is_read = True
                notification_obj.save()

