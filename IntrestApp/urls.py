from django.urls import path

from.import views

urlpatterns=[
    path('',views.Intrestcalculateview),
    path('Intrest/',views.Intrestview),
    path('Compound/',views.compoundview)
]