from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.http import require_POST
from .models import ChatMessage
from .forms import ChatMessageForm

def home(request):
    # Получаем последние 50 сообщений
    messages = ChatMessage.objects.all()[:50]
    form = ChatMessageForm()
    
    return render(request, 'home.html', {
        'messages': messages,
        'form': form
    })

@require_POST
def send_message(request):
    form = ChatMessageForm(request.POST)
    if form.is_valid():
        message = form.save()
        return JsonResponse({
            'success': True,
            'username': message.username,
            'message': message.message,
            'created_at': message.created_at.strftime('%H:%M %d.%m.%Y')
        })
    return JsonResponse({'success': False, 'errors': form.errors})

def get_messages(request):
    # Получаем сообщения новее определенного ID
    last_id = request.GET.get('last_id', 0)
    messages = ChatMessage.objects.filter(id__gt=last_id)[:20]
    
    messages_data = [{
        'id': msg.id,
        'username': msg.username,
        'message': msg.message,
        'created_at': msg.created_at.strftime('%H:%M %d.%m.%Y')
    } for msg in messages]
    
    return JsonResponse({'messages': messages_data})