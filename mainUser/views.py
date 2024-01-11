from django.shortcuts import render, redirect, get_list_or_404
from .models import Item
from .forms import Item_form

# Create your views here.
def Item_list_view(request):
    items = Item.objects.all()
    return render(request, 'Item_list.html',{'items':items})

def Item_detail_view(request, pk):
    item = get_list_or_404(Item, pk=pk)
    print(pk)
    print(item)
    return render(request, 'Item_details.html', {'item':item})

def Item_new_view(request):
    if request.method == 'POST':
        form = Item_form(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Item_list_view', pk=Item.pk)
    else:
        form = Item_form()

    return render(request, 'add_new_item.html', {'form':form})

def Item_delete_view(request, pk):
    item = get_list_or_404(Item, pk=pk)
    item.delete()
    return redirect('Item_list_view')