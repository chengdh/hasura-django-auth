from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import  AbstractUser

class HasuraUser(AbstractUser):
    '''
    user代理类,用于扩展user的部分功能和属性
    '''

    default_role= models.ForeignKey("Role",related_name='+',verbose_name="默认用户组",null=True, on_delete=models.SET_NULL)

    default_org = models.ForeignKey("Organization",related_name='+', verbose_name="默认机构",null=True, on_delete=models.SET_NULL)

    avatar_url = models.CharField("头像地址", max_length=200)

    note = models.TextField("note")

    organizations = models.ManyToManyField("organization")
    roles = models.ManyToManyField("Role")

    @property
    def get_default_role(self):
        '''
        获取当前用户默认用户组,
        如果未设置,返回第一个用户组
        否则返回设置的用户组
        '''
        ret_role = self.default_role
        if not ret_role:
            ret_role = self.roles.first() 
        return ret_role

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
    note = models.TextField("备注",null=True,blank=True)
    parent_org = models.ForeignKey("self", verbose_name="上级机构",null=True, on_delete=models.CASCADE)
    header = models.ForeignKey(HasuraUser, verbose_name="负责人",null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField("是否有效", default=True)

class FunctionCategory(models.Model):
    """
    功能分类
    """
    frontend_router_path = models.CharField("路径",  max_length=200)
    frontend_router_name = models.CharField("类别",help_text="对应前端router名称",  max_length=200)
    frontend_router_redirect = models.CharField("重定向path",  max_length=200,null =True,blank=True)
    frontend_router_meta_title = models.CharField("类别",  max_length=200)
    frontend_router_meta_icon= models.CharField("显示图标",  max_length=200,null =True,blank=True)
    parent_function_category = models.ForeignKey("self", verbose_name="上级功能",null=True,blank=True, on_delete=models.CASCADE)
    rank = models.IntegerField("排序",default=1)
    is_active = models.BooleanField("是否有效", default=True)
    note = models.TextField("备注",null=True,blank=True)
    class Meta:
        ordering=["rank"]



class SystemFunction(models.Model):
    """
    系统功能
    """
    function_category = models.ForeignKey("FunctionCategory",verbose_name="所属类别",on_delete=models.CASCADE,related_name="children")
    frontend_router_path = models.CharField("路径",  max_length=200)
    frontend_router_name = models.CharField("类别",help_text="对应前端router名称",  max_length=200)
    frontend_router_redirect = models.CharField("重定向path",  max_length=200,null =True,blank=True)
    frontend_router_meta_title = models.CharField("类别",  max_length=200)
    frontend_router_meta_icon= models.CharField("显示图标",  max_length=200,null =True,blank=True)
    is_active = models.BooleanField("是否有效", default=True)
    rank = models.IntegerField("排序",default=1)
    note = models.TextField("备注",null=True,blank=True)

    class Meta:
        ordering=["rank"]


class SystemFunctionOperate(models.Model):
    """
    功能操作
    """ 
    system_function = models.ForeignKey("SystemFunction",verbose_name="所属功能",on_delete=models.CASCADE,related_name="operates")
    name = models.CharField("显示名称",  max_length=200)
    code = models.CharField("操作代码",  max_length=200)
    is_active = models.BooleanField("是否有效", default=True)
    rank = models.IntegerField("排序",default=1)
    note = models.TextField("备注",null=True,blank=True)

    class Meta:
        ordering=["rank"]



class Role(models.Model):
    """
    角色
    """ 
    name = models.CharField("名称",  max_length=200)
    is_active = models.BooleanField("有效", default=True)
    rank = models.IntegerField("排序",default=1)
    note = models.TextField("备注",null=True,blank=True)
    #角色具有的权限
    system_function_operates= models.ManyToManyField(SystemFunctionOperate,verbose_name="角色具有的权限")
    # class Meta:
        # ordering=["rank"]