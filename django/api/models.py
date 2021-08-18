from django.db import models
from django.contrib.auth.models import Group, User


class Organization(models.Model):
    """
     组织机构 
    """
    name = models.CharField("机构名称", null=False, max_length=200)
    address = models.CharField("地址", max_length=200)
    note = models.TextField("备注")
    parent_org = models.ForeignKey("self", verbose_name="上级机构",null=True, on_delete=models.CASCADE)
    header = models.ForeignKey(User, verbose_name="负责人",null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField("是否有效", default=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    default_group = models.ForeignKey(Group, verbose_name="默认用户组",null=True, on_delete=models.SET_NULL)

    default_org = models.ForeignKey(Organization, verbose_name="默认机构",null=True, on_delete=models.SET_NULL)

    avatar_url = models.CharField("头像地址", max_length=200)

    note = models.TextField("note")
