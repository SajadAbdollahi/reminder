from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .forms import FriendForm
from .models import Category, Task

from django.views import View


def indexView(request):
    form = FriendForm()
    friends = Task.objects.all()
    return render(request, "index.html", {"form": form, "friends": friends})


def postFriend(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        _form = FriendForm(request.POST)
        # save the data and after fetch the object in instance
        if _form.is_valid():
            instance = _form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": _form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


# BONUS CBV
def checkNickName(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        title = request.GET.get("title", None)
        # check for the nick name in the database.
        if Task.objects.filter(nick_name=nick_name).exists():
            # if nick_name found return not valid new friend
            return JsonResponse({"valid": False}, status=200)
        else:
            # if nick_name not found, then user can create a new friend.
            return JsonResponse({"valid": True}, status=200)

    return JsonResponse({}, status=400)


class FriendView(View):
    form_class = FriendForm
    template_name = "index.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        friends = Task.objects.all()
        return render(self.request, self.template_name,
                      {"form": form, "friends": friends})

    def post(self, *args, **kwargs):
        # request should be ajax and method should be POST.
        if self.request.is_ajax and self.request.method == "POST":
            # get the form data
            form = self.form_class(self.request.POST)
            # save the data and after fetch the object in instance
            if form.is_valid():
                instance = form.save()
                # serialize in new friend object in json
                ser_instance = serializers.serialize('json', [instance, ])
                # send to client side.
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                # some form errors occured.
                return JsonResponse({"error": form.errors}, status=400)

        # some error occured
        return JsonResponse({"error": ""}, status=400)
