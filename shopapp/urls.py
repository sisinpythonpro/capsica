from django.urls import path
from . import views
app_name='shopapp'
urlpatterns=[
    path('',views.All_Prod_Cat,name='All_Prod_Cat'),
    path('<slug:c_slug>/',views.All_Prod_Cat,name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>', views.Prod_Detail, name='Prod_Cat_Detail')
]