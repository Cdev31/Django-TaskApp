from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, Category
from .load_image import load

@login_required
def task( request:HttpRequest ):
    return render( 
        request=request, 
        template_name='task.html', 
        context= {
            'tasks': [
                {
                    'id':1
                },
                {
                    'id':2
                },
                {
                    'id':3
                },
                {
                    'id':4
                }
            ]
          }
        )

@login_required
def detail_task( request, id ):
    newTask = {}
    tasks = [
        { 'id':1, 'desc': 'comp1' },
        { 'id':2, 'desc': 'comp2' },
        { 'id':3, 'desc': 'comp3' },
        { 'id':4, 'desc': 'comp4' }
    ]
    for task in tasks:
        if task['id'] == id:
            newTask.update(task)
            break
    return render( request, 'detail_task.html', {
        'task': newTask
    } )

@login_required
def create( request: HttpRequest ):
    if request.method == 'GET':
        categories = Category.objects.filter( user= request.user )
        return render( request=request, 
                       template_name='create_task.html',
                       context={
                           'categories': categories
                       }
                        )
    elif request.method == 'POST':
        try:
            url = load( request.FILES['taskImage'] )
            task = request.POST
            new_task = Task( title=task['title'], description=task['description'],
                            image= url, important_level=task['level'], date_completed=task['date'],
                            category=task['category']
                            )
            new_task.save()
            redirect('/task')
        except:
            return render( request=request, 
                          template_name='create_task.html',
                            context={
                           'categories': categories,
                           'error': 'Campos invalidos'
                        })




@login_required
def categories( request: HttpRequest ):
    categories = Category.objects.filter( user= request.user )
    try:
        return render( request=request, template_name='categories.html' , context={
        'categories': categories
        })
    except Exception as error:
        return render( request=request, template_name='categories.html' , context={
        'error': error
        })



@login_required
def create_category( request: HttpRequest ):
    if request.method == 'GET':
        return render( request=request, template_name='create_category.html')
    elif request.method == 'POST':
        try:
            category = request.POST
            if len( category['category_name'] ) == 0 or len( category['description'] ) == 0:
                return render( request=request,
                              template_name='create_category.html',
                              context={
                                  'error': 'Campos vacios invalidos'
                              })
            new_category = Category( 
                category_name=category['category_name'], 
                description=category['description'],
                user=request.user )
            new_category.save()
            if new_category != None:
                return redirect('/task/categories') 
        except Exception as err:    
            return render( request=request, 
                          template_name='create_category.html', 
                          context={
                              'error': err
                          })
        
@login_required
def delete_category( request: HttpRequest, id: int ):

    try:
        category = get_object_or_404( Category, pk=id, user=request.user )
        category.delete()
        redirect('/task/categories/')
    except Exception as err:
        render( request=request, 
                template_name='categories.html', 
                context={
                    'error': err
                })
    redirect('/task')    


