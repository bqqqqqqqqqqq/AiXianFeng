from django.shortcuts import render
from .models import Wheel, Nav, Mustbuy, Shop, MainShow


# Create your views here.

# 主页: home
def home(request):
    wheelList = Wheel.objects.all()  # 轮播数据
    navList = Nav.objects.all()  # 导航数据
    mustbuyList = Mustbuy.objects.all()  # 必购数据
    shopList = Shop.objects.all()  # 便利店数据
    shop1 = shopList[0]
    shop2 = shopList[1:3]
    shop3 = shopList[3:7]
    shop4 = shopList[7:11]
    mainShowList = MainShow.objects.all()  # 主要信息数据
    return render(request, 'axf/home.html', {'title': '主页', 'wheelList': wheelList, 'navList': navList, 'mustbuyList':mustbuyList,'shop1':shop1,'shop2':shop2,'shop3':shop3,'shop4':shop4,'mainList':mainShowList})


# 闪送超市: merket
def market(request):
    return render(request, 'axf/market.html', {'title': '闪送超市'})


# 购物车: cart
def cart(request):
    return render(request, 'axf/cart.html', {'title': '购物车'})


# 我的: mine
def mine(request):
    return render(request, 'axf/mine.html', {'title': '我的'})
