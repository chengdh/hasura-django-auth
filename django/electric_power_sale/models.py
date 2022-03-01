from django.db import models
from api.models import Organization
from datetime import date

class Agent(models.Model):
    """居间资料
    """
    name = models.CharField("居间名称",max_length=200)
    organization = models.ForeignKey(Organization, verbose_name="上级机构",null=True,on_delete=models.SET_NULL)
    address = models.CharField("地址",null=True,blank=True,max_length=200)
    agent_no = models.CharField("编号",null=True,blank=True,max_length=60)
    toucher_1 = models.CharField("联系人1",null=True,blank=True,max_length=60)
    toucher_2 = models.CharField("联系人2",null=True,blank=True,max_length=60)
    toucher_mobile_1 = models.CharField("联系电话1",null=True,blank=True,max_length=60)
    toucher_mobile_2 = models.CharField("联系电话2",null=True,blank=True,max_length=60)
    default_agent_rate = models.DecimalField("默认居间分成比例",max_digits=20,decimal_places=4,default=0)

 
# Create your models here.
class Customer(models.Model):
    """客户资料
    """
    def get_customer_no():
        """自动生成客户编号

        Returns:
            string: 8位日期-6位序号 
        """
        count = Customer.objects.count()
        if no == None:
            count = 1 
        else:
            count += 1
        return "{:%Y%M%d}-{:06d}".format(date.today(),count)

    name = models.CharField("客户名称",max_length=200)
    organization = models.ForeignKey(Organization, verbose_name="上级机构",null=True,on_delete=models.SET_NULL)
    address = models.CharField("地址",null=True,blank=True,max_length=200)
    custom_no = models.CharField("客户编号",null=True,blank=True,max_length=60,default=get_customer_no)
    toucher_1 = models.CharField("联系人1",null=True,blank=True,max_length=60)
    toucher_2 = models.CharField("联系人2",null=True,blank=True,max_length=60)
    toucher_mobile_1 = models.CharField("联系电话1",null=True,blank=True,max_length=60)
    toucher_mobile_2 = models.CharField("联系电话2",null=True,blank=True,max_length=60)

    grid_account = models.CharField("电网账号",null=True,blank=True,max_length=60)
    grid_password = models.CharField("电网密码",null=True,blank=True,max_length=60)

    elect_level = models.IntegerField("电压等级",null=True,blank=True)
    transformer_volume = models.IntegerField("变压器容量",null=True,blank=True)

    #收入结算方式
    #服务费率
    INCOME_TYPE_RATE="income_type_rate"
    #固定金额
    INCOME_TYPE_FIXED="income_type_fixed"
    #分成比例
    INCOME_TYPE_DIVIDE_RATE="income_type_divide_rate"

    INCOME_TYPE_CHOICES = [(INCOME_TYPE_RATE,"按服务费率"),(INCOME_TYPE_FIXED,"按固定金额"),(INCOME_TYPE_DIVIDE_RATE,"按分成比例")]
    income_type = models.CharField("收入结算方式",max_length=40,
        choices=INCOME_TYPE_CHOICES ,
        default=INCOME_TYPE_RATE)
    
    rate = models.DecimalField("服务费率",max_digits=10,decimal_places=4,default=0)
    fix_fee = models.DecimalField("固定服务费",max_digits=20,decimal_places=4,default=0)
    divide_rate = models.DecimalField("分成比例",max_digits=20,decimal_places=4,default=0)

    agent = models.ForeignKey(Agent, verbose_name="所属居间",null=True, on_delete=models.SET_NULL)
    agent_rate = models.DecimalField("与居间分成比例",max_digits=20,decimal_places=4,default=0)
    tax_diff = models.DecimalField("税差",max_digits=20,decimal_places=4,default=0)
 
    note_1 = models.TextField("备注1",null=True,blank=True)
    note_2 = models.TextField("备注2",null=True,blank=True)
    note_3 = models.TextField("备注3",null=True,blank=True)
    is_active = models.BooleanField("是否有效", default=True)
