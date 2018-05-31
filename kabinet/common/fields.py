from django.db import models
from django.contrib.postgres.fields import ArrayField


class OptionalField:
    def __init__(self, *args, **kwargs):
        kwargs['blank'] = True
        kwargs['null'] = True
        super(OptionalField, self).__init__(*args, **kwargs)


class OptionalForeignKey(OptionalField, models.ForeignKey):
    pass


class OptionalManyToManyField(models.ManyToManyField):

    def __init__(self, *args, **kwargs):
        kwargs['blank'] = True
        super(OptionalManyToManyField, self).__init__(*args, **kwargs)


class OptionalCharField(OptionalField, models.CharField):
    pass


class MaxOptionalCharField(OptionalCharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 255
        super(MaxOptionalCharField, self).__init__(*args, **kwargs)


class OptionalBigIntegerField(OptionalField, models.BigIntegerField):
    pass


class OptionalArrayField(OptionalField, ArrayField):
    pass


class OptionalDateTimeField(OptionalField, models.DateTimeField):
    pass


class OptionalPositiveIntegerField(OptionalField, models.PositiveIntegerField):
    pass
