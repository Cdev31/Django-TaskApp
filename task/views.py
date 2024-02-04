from django.shortcuts import render
from django.http import HttpRequest

def task( request:HttpRequest ):
    return render( 
        request=request, 
        template_name='task.html', 
        context= {
            'tasks': [1,2,3,4,5,6,7,8,9,10]
          }
        )
