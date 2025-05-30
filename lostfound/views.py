from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home_view(request):
    items = Item.objects.all()
    return render(request, 'lostfound/home.html', {'items': items})

@login_required
def report_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.reported_by = request.user
            item.user = request.user  # 👈 add this line too
            item.save()

            return redirect('newsfeed')  # change as needed
    else:
        form = ItemForm()
    return render(request, 'lostfound/report.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'lostfound/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'lostfound/login.html', {'error': 'Invalid credentials'})
    return render(request, 'lostfound/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

from django.db.models import Q

def newsfeed_view(request):
    items = Item.objects.all()

    # Search
    query = request.GET.get('q')
    if query:
        items = items.filter(Q(title__icontains=query) | Q(description__icontains=query))

    # Filter by status
    status_filter = request.GET.get('status')
    if status_filter in ['Lost', 'Found']:
        items = items.filter(status=status_filter)

    disposition_filter = request.GET.get('disposition')
    if disposition_filter:
        reports = reports.filter(disposition=disposition_filter)
    return render(request, 'lostfound/newsfeed.html', {'items': items})


def user_dashboard(request):
    user_items = Item.objects.filter(reported_by=request.user).order_by('-date')
    return render(request, 'lostfound/dashboard.html', {'user_items': user_items})


from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Item

@login_required
def report_lost(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.reported_by = request.user
            item.status = 'Lost'
            item.save()
            return redirect('newsfeed')  # 👈 this sends user to the feed
    else:
        form = ReportForm()
    return render(request, 'lostfound/report_form.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm  # assume you have a ModelForm for items

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if item.user == item.reported_by:
        if request.method == 'POST':
            form = ItemForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                return redirect('newsfeed')  # Redirect to newsfeed or detail page
        else:
            form = ItemForm(instance=item)
        return render(request, 'lostfound/edit_item.html', {'form': form})
    return redirect('newsfeed')

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if item.user == item.reported_by:
        item.delete()
    return redirect('newsfeed')

    
