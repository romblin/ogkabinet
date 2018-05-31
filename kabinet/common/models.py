from django.db import models


class AbstractNamedModel(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ReadOnlyModelMixin:
    def save(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    class Meta:
        abstract = True

