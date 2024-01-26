from django.shortcuts import render,redirect, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.http import HttpResponseRedirect, JsonResponse
from apps.user.models import Office_User, Office, Office_User_Profile
from . models import Category, Status, Flow, Workflow, Document, Received, Forwarded
from . forms import CategoryForm,FlowForm,StatusForm, WorkflowForm, DocumentForm, ForwardedForm, ConfirmReceiveForm


# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')


#________________________________________________________________________________________________________


                        #------------Category Views---------------#

#________________________________________________________________________________________________________
#01/10/2024/julius

def categories(request):
        categories = Category.objects.all()
        return render(request, 'admin_page/category/category.html',{'categories':categories})

def add_category(request):
        if(request.method == 'POST'):
                form = CategoryForm(request.POST)
        else:    
                form = CategoryForm()

        return save_category(request, form, 'admin_page/category/add-category.html')


def edit_category(request,pk):
        category = get_object_or_404(Category, pk=pk)
        if(request.method == 'POST'):
                form = CategoryForm(request.POST, instance=category)
        else:    
                form = CategoryForm(instance=category)
        return save_category(request, form, 'admin_page/category/edit-category.html')


def delete_category(request,pk):
        category = get_object_or_404(Category, pk=pk)
        data = dict()
        if request.method == 'POST':
                category.delete()
                data['form_is_valid'] = True
                categories= Category.objects.all()
                data['category_list'] = render_to_string('admin_page/category/category-list.html',{'categories':categories})
        else:    
                context = {'category':category}
                data['html_form'] = render_to_string('admin_page/category/delete-category.html',
                context,
                request=request)
        return JsonResponse(data)


def save_category(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            categories= Category.objects.all()
            data['category_list'] = render_to_string('admin_page/category/category-list.html', {'categories':categories})
        else:
            data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------Flow Views---------------#

#________________________________________________________________________________________________________
#01/11/2024/julius

def flows(request):
        flows = Flow.objects.all()
        return render(request, 'admin_page/flow/flow.html',{'flows':flows})

def add_flow(request):
        if(request.method == 'POST'):
                form = FlowForm(request.POST)
        else:    
                form = FlowForm()

        return save_flow(request, form, 'admin_page/flow/add-flow.html')


def edit_flow(request,pk):
        flow = get_object_or_404(Flow, pk=pk)
        if(request.method == 'POST'):
                form = FlowForm(request.POST, instance=flow)
        else:    
                form = FlowForm(instance=flow)
        return save_flow(request, form, 'admin_page/flow/edit-flow.html')


def delete_flow(request,pk):
        flow = get_object_or_404(Flow, pk=pk)
        data = dict()
        if request.method == 'POST':
                flow.delete()
                data['form_is_valid'] = True
                flows= Flow.objects.all()
                data['flow_list'] = render_to_string('admin_page/flow/flow-list.html',{'flows':flows})
        else:    
                context = {'flow':flow}
                data['html_form'] = render_to_string('admin_page/flow/delete-flow.html',
                context,
                request=request)
        return JsonResponse(data)


def save_flow(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            flows= Flow.objects.all()
            data['flow_list'] = render_to_string('admin_page/flow/flow-list.html', {'flows':flows})
        else:
            data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------workflow Views---------------#

#________________________________________________________________________________________________________
#01/11/2024/julius

def workflow(request):
        workflow = Workflow.objects.all()
        return render(request, 'admin_page/workflow/workflow.html',{'workflow':workflow})

def add_workflow(request):
        if(request.method == 'POST'):
                form = WorkflowForm(request.POST)
        else:    
                form = WorkflowForm()

        return save_workflow(request, form, 'admin_page/workflow/add-workflow.html')


def edit_workflow(request,pk):
        workflow = get_object_or_404(Workflow, pk=pk)
        if(request.method == 'POST'):
                form = WorkflowForm(request.POST, instance=workflow)
        else:    
                form = WorkflowForm(instance=workflow)
        return save_workflow(request, form, 'admin_page/workflow/edit-workflow.html')


def delete_workflow(request,pk):
        workflow = get_object_or_404(Workflow, pk=pk)
        data = dict()
        if request.method == 'POST':
                workflow.delete()
                data['form_is_valid'] = True
                workflow= Workflow.objects.all()
                data['workflow_list'] = render_to_string('admin_page/workflow/workflow-list.html',{'workflow':workflow})
        else:    
                context = {'workflow':workflow}
                data['html_form'] = render_to_string('admin_page/workflow/delete-workflow.html',
                context,
                request=request)
        return JsonResponse(data)


def save_workflow(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            workflow= Workflow.objects.all()
            data['workflow_list'] = render_to_string('admin_page/workflow/workflow-list.html', {'workflow':workflow})
        else:
            data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------Status Views---------------#

#________________________________________________________________________________________________________
#01/11/2024/julius

def status(request):
        status = Status.objects.all()
        return render(request, 'admin_page/status/status.html',{'status':status})

def add_status(request):
        if(request.method == 'POST'):
                form = StatusForm(request.POST)
        else:    
                form = StatusForm()

        return save_status(request, form, 'admin_page/status/add-status.html')


def edit_status(request,pk):
        status = get_object_or_404(Status, pk=pk)
        if(request.method == 'POST'):
                form = StatusForm(request.POST, instance=status)
        else:    
                form = StatusForm(instance=status)
        return save_status(request, form, 'admin_page/status/edit-status.html')


def delete_status(request,pk):
        status = get_object_or_404(Status, pk=pk)
        data = dict()
        if request.method == 'POST':
                status.delete()
                data['form_is_valid'] = True
                status= Status.objects.all()
                data['status_list'] = render_to_string('admin_page/status/status-list.html',{'status':status})
        else:    
                context = {'status':status}
                data['html_form'] = render_to_string('admin_page/status/delete-status.html',
                context,
                request=request)
        return JsonResponse(data)


def save_status(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            status= Status.objects.all()
            data['status_list'] = render_to_string('admin_page/status/status-list.html', {'status':status})
        else:
            data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#________________________________________________________________________________________________________


                        #------------Document Views---------------#

#________________________________________________________________________________________________________
#01/12/2024/julius

def documents(request): 
    if request.method == "POST" and 'btngenerate' in request.POST:
           form1 = DocumentForm(request.POST)
           if form1.is_valid():
                  form1.save()
                  return render(request, "tracking/document.html")
           
    if request.method == "POST" and 'btnsubmit' in request.POST:
           form2 = ForwardedForm(request.POST)
           if form2.is_valid():
                  form2.save()
                  return render(request, "tracking/document.html")
    else:
           form1 = DocumentForm
           form2 = ForwardedForm
    return render(request, "tracking/document.html",{'form1':form1,'form2':form2})

def received_doc(request):
    user_profile = Office_User_Profile.objects.all()
    offices = Office.objects.all()
    forwarded = Forwarded.objects.all()
    received = Received.objects.all()
    return render(request, "tracking/received-doc.html",{'offices':offices,'forwarded':forwarded,'received':received,'user_profile':user_profile})

def confirm_received(request,pk):
        forwarded = get_object_or_404(Forwarded, pk=pk)
        if(request.method == 'POST'):
                form = ConfirmReceiveForm(request.POST, instance=forwarded)
        else:    
                form = ConfirmReceiveForm(instance=forwarded)
        return save_forwarded(request, form, 'tracking/confirm-received.html')

def save_forwarded(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            status= Forwarded.objects.all()
            data['forwarded_list'] = render_to_string('tracking/incoming-list.html', {'status':status})
        else:
            data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def forwarded_doc(request):
    user_profile = Office_User_Profile.objects.all()
    offices = Office.objects.all()
    forwarded = Forwarded.objects.all()
    received = Received.objects.all()
    return render(request, "tracking/forwarded-doc.html",{'offices':offices,'forwarded':forwarded,'received':received,'user_profile':user_profile})

def incoming_doc(request):
    user_profile = Office_User_Profile.objects.all()
    offices = Office.objects.all()
    forwarded = Forwarded.objects.all()
    received = Received.objects.all()
    return render(request, "tracking/incoming-doc.html",{'offices':offices,'forwarded':forwarded,'received':received,'user_profile':user_profile})

def tracking(request):
    
    return render(request, "tracking/track-doc.html")

def tracking_doc_list(request):
    
    return render(request, "tracking/track-doc-list.html")