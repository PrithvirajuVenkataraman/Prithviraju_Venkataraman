from django.shortcuts import render

def contact_list(request):
    return render(request, 'contact_details/contact_list.html')

def contact_detail(request, pk):
    return render(request, 'contact_details/contact_detail.html')

def contact_create(request):
    return render(request, 'contact_details/contact_create.html')

def contact_edit(request, pk):
    return render(request, 'contact_details/contact_edit.html')

def contact_delete(request, pk):
    return render(request, 'contact_details/contact_delete.html')
