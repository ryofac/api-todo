from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    description = models.CharField(max_length=155)
    created_at = models.DateField(_("Created At"), auto_now_add=True)
    end_at = models.DateField(_("End at"), auto_now=False, auto_now_add=False)
    is_active = models.BooleanField(_("Is the task active"), default=True)

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Task_detail", kwargs={"pk": self.pk})
