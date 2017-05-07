from django.shortcuts import render,redirect
from django.http import HttpResponse
from todos.models import Todo 
from django.utils import timezone
from django.contrib import messages
#from django.views.generic import TemplateView
# Create your views here.


def index(request):
	context = {
	'app_title':'TodoApp'
	}
	items = Todo.objects.all()	
	return render(request, 'index.html', {'items':items})


def create(request):
	return render(request, 'create.html', {'form_type': 'create'})
	#return HttpResponse('this should display the create form.')


def contact(request):
	return render(request, 'contact.html')
	

def about(request):
	return render(request, 'about.html')

def save(request):
	
	title = request.POST.get('title')
	description = request.POST.get('description')
	
	form_type = request.POST.get('form_type')
	id = request.POST.get('id')

	# Validation logic
	if title is None or title.strip() == '':
		messages.error(request, 'Item not saved. Please provide the title.')
		return redirect(request.META.get('HTTP_REFERER'))
	

	if form_type == 'create' :
		Todo.objects.create(title = title,
						description = description,
						
						created_at = timezone.now()
						)
      
    
	
	elif form_type == 'edit' and id.isdigit():
		todo = Todo.objects.get(pk=id)
		todo.title = title
		todo.description = description

		todo.save()
		print('Todo updated: ', todo.__dict__)

	# Add save success message
	messages.success(request, 'Todo Item Saved.')

	
	return redirect('index')

def edit(request,id):
	print('go id: ' , str(id))
	todo = Todo.objects.get(pk = id)
	print('Got todo item: ', todo.__dict__)

	return render(request,'create.html', { 'form_type': 'edit', 'todo' :todo})

def remove(request,id):
	form_type = 'remove'
	if form_type == 'remove' and id.isdigit():
		todo = Todo.objects.get(pk=id).delete()


	return redirect('index')

