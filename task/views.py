from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
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


def create( request: HttpRequest ):
    if request.method == 'GET':
        return render( request=request, template_name='create_task.html' )
    elif request.method == 'POST':
       print(  load( file = request.FILES['taskImage'] ) )