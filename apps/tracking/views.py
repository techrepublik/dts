from django.shortcuts import render,redirect, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.http import HttpResponseRedirect, JsonResponse
from apps.user.models import Office_User, Office, Office_User_Profile
from . models import Category, Status, Flow, Workflow, Document, Received, Forwarded, Model1, Model2
from . forms import CategoryForm,FlowForm,StatusForm, WorkflowForm, DocumentForm, ForwardedForm, ConfirmReceivedForm, Model2Form, SearchForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


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


#New Documents 2024-02-03 Josh
def get_all_documents(request):
        user=request.GET.get('user')
        print(user)
        if not user: return
        documents = Document.objects.filter(user=user)
        return render(request, "tracking/new_document/documents.html", {'documents':documents})

def add_document(request):
        if(request.method == 'POST'):
                form = DocumentForm(request.POST,)
        else:    
                form = DocumentForm()

        return save_document(request, form, 'tracking/new_document/add-document.html')



def doc_new_forward(request):
        if(request.method == 'POST'):
                form = ForwardedForm(request.POST,)
        else:    
                form = ForwardedForm()

        return save_forwaded(request, form, 'tracking/new_document/doc_forward.html')

def save_forwaded(request, form, template_name):
    data = dict()
    print("1")
    if request.method == 'POST':
        print("2")
        if form.is_valid():
            instance = form.save(commit=False)
            user = Office_User_Profile.objects.all()
            for u in user:
                   if u.user_id == request.user.id:
                        instance.forwarded_from = u.office
                        form.save()
                        data['form_is_valid'] = True
                        data['document_list'] = render_to_string('tracking/new_document/documents-list.html')
        else:
            data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def save_document(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            form.save()
            data['form_is_valid'] = True
            documents= Document.objects.all()
            data['document_list'] = render_to_string('tracking/new_document/documents-list.html', {'documents':documents})
        else:
            data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#_____________________________________________________________________________________________________________

#incoming

#_____________________________________________________________________________________________________________

def incoming(request):
    user_profile = Office_User_Profile.objects.all()
    offices = Office.objects.all()
    forwarded = Forwarded.objects.all()
    received = Received.objects.all()
    return render(request, "tracking/incoming/incoming.html",{'offices':offices,'forwarded':forwarded,'received':received,'user_profile':user_profile})

def confirm_received(request,pk):
        forwarded = get_object_or_404(Forwarded, pk=pk)
        if(request.method == 'POST'):
                form = ConfirmReceivedForm(request.POST, instance=forwarded)
        else:    
                form = ConfirmReceivedForm(instance=forwarded)
        return save_received(request, form, "tracking/incoming/received-doc.html")

def save_received(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.received = True
            form.save()
            data['form_is_valid'] = True
            forwarded= Forwarded.objects.all()
            offices = Office.objects.all()
            user_profile = Office_User_Profile.objects.all()
            data['incoming_list'] = render_to_string("tracking/incoming/incoming-list.html", {'offices':offices,'forwarded':forwarded,'user_profile':user_profile})
        else:
            data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


#_________________________________________________________________________________________________________________
    
#Received
    
#_________________________________________________________________________________________________________________
    

def received_doc(request):
    user_profile = Office_User_Profile.objects.all()
    offices = Office.objects.all()
    forwarded = Forwarded.objects.all()
    received = Received.objects.all()
    return render(request, "tracking/received/received.html",{'offices':offices,'forwarded':forwarded,'received':received,'user_profile':user_profile})


#_________________________________________________________________________________________________________________

#forwarded

#_________________________________________________________________________________________________________________


def forwarded_doc(request):
    user_profile = Office_User_Profile.objects.all()
    offices = Office.objects.all()
    forwarded = Forwarded.objects.all()
    received = Received.objects.all()
    return render(request, "tracking/forwarded/forwarded-doc.html",{'offices':offices,'forwarded':forwarded,'received':received,'user_profile':user_profile})



#______________________________________________________________________________________________________________________________

#track

#______________________________________________________________________________________________________________________________

def tracking(request,pk):
    forwarded =Forwarded.objects.all()
    received =Received.objects.all()
    documents = Document.objects.get(id=pk)
    return render(request, "tracking/track/track-doc.html",{'documents':documents,'forwarded':forwarded, 'received':received})

def tracking_doc_list(request):
    documents = Document.objects.all()
    return render(request, "tracking/track/track-doc-list.html",{'documents':documents})

########################################################################################################

def aaa(request):
      model1_instances = Model1.objects.all()
      return render(request,"try/try_table.html",{'model1_instances':model1_instances} )

def get_model1_data(request, pk):
    instance = get_object_or_404(Model1, pk=pk)
    data = {
        'pk': instance.pk,
        'name': instance.name,  
    }
    return JsonResponse(data)

def create_model2(request):
    if request.method == 'POST':
        form = Model2Form(request.POST)
        if form.is_valid():
            form.save()
            # Handle form submission
            return JsonResponse({'success': True})
        return render(request,"try/try_table.html",{'form':form})
    return JsonResponse({'success': False})

def search(request):
    if 'query' in request.GET:
        query = request.GET['query']
        results = Document.objects.filter(Q(document_title__icontains=query) | Q(document_code__icontains=query))
    else:
        results = []
    return render(request, 'search/search.html', {'results': results})
