from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm,EditProfileForm,MsgEditForm,MessageForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse

from .models import Message


# Create your views here.
def home(request):
    return render(request,'user_account/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user_account')
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request,'user_account/reg_form.html',args)

def view_profile(request):
    args = {'user':request.user}
    return render(request,'user_account/profile.html',args)

def all_profile(request):
    all_profile_list = User.objects.all()
    output = ', '.join([q.username for q in all_profile_list])
    return render(request, "user_account/view.html", {"all_profile_list":all_profile_list})

def index_profile(request, id):
	ls = User.objects.get(id=id)
	return render(request, "user_account/index.html", {"ls": ls})


def all_msg(request):
    all_msg_list = Message.objects.all()
    output = ', '.join([q.user_messsage for q in all_msg_list])
    return render(request, "user_account/view_msg.html", {"all_msg_list":all_msg_list})

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/user_account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request,'user_account/edit_profile.html',args)

def edit_msg(request,user_id):
    item = Message.objects.get(pk=user_id)
    if request.method == 'POST':
        if request.user == item.user_id or request.user.is_superuser:
        # create a form instance and populate it with data from the request:
            form = MsgEditForm(request.POST)

            # check whether it's valid:
            if form.is_valid():
                item.user_messsage = form.cleaned_data['user_messsage']
                item.save()
               
                return redirect('/user_account/all/msg')
        else :
            return HttpResponse("You can edit only your messages!!!")
    else:
        form = MsgEditForm()
    
    return render(request, 'user_account/edit_msg.html', {'form': form})