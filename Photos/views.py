from django.shortcuts import render,redirect
from . models import Category,Imageadd
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# Create your views here.

def loginUser(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('gallery')
    return render(request,'loginregister.html',{'page':page})

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, username=user.username, password=request.POST['password1'])

            if user is not None:
                login(request, user)
                return redirect('gallery')

    context = {'form': form,'page': page}
    return render(request, "loginregister.html", context)

@login_required(login_url='login')
def gallery(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        images = Imageadd.objects.filter(category__user=user)
    else:
        images = Imageadd.objects.filter(category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'images': images}
    return render(request,"gallery.html", context)

@login_required(login_url='login')
def add(request):
    user = request.user
    categories = user.category_set.all()

    if request.method == "POST":
        data = request.POST
        image = request.FILES.getlist('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['new_category'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['new_category'])
        else:
            category = None

        for img in image:
            photo = Imageadd.objects.create(
                title=data['title'],
                category=category,
                image=img,
            )
        return redirect('gallery')
    context = {'categories':categories}
    return render(request, "add.html", context)

@login_required(login_url='login')
def viewimage(request, pk):
    images=Imageadd.objects.get(id=pk)
    return render(request, 'view.html', {'images': images})

@login_required(login_url='login')
def deleteimage(request, pk):
    items = Imageadd.objects.get(id=pk)

    if request.method == "POST":
        items.delete()
        return redirect('gallery')
    return render(request, 'delete.html', {'items':items})

def aboutsite(request):
    return render(request, 'about.html')

