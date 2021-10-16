from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from products.models import Product
from basket.models import Basket

from django.template.loader import render_to_string
from django.http import JsonResponse


@login_required
def basket_add(request, id):
    product = Product.objects.get(id=id)
    basket = Basket.objects.filter(user=request.user, product=product)
    if not basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, id):
    Basket.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, id, quantity):
    final_sum = 0
    final_quantity = 0
    baskets = Basket.objects.filter(user=request.user)
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
            for basket in baskets:
                final_sum += basket.sum()
                final_quantity += basket.quantity
                basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        context = {'baskets': baskets,
                   'final_quantity': final_quantity,
                   'final_sum': final_sum}
        result = render_to_string('basket/basket.html', context)
        return JsonResponse({'result': result})
