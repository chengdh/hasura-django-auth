from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, AbstractUser

class HasuraUser(AbstractUser):
    '''
    user代理类，用于扩展user的部分功能和属性
    '''

    default_group = models.ForeignKey(Group, verbose_name="默认用户组",null=True, on_delete=models.SET_NULL)

    default_org = models.ForeignKey("Organization", verbose_name="默认机构",null=True, on_delete=models.SET_NULL)

    avatar_url = models.CharField("头像地址", max_length=200)

    note = models.TextField("note")

    @property
    def get_default_group(self):
        '''
        获取当前用户默认用户组,
        如果未设置，返回第一个用户组
        否则返回设置的用户组
        '''
        ret_group = self.default_group
        if not ret_group:
            ret_group = self.groups.first() 
        return ret_group

    @property
    def get_default_organization(self):
        '''
        获取用户默认的组织机构
        '''
        ret_org = None
        ret_org = self.default_org 
        if not ret_org:
            ret_org = self.organizations.first()
        return ret_org

class Organization(models.Model):
    """
     组织机构 
    """
    name = models.CharField("机构名称", null=False, max_length=200)
    address = models.CharField("地址", max_length=200)
    note = models.TextField("备注")
    parent_org = models.ForeignKey("self", verbose_name="上级机构",null=True, on_delete=models.CASCADE)
    header = models.ForeignKey(HasuraUser, verbose_name="负责人",null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField("是否有效", default=True)
    users = models.ManyToManyField(get_user_model(),related_name="organizations")