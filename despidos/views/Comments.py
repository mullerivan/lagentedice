# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

import operator

from django.db import models
from django.db.models import Q
from django.db.models import QuerySet
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from mptt.models import MPTTModel
from mptt.models import TreeForeignKey
from mptt.managers import TreeManager

__all__ = (
    'Comment',
    'CommentContext',
)


class CommentQuerySet(models.QuerySet):
    """Custom queryset for Comment model that works similar to fsm state log."""

    def _get_content_type(self, obj):
        return ContentType.objects.get_for_model(obj)

    def for_(self, *args):
        """Queryset all log messages for given object."""
        filters = []
        is_public = True
        for obj in args:
            if isinstance(obj, QuerySet):
                for o in obj:
                    if type(obj.pk) is int:
                        filters.append(
                            Q(content_type=self._get_content_type(o),
                              object_id=o.pk))
            elif type(obj) is bool:
                is_public = obj
            elif type(obj.pk) is int:
                filters.append(
                    Q(content_type=self._get_content_type(obj),
                      object_id=obj.pk))

        if len(filters) > 0:
            pks = CommentContext.objects \
                .filter(reduce(operator.or_, filters)) \
                .values_list('comment__pk', flat=True)
            return self.filter(pk__in=pks, is_public=is_public).order_by('pk')
        return self.none()


class CommentManager(models.Manager.from_queryset(CommentQuerySet),
                     TreeManager):
    """Empty class just to get the correct inheritance."""

    pass


@python_2_unicode_compatible
class Comment(MPTTModel):
    """Generic model to store comments."""

    comment = models.TextField()

    by = models.ForeignKey(
        'accounts.User')

    date_created = models.DateTimeField(
        auto_now_add=True)

    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True)

    is_public = models.BooleanField(
        default=True,
        help_text='Only staff members can view private comments')

    objects = CommentManager()

    def __str__(self):
        return '{} commented {}'.format(self.by, self.comment)

    def add_context(self, obj):
        """Add object context to the comment."""
        ct = ContentType.objects.get_for_model(obj)
        return CommentContext.objects.create(
            comment=self,
            content_type=ct,
            object_id=obj.pk)

    def get_context(self, content_object_type=None):
        """Get context objects for comment."""
        objs = list()
        for row in CommentContext.objects.filter(comment=self):
            if (content_object_type is not None and \
                        isinstance(row.content_object, content_object_type)) or \
                            content_object_type is None:
                objs.append(row.content_object)
        return objs


class CommentContext(models.Model):
    """Give comments context by assigning to other model objects.

    This uses generic foreign keys.

    """

    comment = models.ForeignKey(
        Comment)

    content_type = models.ForeignKey(
        ContentType)

    object_id = models.PositiveIntegerField(
        db_index=True)

    content_object = GenericForeignKey(
        'content_type',
        'object_id')
