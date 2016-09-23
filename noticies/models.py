from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

#Dades Noticies

class categoria(models.Model):
	id_categoria = models.AutoField(primary_key=True)
	nom_categoria = models.CharField('Nom Noticia' ,max_length=50)
	#pare_categoria = models.ForeignKey(categoria)

	def __unicode__(self):
		return u'%s' % (self.nom_categoria)

	class Meta:
		ordering = ['nom_categoria']

class post(models.Model):
	id_post = models.AutoField(primary_key=True)
	nom_post = models.CharField('Nom Noticia' ,max_length=40)
	descr_post = models.TextField('Descripcio' ,max_length=250)
	autor_post = models.ForeignKey('auth.User')
	data_post = models.DateTimeField(default=timezone.now)
	#cod_categoria = models.ForeignKey(categoria)
	foto_post = models.ImageField(upload_to='uploads',verbose_name='Imatge Noticia')

	def __unicode__(self):
		return u'%s' % (self.nom_post)

	class Meta:
		ordering = ['nom_post']

