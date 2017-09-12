from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
#from main_app.forms import RegistrationForm
from django.contrib.auth.decorators import user_passes_test
from .forms import RegistrationForm


# доступ у админке только суперпользователю
# @user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    users = User.objects.all()
    #user_form = RegistrationForm()

    return render(request, 'admin_page.html', {'users': users})

def view_user(request, user_id):
	user = User.objects.get(pk=user_id)
	return render(request, 'admin_view_user.html', {'user':user})

#Переделать удаление, добавить подтверждение удаления
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/my_admin')

def create_user(request):
	if request.method=='POST':
		form = RegistrationForm(request.POST)
		if form.is_valid:
			form.save()
			return HttpResponseRedirect('/my_admin')
		else:
			return render(request, 'admin_create_user.html', {'form':form})
	else:
		form = RegistrationForm()
		return render(request, 'admin_create_user.html', {'form':form})


def update_user(request, user_id):
	user = get_object_or_404(User, id=user_id)
	if request.method=='POST':
		form = RegistrationForm(request.POST, isinstance=user)
		if form.is_valid:
			form.save()
			return HttpResponseRedirect('/my_admin')
		else:
			pass
			#Тут остановился!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	else:
		pass
