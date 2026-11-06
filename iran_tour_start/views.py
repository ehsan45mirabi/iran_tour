from django.shortcuts import render, redirect
from .models import card_tour, Category, Person

from django.core.paginator import Paginator


from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):

    # card_tours = card_tour.objects.all()[:5]
    q = request.GET.get('q', '')
    card_tours = (card_tour.objects.all() if q == '' else card_tour.objects.filter(title__icontains=q))[:5]
    context = {
        'card_tours' : card_tours
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def details(requets, pk):
    details = card_tour.objects.get(id=pk)
    context = {
        'details' : details
    }
    return render(requets, 'detales.html', context)

def login_register(request):

    if request.method == 'POST':
        if request.POST.get('type') == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username = username , password = password)

            if user is not None:
                login(request, user)
                messages.success(request, 'با موفقیت وارد شدین ')
                return redirect('home_url')
            else:
                messages.error(request, 'ورود موفق نبود مجدد تلاش کنید ')
                return redirect('login_register_url')
            

        else:
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                x = Person.objects.create(
                    username = username,
                    email = email,
                    phone = phone,
                    password = password2
                )
                x.set_password(password2)
                x.save()
                messages.success(request, 'موفقیت امیز بود برای ادامه روی وارد شوید بزنید')
                return redirect('login_register_url')
            else:
                messages.error(request, 'error')
                return redirect('login_register_url')
    
    return render(request, 'auth.html')




def maghsad(request):
    q = request.GET.get('q', '')
    card_tours = card_tour.objects.all().order_by('-id')
    if q:
        card_tours = card_tours.filter(title__icontains=q)

    city = request.GET.get('city', '')
    if city:
        card_tours = card_tours.filter(city__title=city)

    paginator = Paginator(card_tours, 8)   # تعداد کارت در هر صفحه
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'Categorys': Category.objects.all(),
        'card_tours': page_obj,
        'page_obj': page_obj,
        'q': q,
        'city' : city
    }
    return render(request, 'maghsad.html', context)






# def maghsad(request):
#     # card_tours = card_tour.objects.all()

    
#     q = request.GET.get('q') if request.GET.get('q') is not None else ''
#     card_tours = card_tour.objects.all() if q=='' else card_tour.objects.filter(title__icontains=q)
    
#     Categorys = Category.objects.all()

#     context = {
#         'Categorys' : Categorys,
#         'card_tours' : card_tours,
#     }

#     return render(request, 'maghsad.html', context)