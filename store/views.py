from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, reverse
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import Game, Genre, Order, OrderItem, Wishlist
from .forms import AddToCartForm
from .cart import Cart
from django.http import HttpResponseRedirect


class GameListView(ListView):
    model = Game
    template_name = 'store/game_list.html'
    context_object_name = 'games'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset().filter(available=True)
        genre_slug = self.kwargs.get('genre_slug')
        search_query = self.request.GET.get('search')

        if genre_slug:
            genre = get_object_or_404(Genre, slug=genre_slug)
            queryset = queryset.filter(genres=genre)

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(developer__name__icontains=search_query))

        return queryset.select_related('developer').prefetch_related('genres')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context


class GameDetailView(DetailView):
    model = Game
    template_name = 'store/game_detail.html'
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddToCartForm()
        return context

@login_required
def order_create(request):
    cart = Cart(request)

    if not cart:
        messages.warning(request, 'Ваша корзина пуста')
        return redirect('game_list')

    order = Order.objects.create(user=request.user)

    for item in cart:
        OrderItem.objects.create(
            order=order,
            game=item['game'],
            price=item['price'],
            quantity=item['quantity']
        )

    cart.clear()
    messages.success(request, 'Заказ успешно оформлен')
    return render(request, 'store/order_created.html', {'order': order})


def api_games(request):
    games = Game.objects.filter(available=True).values('id', 'title', 'price', 'image')
    return JsonResponse(list(games), safe=False)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '✅ Вы успешно зарегистрировались!')
            return redirect('store:game_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'❌ {error}')
    else:
        form = RegisterForm()
    return render(request, 'store/auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'👋 Добро пожаловать, {username}!')
                return redirect('store:game_list')
        messages.error(request, '❌ Неверный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'store/auth/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('store:game_list')

# Корзина
@login_required
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'store/cart.html', {'cart': cart})

@require_POST
@login_required
def cart_add(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(game=game, quantity=quantity)
    return redirect('store:cart_detail')

@login_required
def cart_remove(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    cart.remove(game)
    return redirect('store:cart_detail')

@require_POST
@login_required
def cart_update(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(game=game, quantity=quantity, update_quantity=True)
    return redirect('store:cart_detail')

# Избранное
@login_required
def add_to_wishlist(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if game in wishlist.games.all():
        wishlist.games.remove(game)
        messages.success(request, f'Игра "{game.title}" удалена из избранного')
    else:
        wishlist.games.add(game)
        messages.success(request, f'Игра "{game.title}" добавлена в избранное')

    # Перенаправляем обратно на предыдущую страницу
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('store:game_list')))


@login_required
def remove_from_wishlist(request, game_id):
    wishlist = get_object_or_404(Wishlist, user=request.user)
    game = get_object_or_404(Game, id=game_id)
    wishlist.games.remove(game)
    messages.success(request, f'Игра "{game.title}" удалена из избранного')
    return redirect('store:wishlist')


@login_required
def wishlist_view(request):
    wishlist = get_object_or_404(Wishlist, user=request.user)
    return render(request, 'store/wishlist.html', {'wishlist': wishlist})