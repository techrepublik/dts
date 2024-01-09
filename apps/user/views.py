from django.shortcuts import render,redirect, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse, JsonResponse
from .forms import LoginForm, SignUpForm,AdminSignUpForm, AgencyForm
from django.contrib.auth import authenticate, login
from .models import Office_User, Office_User_Profile,Agency

# Create your views here.


def office_user_index(request,):
    # Page from the theme 
    return render(request, 'index.html')

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('/admin')
            elif user is not None and user.is_staff and not user.is_superuser and not user.office_user:
                login(request, user)
                return redirect('agency-list')
            elif user is not None and user.office_user:
                login(request, user)
                return redirect('officeUser-index')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'accounts/login.html', {'form': form, 'msg': msg})



def office_user_signup(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            return redirect("login")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

def admin_user_signup(request):
    msg = None
    success = False

    if request.method == "POST":
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            return redirect("login")

        else:
            msg = 'Form is not valid'
    else:
        form = AdminSignUpForm()

    return render(request, "accounts/reg_admin.html", {"form": form, "msg": msg, "success": success})

def agency_list(request):

    return render(request, 'admin_page/agency_list.html')

def office_user_profile(request):
    office_user = Office_User_Profile.objects.all()

    return render(request, 'user/edit_profile.html',{'office_user':office_user})


#________________________________________________________________________________________________________


                        #------------Agency Views---------------#

#________________________________________________________________________________________________________


def agencies(request):
        agencies = Agency.objects.all()
        return render(request, 'tracking/agency/agency.html',{'agencies':agencies})

def add_agency(request):
        if(request.method == 'POST'):
                form = AgencyForm(request.POST)
        else:    
                form = AgencyForm()

        return save_agency(request, form, 'tracking/agency/add-agency.html')


def edit_agency(request,pk):
        agency = get_object_or_404(Agency, pk=pk)
        if(request.method == 'POST'):
                form = AgencyForm(request.POST, instance=agency)
        else:    
                form = AgencyForm(instance=agency)
        return save_agency(request, form, 'tracking/agency/edit-agency.html')


def delete_agency(request,pk):
        agency = get_object_or_404(Agency, pk=pk)
        data = dict()
        if request.method == 'POST':
                agency.delete()
                data['form_is_valid'] = True
                agencies= Agency.objects.all()
                data['agency_list'] = render_to_string('tracking/agency/agency-list.html',{'agencies':agencies})
        else:    
                context = {'agency':agency}
                data['html_form'] = render_to_string('tracking/agency/delete-agency.html',
                context,
                request=request)
        return JsonResponse(data)


def save_agency(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            agencies= Agency.objects.all()
            data['agency_list'] = render_to_string('tracking/agency/agency-list.html', {'agencies':agencies})
        else:
            data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)