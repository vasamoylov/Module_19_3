from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse
from .models import Buyer, Game

users = ['Vasya', 'Alex', 'Pavel', 'Elena', 'Mike']


# Create your views here.
def wellcome(request):
    return render(request, 'main_page.html')


def games(request):
    games_list = Game.objects.all()
    context = {'games_list': games_list}
    return render(request, 'games.html', context)


def cart(request):
    return render(request, 'cart.html')


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                return HttpResponse('Пароли не совпадают')
            elif age < 18:
                return HttpResponse('Вы должны быть старше 18')
            elif Buyer.objects.filter(name=username).exists():
                return HttpResponse('Пользователь уже существует')
            else:
                Buyer.objects.create(name=username, balance=0.00, age=age)
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})
