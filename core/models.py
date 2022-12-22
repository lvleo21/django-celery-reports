from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Task(Timestamp):
    SEGMENTATION_CHOICE = (
        ("heroes", _(u"Heróis")),
        ("sidekicks", _(u"Ajudantes")),
        ("interns", _(u"Estagiários")),
        ("students", _(u"Estudantes")),
    )

    title = models.CharField(_(u"Título"), max_length=255)
    segmentation = models.CharField(_(u"Segmentação"), max_length=255, choices=SEGMENTATION_CHOICE, default = "students")
    organization = models.ForeignKey("Organization", verbose_name=_(u"Organização"), on_delete=models.CASCADE)
    points = models.PositiveIntegerField(_(u"Pontuação"), default=0, blank=True)

    class Meta:
        verbose_name = _(u"Ação")
        verbose_name_plural = _(u"Ações")
    
    def __str__(self):
        return f"{self.title}"


class Organization(Timestamp):
    name = models.CharField(_(u"Nome"), max_length=255)

    class Meta:
        verbose_name = _(u"Organização")
        verbose_name_plural = _(u"Organizações")
    
    def __str__(self):
        return f"{self.name}"


class Realization(Timestamp):
    STATUS_CHOICE = (
        ('created', _(u'Criado')),
        ('succeeded', _(u'Aprovado')),
        ('validating', _(u'Validando')),
        ('failed', _(u'Falhou')),
    )

    points = models.PositiveIntegerField(_(u"Pontos"), default=0, blank=True)
    organization = models.ForeignKey(Organization, verbose_name=_(u"Organização"), on_delete=models.CASCADE)
    task = models.ForeignKey(Task, verbose_name=_(u"Ação"), on_delete=models.CASCADE)
    account = models.ForeignKey(User, verbose_name=_(u"Usuário"), on_delete=models.CASCADE)
    status = models.CharField(_(u"status"), max_length=20, choices=STATUS_CHOICE, default="validating")

    class Meta:
        verbose_name = _(u"Realização")
        verbose_name_plural = _(u"Realizações")
        unique_together = (('account', 'task'),)
    
    def __str__(self):
        return f"#{self.id}"
