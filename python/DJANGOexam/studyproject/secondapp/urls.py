from django.urls import path
from . import views
urlpatterns = [
    path('', views.exam1, name='exam1'),
    path('exam2/', views.exam2, name='exam2'),
    path('exam2_1/', views.exam2_1, name='exam2_1'),
    path('exam3/', views.exam3, name='exam3'),
    path('exam4/', views.exam4, name='exam4'),
    path('exam5/', views.exam5, name='exam5'),
    path('exam6/', views.exam6, name='exam6'),
    path('exam7/', views.exam7, name='exam7'),
    path('exam8/', views.exam8, name='exam8'),
    path('exam9/', views.exam9, name='exam9'),
    path('exam10/<name>/', views.exam10, name='exam10'),
    path('exam11/<name>/<int:age>', views.exam11, name='exam11'),
    path('exam12/<int:num1>/<int:num2>', views.exam12, name='exam12'),
    path('exam13/', views.exam13, name='exam13'),
    path('exam14/<word>/<int:num1>/<num2>', views.exam14, name='exam14'),
    path('exam15/', views.exam15, name='exam15'),
    path('exam16/', views.exam16, name='unico'),
    path('exam17/', views.exam17, name='exam17'),
    path('exam18/', views.exam18, name='exam18'),
    path('exam19/', views.exam19, name='exam19'),
    path('exam20/', views.exam20, name='exam20'),
    path('exam21/', views.exam21, name='exam21'),
    path('exam22/', views.exam22, name='exam22'),
    path('exam23/', views.exam23, name='exam23'),
    path('exam24/', views.exam24, name='exam24'),
    path('json1/', views.json1, name='json1'),
    path('json2/', views.json2, name='json2'),
    path('json3/', views.json3, name='json3'),
    path('product1/', views.product1, name='product1'),
    path('basket1/', views.basket1, name='basket1'),
    path('product2/', views.product2, name='product2'),
    path('basket2/', views.basket2, name='basket2'),
    path('ggmap1/', views.ggmap1),
    path('ggmap2/', views.ggmap2),
    path('ggmap3/', views.ggmap3),
    path('ggmap4/', views.ggmap4),
    path('ggmap5/', views.ggmap5),
    path('ggmap6/', views.ggmap6),
    path('ggmap7/', views.ggmap7),
    path('kkmap1/', views.kkmap1),
    path('kkmap2/', views.kkmap2),
    path('kkmap3/', views.kkmap3),
    path('kkmap4/', views.kkmap4),
    path('kkmap5/', views.kkmap5),
    path('kkmap6/', views.kkmap6),
    path('kkmap7/', views.kkmap7),
    path('test/', views.test),
]
