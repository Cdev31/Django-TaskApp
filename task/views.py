from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task, Category
from .load_image import load, delete
import datetime

@login_required
def task( request:HttpRequest ):

    task = Task.objects.filter( user=request.user )

    return render( 
        request=request, 
        template_name='task.html', 
        context= {
            'tasks': task
            }
        )

@login_required
def detail_task( request: HttpRequest, id: int ):
    task = get_object_or_404(Task, id=id, user=request.user )
    return render( request=request, 
                   template_name='detail_task.html', 
                   context={
                        'task': task
                    })

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
            url = load( request.FILES.get('taskImage') )
            task = request.POST
            date_completed_str = task.get('date')
            date_completed = timezone.make_aware(datetime.datetime.strptime(date_completed_str, '%Y-%m-%d'))
            category = Category.objects.get( id=int(task.get('category')) )
            new_task = Task( title=task.get('title'), description=task.get('description'),user=request.user,
                            image=url, important_level=task.get('level'), date_completed=date_completed,
                            category=category
                            )
            new_task.save()
            return redirect('/task')
        except Exception as error:
            print(error)
            categories = Category.objects.filter( user= request.user )
            return render( request=request, 
                          template_name='create_task.html',
                            context={
                           'categories': categories,
                           'error': error
                        })

@login_required
def delete_task( request: HttpRequest, id: int ):
    try:
        task = get_object_or_404( Task, pk=id, user=request.user )
        delete( task.image )
        task.delete()
        return redirect('/task/')
    except Exception as err:
        return render( request=request, 
                template_name='task.html', 
                context={
                    'error': err
                }) 

@login_required
def completed_task( request: HttpRequest, id: int ):
    try:
        task = get_object_or_404( Task, pk=id, user=request.user )
        task.done = True
        task.save()
        return redirect('/task/')
    except Exception as err:
        return render( request=request, 
                template_name='task.html', 
                context={
                    'error': err
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
        return redirect('/task/categories/')
    except Exception as err:
        return render( request=request, 
                template_name='categories.html', 
                context={
                    'error': err
                })   


