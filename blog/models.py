from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField(max_length=255, unique=True) # /slug
  author = models.ForeignKey(User, on_delete=models.CASCADE) # chave com id do usuário e marcada para deletar todos os post quando usuário for deletado
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True) # gravar a data automática quando criado
  updated = models.DateTimeField(auto_now=True) # gravar sempre nova data quando editado

  class Meta:
    ordering = ('-created',)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('blog:detail', kwargs={'slug': self.slug})