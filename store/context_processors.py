from .cart import Cart
from .models import Wishlist

def cart(request):
    return {'cart': Cart(request)}

def wishlist(request):
    if request.user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        return {'wishlist': wishlist}
    return {}