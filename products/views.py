from django.shortcuts import render
# import os
# import json
#
# MODULE_DIR = os.path.dirname(__file__)

# Create your views here.


def index(request):
    context = {'title': 'geekshop'}
    return render(request, 'index.html', context)


def products(request):
    context = {'title': 'catalogue'}
    # path_file = os.path.join(MODULE_DIR, 'fixtures/db.json')
    # context['products'] = json.load(open(path_file, encoding='utf-8'))
    context['products'] = [
      {
        "name": "Худи черного цвета с монограммами adidas Originals",
        "price": "6 090,00 руб.",
        "description": "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
        "image": "/vendor/img/products/Adidas-hoodie.png",
        "to_do": "Отправить в корзину"
      },
      {
        "name": "Синяя куртка The North Face",
        "price": "23 725,00 руб.",
        "description": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
        "image": "/vendor/img/products/Blue-jacket-The-North-Face.png",
        "to_do": "Отправить в корзину"
      },
      {
        "name": "Коричневый спортивный oversized-топ ASOS DESIGN",
        "price": "3 390,00 руб.",
        "description": "Материал с плюшевой текстурой. Удобный и мягкий.",
        "image": "/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png",
        "to_do": "Отправить в корзину"
      },
      {
        "name": "Черный рюкзак Nike Heritage",
        "price": "2 340,00 руб.",
        "description": "Плотная ткань. Легкий материал.",
        "image": "/vendor/img/products/Black-Nike-Heritage-backpack.png",
        "to_do": "Отправить в корзину"
      },
      {
        "name": "Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
        "price": "13 590,00 руб.",
        "description": "Гладкий кожаный верх. Натуральный материал.",
        "image": "/vendor/img/products/Black-Dr-Martens-shoes.png",
        "to_do": "Отправить в корзину"
      },
      {
        "name": "Темно-синие широкие строгие брюки ASOS DESIGN",
        "price": "2 890,00 руб.",
        "description": "Легкая эластичная ткань сирсакер Фактурная ткань.",
        "image": "/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png",
        "to_do": "Отправить в корзину"
      }
    ]
    return render(request, 'products.html', context)


def test(request):
    context = {
        'title': 'geekshop',
        'user': 'Petrov',
        'description': 'Welcome!',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00'},
        ],
        'promotion': True,
        'products_of_promotion': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00'},
        ]
    }
    return render(request, 'test.html', context)
