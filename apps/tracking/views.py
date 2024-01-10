from django.shortcuts import render,redirect, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse, JsonResponse
from . models import Category, Status, Flow
from . forms import CategoryForm


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