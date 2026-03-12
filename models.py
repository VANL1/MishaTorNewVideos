from django.db import models
from django.utils import timezone

class ChatMessage(models.Model):
    username = models.CharField('Имя пользователя', max_length=50, default='Аноним')
    message = models.TextField('Сообщение')
    created_at = models.DateTimeField('Дата и время', default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']  # Сортировка по убыванию (новые сверху)
        verbose_name = 'Сообщение чата'
        verbose_name_plural = 'Сообщения чата'
    
    def __str__(self):
        return f'{self.username}: {self.message[:50]}'