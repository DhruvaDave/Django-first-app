from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm,EditProfileForm,MsgEditForm,MessageForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse

from .models import Message


# Create your views here.
def home(request):
    # return HttpResponse('Home Page !')
    return render(request,'user_account/login.html')

def register(request):
    print("---reg---")
    if request.method == 'POST':
        print("--post----")
        form = RegistrationForm(request.POST)
        print("---form----",form.errors)
        print("---form----",form.is_valid())
        if form.is_valid():
            print("---valid")
            form.save()
            print("---save---")
            return redirect('/user_account')
    else:
        print("--else-----")
        form = RegistrationForm()

        args = {'form':form}
        return render(request,'user_account/reg_form.html',args)

def view_profile(request):
    args = {'user':request.user}
    return render(request,'user_account/profile.html',args)

def all_profile(request):
    # print("--------User.objects------",User.objects.all())
    all_profile_list = User.objects.all()
    output = ', '.join([q.username for q in all_profile_list])
    # print("---output--------",output)
    return render(request, "user_account/view.html", {"all_profile_list":all_profile_list})
    return HttpResponse(output)

# def detail(request, user_id):
#     return HttpResponse("You're looking at question %s." % user_id)

def index_profile(request, id):
	ls = User.objects.get(id=id)

	# if request.method == "POST":
	# 	if request.POST.get("save"):
	# 		for item in ls.item_set.all():
	# 			p = request.POST
				
	# 			if "clicked" == p.get("c"+str(item.id)):
	# 				item.complete = True
	# 			else:
	# 				item.complete = False

	# 			if "text" + str(item.id) in p:
	# 				item.text = p.get("text" + str(item.id))


	# 			item.save()

	# 	elif request.POST.get("add"):
	# 		newItem = request.POST.get("new")
	# 		if newItem != "":
	# 			ls.item_set.create(text=newItem, complete=False)
	# 		else:
	# 			print("invalid")

	return render(request, "user_account/index.html", {"ls": ls})

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


def all_msg(request):
    # print("--------User.objects------",User.objects.all())
    all_msg_list = Message.objects.all()
    output = ', '.join([q.user_messsage for q in all_msg_list])
    # print("---output--------",output)
    return render(request, "user_account/view_msg.html", {"all_msg_list":all_msg_list})
    # return HttpResponse(output)

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
    # if this is a POST request we need to process the form data
    print("----------eidt-------msg----",user_id)
    item = Message.objects.get(pk=user_id)
    print("---item---------",item)
    print("---requ---------",request.user)
    if request.method == 'POST':
        print("===========superuser========",request.user.is_superuser)
        if request.user == item.user_id or request.user.is_superuser:
            print("--------match--------")
        # create a form instance and populate it with data from the request:
            form = MsgEditForm(request.POST)

            # check whether it's valid:
            if form.is_valid():
                print("--valid-------")
                # obj = Message()
                item.user_messsage = form.cleaned_data['user_messsage']
                item.save()
                

                # user_messsage = form.cleaned_data.get('user_messsage')
                # user_id = form.cleaned_data.get('user_id')
                # user_data = Message(user_id=user_id,user_messsage=user_messsage)
                # user_data.save()
                # print("------user_data-------",user_data)
                # doc = form.save(commit=False)
                # doc.username = user_id
                # doc.save()

                # selected_user_id = form.cleaned_data.get('user_id')
                # form.save()
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return redirect('/user_account/all/msg')
        else :
            return HttpResponse("You can edit only your messages!!!")
    # if a GET (or any other method) we'll create a blank form
    else:
        # form = MsgEditForm(user=request.user)
        form = MsgEditForm()
    
    return render(request, 'user_account/edit_msg.html', {'form': form})