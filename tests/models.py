import uuid

from django.db import models

from treenode.models import TreeNodeModel


class Category(TreeNodeModel):
    treenode_display_field = "name"

    name = models.CharField(max_length=50, unique=True)

    class Meta(TreeNodeModel.Meta):
        app_label = "tests"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class CategoryWithUUIDPk(TreeNodeModel):
    treenode_display_field = "name"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)

    class Meta(TreeNodeModel.Meta):
        app_label = "tests"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class CategoryWithoutDisplayField(TreeNodeModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta(TreeNodeModel.Meta):
        app_label = "tests"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
