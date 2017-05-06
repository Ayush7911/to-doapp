from django.shortcuts import render, redirect
from django.utils import timezone
from todos.models import Todo


	
# Create your views here.
def index(request):
	
	items = Todo.objects.all()
	
	return render(request, 'index.html', {'items': items})

def create(request):
	return render(request, 'create.html')
	
def contact(request):
	return render(request, 'contact.html')

def about(request):
	return render(request, 'about.html')

def save(request):
    # Get the form data from the request.
    title = request.POST.get('title')
    description = request.POST.get('description')

    # Create a new todo item with the data.
    Todo.objects.create(
        title=title,
        description=description,
        created_at=timezone.now()
    )

    # Redirect back to index page
    return redirect('index')

def edit(request, id):
	print('Received Id =' +str(id))
	return render(request, 'create.html')