from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {
        'pagename': 'Glavna stranica',
        'menu': ['Glavna', 'Prodavnica', 'Korpa'],
        'content': 'Dobrodošli na UrbanDjango sajt!',
    })

def products(request):
    products_list = [
        {'name': 'Atomic Heart', 'price': 31, 'description': 'Futuristička igra'},
        {'name': 'Cyberpunk 2077', 'price': 50, 'description': 'RPG igra'},
        {'name': 'PayDay 2', 'price': 20, 'description': 'Akciona igra'},
    ]
    return render(request, 'products.html', {
        'pagename': 'Igre',
        'menu': ['Glavna', 'Prodavnica', 'Korpa'],
        'products': products_list,
    })

def cart(request):
    return render(request, 'cart.html', {
        'pagename': 'Korpa',
        'menu': ['Glavna', 'Prodavnica', 'Korpa'],
        'content': 'Vaša korpa je trenutno prazna.',
    })
