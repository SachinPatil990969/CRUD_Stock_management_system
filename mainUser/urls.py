from django.urls import path
from .views import Item_list_view, Item_detail_view, Item_new_view, Item_delete_view

urlpatterns = [
    path('', Item_list_view, name = 'Item_list_view'),
    path('item/<int:pk>/', Item_detail_view, name = 'Item_detail_view'),
    path('new/', Item_new_view, name = 'Item_new_view'),
    path('item/<int:pk>/delete', Item_delete_view, name ='Item_delete_view')
]
