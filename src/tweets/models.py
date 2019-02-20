from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from core.validators import checkurl


class Tweet(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='tweets')
    content = models.CharField(max_length=140, validators=[checkurl])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('tweet')
        verbose_name_plural = _('tweets')
        ordering = ('-updated_at',)

    def __str__(self):
        return self.content

    def __repr__(self):
        return '{}<User: {}, Id:{}>'.format(self.__class__.__name__,
                                            self.user.username,
                                            self.pk)

    def get_absolute_url(self):
        return reverse("tweets:detail", kwargs={'pk': self.pk})

#    def clean(self, *args, **kwargs):
#        content = self.content
#        if get_urls(content):
#            raise ValidationError('Text cannot consist of urls')
#        return super(Tweet, self).clean(*args, **kwargs)
