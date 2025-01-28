from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic.edit import DeleteView
from .models import Client, ClientNote
from .forms import ClientForm, ClientNoteForm

@login_required
def client_list(request):
    clients_list = Client.objects.all()
    paginator = Paginator(clients_list, 3)     
    page = request.GET.get('page')
    clients = paginator.get_page(page)
    return render(request, 'crm/client_list.html', {'clients': clients})

@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    notes = client.notes.all()
    
    if request.method == 'POST':
        form = ClientNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.client = client
            note.agent = request.user
            note.save()
            messages.success(request, 'Note ajoutée avec succès.')
            return redirect('client_detail', pk=pk)
    else:
        form = ClientNoteForm()
    
    return render(request, 'crm/client_detail.html', {
        'client': client,
        'notes': notes,
        'form': form
    })

@login_required
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            messages.success(request, 'Client créé avec succès.')
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
    
    return render(request, 'crm/client_form.html', {
        'form': form,
        'title': 'Nouveau Client'
    })

@login_required
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client modifié avec succès.')
            return redirect('client_detail', pk=pk)
    else:
        form = ClientForm(instance=client)
    
    return render(request, 'crm/client_form.html', {
        'form': form,
        'title': f'Modifier {client.name}'
    })

@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Client supprimé avec succès.')
        return redirect('client_list')
    return render(request, 'crm/client_confirm_delete.html', {'client': client})