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
    note = models.TextField("备注1",null=True,blank=True)
    is_active = models.BooleanField("是否有效", default=True)


 
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

    elect_level = models.CharField("电压等级",null=True,blank=True,max_length=60)
    transformer_volume = models.CharField("变压器容量",null=True,blank=True,max_length=60)

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

    #客户用电性质
    #常规
    USE_TYPE_COMMON="use_type_common"
    #分时段
    USE_TYPE_SEPRATE_TIME="use_type_seprate_time"
    #常规-高耗能
    USE_TYPE_COMMON_HIGH_POWER="use_type_common_high_power"
    #高耗能-分时段
    USE_TYPE_HIGH_POWER_SEPRATE_TIME="use_type_high_power_seprate_time"

    USE_TYPE_CHOICES = [(USE_TYPE_COMMON,"常规"),(USE_TYPE_SEPRATE_TIME,"常规-分时段"),(USE_TYPE_COMMON_HIGH_POWER,"常规-高耗能"),(USE_TYPE_HIGH_POWER_SEPRATE_TIME,"高耗能-分时段")]


    use_type = models.CharField("客户用电性质",max_length=80,
        choices=USE_TYPE_CHOICES ,
        default=USE_TYPE_COMMON)
 
    
    rate = models.DecimalField("服务费率",max_digits=10,decimal_places=4,null=True,default=0)
    fix_fee = models.DecimalField("固定服务费",null=True,max_digits=20,decimal_places=4,default=0)
    divide_rate = models.DecimalField("分成比例",null=True,max_digits=20,decimal_places=4,default=0)

    agent = models.ForeignKey(Agent, verbose_name="所属居间",null=True, on_delete=models.SET_NULL)
    agent_rate = models.DecimalField("与居间分成比例",null=True,max_digits=20,decimal_places=4,default=0)
    tax_diff = models.DecimalField("税差",max_digits=20,null=True,decimal_places=4,default=0)
 
    note_1 = models.TextField("备注1",null=True,blank=True)
    note_2 = models.TextField("备注2",null=True,blank=True)
    note_3 = models.TextField("备注3",null=True,blank=True)
    is_active = models.BooleanField("是否有效", default=True)
