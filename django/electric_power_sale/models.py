from django.db import models
from api.models import HasuraUser, Organization
from datetime import date,datetime

def default_cur_date():
    return date.today()

def default_cur_mth():
    return date.today().strftime("%Y-%m")

def default_last_mth():
    today = datetime.date.today()
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)
    return last_month .strftime("%Y-%m")

def default_cur_datetime():
    return datetime.now()

def default_year_start_date():
    epoch_year = date.today().year
    year_start = date(epoch_year, 1, 1)
    return year_start

def default_year_end_date():
    epoch_year = date.today().year
    year_end = date(epoch_year, 12, 31)
    return year_end


def default_cur_year():
    return date.today().year

STATE_DRAFT="draft"
STATE_CONFIRMED="confirmed"
STATE_CHOICES = [(STATE_DRAFT,"草稿"),(STATE_CONFIRMED,"已确认")]
 
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
    note = models.TextField("备注",null=True,blank=True)
    is_active = models.BooleanField("是否有效", default=True)
    created_by = models.ForeignKey(HasuraUser, verbose_name="录入人",null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField("录入时间", default=default_cur_datetime)
    updated_by = models.ForeignKey(HasuraUser, verbose_name="更新人",related_name="+",null=True,on_delete=models.SET_NULL)
    updated_at = models.DateTimeField("更新时间", default=default_cur_datetime)

TRANSFORMER_TYPE_LT_35="transformer_type_lt_35"
TRANSFORMER_TYPE_GT_35="transformer_type_gt_35"
TRANSFORMER_TYPE_CHOICES = [(TRANSFORMER_TYPE_LT_35,"35KVA以下"),(TRANSFORMER_TYPE_LT_35,"35KVA以上")]
 
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
    organization = models.ForeignKey(Organization, verbose_name="所属机构",null=True,on_delete=models.SET_NULL)
    address = models.CharField("地址",null=True,blank=True,max_length=200)
    custom_no = models.CharField("客户编号",null=True,blank=True,max_length=60,default=get_customer_no)
    toucher_1 = models.CharField("联系人1",null=True,blank=True,max_length=60)
    toucher_2 = models.CharField("联系人2",null=True,blank=True,max_length=60)
    toucher_mobile_1 = models.CharField("联系电话1",null=True,blank=True,max_length=60)
    toucher_mobile_2 = models.CharField("联系电话2",null=True,blank=True,max_length=60)

    grid_account = models.CharField("电网账号",null=True,blank=True,max_length=60)
    grid_password = models.CharField("电网密码",null=True,blank=True,max_length=60)


    #电压等级
    ELECT_LEVEL_LT_1KV = "lt_1kv"
    ELECT_LEVEL_1KV_1KV = "1kv_10kv"
    ELECT_LEVEL_35KV = "35kv"
    ELECT_LEVEL_110KV = "110kv"
    ELECT_LEVEL_220KV = "220kv"
    ELECT_LEVEL_CHOICES = [(ELECT_LEVEL_LT_1KV,"不满1千伏"),(ELECT_LEVEL_1KV_1KV, "1~10千伏"),(ELECT_LEVEL_35KV,"35千伏"),(ELECT_LEVEL_110KV, "110千伏"),(ELECT_LEVEL_220KV, "220千伏")]

    elect_level = models.CharField("电压等级",
        choices=ELECT_LEVEL_CHOICES ,
        default=ELECT_LEVEL_35KV ,
        null=True,blank=True,max_length=60)

    transformer_volume = models.CharField("变压器容量",null=True,blank=True,max_length=60)

    #服务费率

    transformer_type = models.CharField("变压器容量类型",
        choices=TRANSFORMER_TYPE_CHOICES ,
        default=TRANSFORMER_TYPE_LT_35,
        null=True,blank=True,max_length=60)

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
    created_by = models.ForeignKey(HasuraUser, verbose_name="录入人",null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField("录入时间", default=default_cur_datetime)
    updated_by = models.ForeignKey(HasuraUser, verbose_name="更新人",related_name="+",null=True,on_delete=models.SET_NULL)
    updated_at = models.DateTimeField("更新时间", default=default_cur_datetime)

class DeviceNo(models.Model):
    """客户户号表

    Args:
        models (_type_): _description_
    """
    customer = models.ForeignKey(Customer, verbose_name="关联客户",on_delete=models.CASCADE)
    device_no = models.CharField("电表号",max_length=40)
    is_active = models.BooleanField("是否有效", default=True)
    note = models.TextField("备注1",null=True,blank=True)

#电量计费方式
#常规
PRICE_TYPE_COMMON="price_type_common"
#分时段
PRICE_TYPE_SEPRATE_TIME="price_type_seprate_time"

PRICE_TYPE_CHOICES = [(PRICE_TYPE_COMMON,"常规"),(PRICE_TYPE_SEPRATE_TIME,"分时段")]


class Contract(models.Model):
    """销售合同
    """
    name = models.CharField("合同名称",max_length=200)
    organization = models.ForeignKey(Organization, verbose_name="所属机构",null=True,on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, verbose_name="关联客户",null=True,on_delete=models.SET_NULL)
    contract_no = models.CharField("合同编号",max_length=40,blank=True,null=True)
    contract_year = models.IntegerField("所属年度",default=default_cur_year)
    contract_start_date = models.DateField("合同生效日期",default=default_year_start_date)
    contract_end_date = models.DateField("合同结束日期",default=default_year_end_date)

  
    contract_price_type = models.CharField("电价价方式",max_length=40,
        choices=PRICE_TYPE_CHOICES,
        default=PRICE_TYPE_COMMON)


    price_common = models.DecimalField("常规时段电价(元/KWA)",max_digits=20,decimal_places=4,default=0)
    price_peak = models.DecimalField("峰时段电价(元/KWA)",max_digits=20,decimal_places=4,default=0)
    price_flat= models.DecimalField("平时段电价(元/KWA)",max_digits=20,decimal_places=4,default=0)
    price_valley = models.DecimalField("谷时段电价(元/KWA)",max_digits=20,decimal_places=4,default=0)

    year_plan = models.DecimalField("年度签约电量(兆瓦时)",max_digits=20,decimal_places=4,default=0)

    state = models.CharField("状态",choices=STATE_CHOICES,max_length=40,default=STATE_DRAFT)
    note = models.TextField("备注1",null=True,blank=True)
    created_by = models.ForeignKey(HasuraUser, verbose_name="录入人",null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField("录入时间", default=default_cur_datetime)
    updated_at = models.DateTimeField("更新时间", default=default_cur_datetime)
    updated_by = models.ForeignKey(HasuraUser, verbose_name="更新人",related_name="+",null=True,on_delete=models.SET_NULL)

    is_active = models.BooleanField("是否有效", default=True)

class ContractLine(models.Model):
    """合同明细(电量计划表)
    """
    contract = models.ForeignKey(Contract,verbose_name="合同",on_delete=models.CASCADE)

    plan_common_mth_1= models.DecimalField("计划电量-常规",max_digits=20,decimal_places=4,default=0)
    plan_flat_mth_1= models.DecimalField("计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    plan_valley_mth_1= models.DecimalField("计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    plan_peak_mth_1= models.DecimalField("计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    plan_common_mth_2= models.DecimalField("计划电量-常规",max_digits=20,decimal_places=4,default=0)
    plan_flat_mth_2= models.DecimalField("计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    plan_valley_mth_2= models.DecimalField("计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    plan_peak_mth_2= models.DecimalField("计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    plan_common_mth_3= models.DecimalField("计划电量-常规",max_digits=20,decimal_places=4,default=0)
    plan_flat_mth_3= models.DecimalField("计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    plan_valley_mth_3= models.DecimalField("计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    plan_peak_mth_3= models.DecimalField("计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    plan_common_mth_4= models.DecimalField("计划电量-常规",max_digits=20,decimal_places=4,default=0)
    plan_flat_mth_4= models.DecimalField("计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    plan_valley_mth_4= models.DecimalField("计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    plan_peak_mth_4= models.DecimalField("计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    plan_common_mth_5= models.DecimalField("计划电量-常规",max_digits=20,decimal_places=4,default=0)
    plan_flat_mth_5= models.DecimalField("计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    plan_valley_mth_5= models.DecimalField("计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    plan_peak_mth_5= models.DecimalField("计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    plan_common_mth_6= models.DecimalField("计划电量-常规",max_digits=20,decimal_places=4,default=0)
    plan_flat_mth_6= models.DecimalField("计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    plan_valley_mth_6= models.DecimalField("计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    plan_peak_mth_6= models.DecimalField("计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    plan_common_mth_7= models.DecimalField("计划电量-常规",max_digits=20,decimal_places=4,default=0)
    plan_flat_mth_7= models.DecimalField("计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    plan_valley_mth_7= models.DecimalField("计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    plan_peak_mth_7= models.DecimalField("计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    plan_common_mth_8= models.DecimalField("计划电量-常规",max_digits=20,decimal_places=4,default=0)
    plan_flat_mth_8= models.DecimalField("计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    plan_valley_mth_8= models.DecimalField("计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    plan_peak_mth_8= models.DecimalField("计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    plan_common_mth_9= models.DecimalField("计划电量-常规",max_digits=20,decimal_places=4,default=0)
    plan_flat_mth_9= models.DecimalField("计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    plan_valley_mth_9= models.DecimalField("计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    plan_peak_mth_9= models.DecimalField("计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    plan_common_mth_10= models.DecimalField("计划电量-常规",max_digits=20,decimal_places=4,default=0)
    plan_flat_mth_10= models.DecimalField("计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    plan_valley_mth_10= models.DecimalField("计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    plan_peak_mth_10= models.DecimalField("计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    plan_common_mth_11= models.DecimalField("计划电量-常规",max_digits=20,decimal_places=4,default=0)
    plan_flat_mth_11= models.DecimalField("计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    plan_valley_mth_11= models.DecimalField("计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    plan_peak_mth_11= models.DecimalField("计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    plan_common_mth_12= models.DecimalField("计划电量-常规",max_digits=20,decimal_places=4,default=0)
    plan_flat_mth_12= models.DecimalField("计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    plan_valley_mth_12= models.DecimalField("计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    plan_peak_mth_12= models.DecimalField("计划电量-峰时段",max_digits=20,decimal_places=4,default=0)



    #以下字段从不同业务表中同步
    adjust_plan_common_mth_1= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_1= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_1= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_1= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)

    adjust_plan_common_mth_2= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_2= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_2= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_2= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)

    adjust_plan_common_mth_3= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_3= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_3= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_3= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)

    adjust_plan_common_mth_4= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_4= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_4= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_4= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)

    adjust_plan_common_mth_5= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_5= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_5= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_5= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)

    adjust_plan_common_mth_6= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_6= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_6= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_6= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)

    adjust_plan_common_mth_7= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_7= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_7= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_7= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)

    adjust_plan_common_mth_8= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_8= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_8= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_8= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)

    adjust_plan_common_mth_9= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_9= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_9= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_9= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)

    adjust_plan_common_mth_10= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_10= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_10= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_10= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)

    adjust_plan_common_mth_11= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_11= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_11= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_11= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)

    adjust_plan_common_mth_12= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_12= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_12= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_12= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)


    act_common_mth_1= models.DecimalField("电量结算-常规",max_digits=20,decimal_places=4,default=0)
    act_flat_mth_1= models.DecimalField("电量结算-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley_mth_1= models.DecimalField("电量结算-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak_mth_1= models.DecimalField("电量结算-峰时段",max_digits=20,decimal_places=4,default=0)

    act_common_mth_2= models.DecimalField("电量结算-常规",max_digits=20,decimal_places=4,default=0)
    act_flat_mth_2= models.DecimalField("电量结算-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley_mth_2= models.DecimalField("电量结算-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak_mth_2= models.DecimalField("电量结算-峰时段",max_digits=20,decimal_places=4,default=0)

    act_common_mth_3= models.DecimalField("电量结算-常规",max_digits=20,decimal_places=4,default=0)
    act_flat_mth_3= models.DecimalField("电量结算-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley_mth_3= models.DecimalField("电量结算-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak_mth_3= models.DecimalField("电量结算-峰时段",max_digits=20,decimal_places=4,default=0)

    act_common_mth_4= models.DecimalField("电量结算-常规",max_digits=20,decimal_places=4,default=0)
    act_flat_mth_4= models.DecimalField("电量结算-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley_mth_4= models.DecimalField("电量结算-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak_mth_4= models.DecimalField("电量结算-峰时段",max_digits=20,decimal_places=4,default=0)

    act_common_mth_5= models.DecimalField("电量结算-常规",max_digits=20,decimal_places=4,default=0)
    act_flat_mth_5= models.DecimalField("电量结算-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley_mth_5= models.DecimalField("电量结算-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak_mth_5= models.DecimalField("电量结算-峰时段",max_digits=20,decimal_places=4,default=0)

    act_common_mth_6= models.DecimalField("电量结算-常规",max_digits=20,decimal_places=4,default=0)
    act_flat_mth_6= models.DecimalField("电量结算-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley_mth_6= models.DecimalField("电量结算-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak_mth_6= models.DecimalField("电量结算-峰时段",max_digits=20,decimal_places=4,default=0)

    act_common_mth_7= models.DecimalField("电量结算-常规",max_digits=20,decimal_places=4,default=0)
    act_flat_mth_7= models.DecimalField("电量结算-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley_mth_7= models.DecimalField("电量结算-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak_mth_7= models.DecimalField("电量结算-峰时段",max_digits=20,decimal_places=4,default=0)


    act_common_mth_8= models.DecimalField("电量结算-常规",max_digits=20,decimal_places=4,default=0)
    act_flat_mth_8= models.DecimalField("电量结算-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley_mth_8= models.DecimalField("电量结算-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak_mth_8= models.DecimalField("电量结算-峰时段",max_digits=20,decimal_places=4,default=0)

    act_common_mth_9= models.DecimalField("电量结算-常规",max_digits=20,decimal_places=4,default=0)
    act_flat_mth_9= models.DecimalField("电量结算-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley_mth_9= models.DecimalField("电量结算-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak_mth_9= models.DecimalField("电量结算-峰时段",max_digits=20,decimal_places=4,default=0)

    act_common_mth_10= models.DecimalField("电量结算-常规",max_digits=20,decimal_places=4,default=0)
    act_flat_mth_10= models.DecimalField("电量结算-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley_mth_10= models.DecimalField("电量结算-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak_mth_10= models.DecimalField("电量结算-峰时段",max_digits=20,decimal_places=4,default=0)

    act_common_mth_11= models.DecimalField("电量结算-常规",max_digits=20,decimal_places=4,default=0)
    act_flat_mth_11= models.DecimalField("电量结算-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley_mth_11= models.DecimalField("电量结算-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak_mth_11= models.DecimalField("电量结算-峰时段",max_digits=20,decimal_places=4,default=0)

    act_common_mth_12= models.DecimalField("电量结算-常规",max_digits=20,decimal_places=4,default=0)
    act_flat_mth_12= models.DecimalField("电量结算-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley_mth_12= models.DecimalField("电量结算-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak_mth_12= models.DecimalField("电量结算-峰时段",max_digits=20,decimal_places=4,default=0)


    state = models.CharField("状态",max_length=40,default="draft")

    note = models.TextField("备注1",null=True,blank=True)
    created_by = models.ForeignKey(HasuraUser, verbose_name="录入人",null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField("录入时间", default=default_cur_datetime)
    updated_at = models.DateTimeField("更新时间", default=default_cur_datetime)
    updated_by = models.ForeignKey(HasuraUser, verbose_name="更新人",related_name="+",null=True,on_delete=models.SET_NULL)



class MthAdjust(models.Model):
    """月度电量调整表

    Args:
        models (_type_): _description_
    """
    organization = models.ForeignKey(Organization, verbose_name="所属机构",null=True,on_delete=models.SET_NULL)
    mth = models.CharField("月份",max_length=7,default=default_last_mth)

    state = models.CharField("状态",max_length=40,default="draft")

    note = models.TextField("备注",null=True,blank=True)
    created_by = models.ForeignKey(HasuraUser, verbose_name="录入人",null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField("录入时间", default=default_cur_datetime)
    updated_by = models.ForeignKey(HasuraUser, verbose_name="更新人",related_name="+",null=True,on_delete=models.SET_NULL)
    updated_at = models.DateTimeField("更新时间", default=default_cur_datetime)




class MthAdjustLine(models.Model):
    """月度电量调整子表

    Args:
        models (_type_): _description_
    """
    mth_adjust= models.ForeignKey(MthAdjust, verbose_name="月度电量调整主表",on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, verbose_name="关联客户",null=True,on_delete=models.SET_NULL)

    contract = models.ForeignKey(Contract, verbose_name="关联合同",null=True,on_delete=models.SET_NULL)

    #调整前
    previous_plan_common_mth_1= models.DecimalField("调整前计划电量-常规",max_digits=20,decimal_places=4,default=0)
    previous_plan_flat_mth_1= models.DecimalField("调整前计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_valley_mth_1= models.DecimalField("调整前计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_peak_mth_1= models.DecimalField("调整前计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    previous_plan_common_mth_2= models.DecimalField("调整前计划电量-常规",max_digits=20,decimal_places=4,default=0)
    previous_plan_flat_mth_2= models.DecimalField("调整前计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_valley_mth_2= models.DecimalField("调整前计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_peak_mth_2= models.DecimalField("调整前计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    previous_plan_common_mth_3= models.DecimalField("调整前计划电量-常规",max_digits=20,decimal_places=4,default=0)
    previous_plan_flat_mth_3= models.DecimalField("调整前计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_valley_mth_3= models.DecimalField("调整前计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_peak_mth_3= models.DecimalField("调整前计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    previous_plan_common_mth_4= models.DecimalField("调整前计划电量-常规",max_digits=20,decimal_places=4,default=0)
    previous_plan_flat_mth_4= models.DecimalField("调整前计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_valley_mth_4= models.DecimalField("调整前计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_peak_mth_4= models.DecimalField("调整前计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    previous_plan_common_mth_5= models.DecimalField("调整前计划电量-常规",max_digits=20,decimal_places=4,default=0)
    previous_plan_flat_mth_5= models.DecimalField("调整前计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_valley_mth_5= models.DecimalField("调整前计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_peak_mth_5= models.DecimalField("调整前计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    previous_plan_common_mth_6= models.DecimalField("调整前计划电量-常规",max_digits=20,decimal_places=4,default=0)
    previous_plan_flat_mth_6= models.DecimalField("调整前计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_valley_mth_6= models.DecimalField("调整前计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_peak_mth_6= models.DecimalField("调整前计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    previous_plan_common_mth_7= models.DecimalField("调整前计划电量-常规",max_digits=20,decimal_places=4,default=0)
    previous_plan_flat_mth_7= models.DecimalField("调整前计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_valley_mth_7= models.DecimalField("调整前计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_peak_mth_7= models.DecimalField("调整前计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    previous_plan_common_mth_8= models.DecimalField("调整前计划电量-常规",max_digits=20,decimal_places=4,default=0)
    previous_plan_flat_mth_8= models.DecimalField("调整前计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_valley_mth_8= models.DecimalField("调整前计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_peak_mth_8= models.DecimalField("调整前计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    previous_plan_common_mth_9= models.DecimalField("调整前计划电量-常规",max_digits=20,decimal_places=4,default=0)
    previous_plan_flat_mth_9= models.DecimalField("调整前计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_valley_mth_9= models.DecimalField("调整前计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_peak_mth_9= models.DecimalField("调整前计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    previous_plan_common_mth_10= models.DecimalField("调整前计划电量-常规",max_digits=20,decimal_places=4,default=0)
    previous_plan_flat_mth_10= models.DecimalField("调整前计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_valley_mth_10= models.DecimalField("调整前计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_peak_mth_10= models.DecimalField("调整前计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    previous_plan_common_mth_11= models.DecimalField("调整前计划电量-常规",max_digits=20,decimal_places=4,default=0)
    previous_plan_flat_mth_11= models.DecimalField("调整前计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_valley_mth_11= models.DecimalField("调整前计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_peak_mth_11= models.DecimalField("调整前计划电量-峰时段",max_digits=20,decimal_places=4,default=0)


    previous_plan_common_mth_12= models.DecimalField("调整前计划电量-常规",max_digits=20,decimal_places=4,default=0)
    previous_plan_flat_mth_12= models.DecimalField("调整前计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_valley_mth_12= models.DecimalField("调整前计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    previous_plan_peak_mth_12= models.DecimalField("调整前计划电量-峰时段",max_digits=20,decimal_places=4,default=0)

    #调整后
    adjust_plan_common_mth_1= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_1= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_1= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_1= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)

    adjust_plan_common_mth_2= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_2= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_2= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_2= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)


    adjust_plan_common_mth_3= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_3= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_3= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_3= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)


    adjust_plan_common_mth_4= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_4= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_4= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_4= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)


    adjust_plan_common_mth_5= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_5= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_5= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_5= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)


    adjust_plan_common_mth_6= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_6= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_6= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_6= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)

    adjust_plan_common_mth_7= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_7= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_7= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_7= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)


    adjust_plan_common_mth_8= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_8= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_8= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_8= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)


    adjust_plan_common_mth_9= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_9= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_9= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_9= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)


    adjust_plan_common_mth_10= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_10= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_10= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_10= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)

    adjust_plan_common_mth_11= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_11= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_11= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_11= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)


    adjust_plan_common_mth_12= models.DecimalField("计划电量调整-常规",max_digits=20,decimal_places=4,default=0)
    adjust_plan_flat_mth_12= models.DecimalField("计划电量调整-平时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_valley_mth_12= models.DecimalField("计划电量调整-谷时段",max_digits=20,decimal_places=4,default=0)
    adjust_plan_peak_mth_12= models.DecimalField("计划电量调整-峰时段",max_digits=20,decimal_places=4,default=0)

    state = models.CharField("状态",max_length=40,default="draft")
    note = models.TextField("备注",null=True,blank=True)


class MthCustomerBill(models.Model):
    """月度电量结算单主表 

    Args:
        models (_type_): _description_
    """
    organization = models.ForeignKey(Organization, verbose_name="所属机构",null=True,on_delete=models.SET_NULL)
    mth = models.CharField("月份",max_length=7,default=default_last_mth)

    state = models.CharField("状态",max_length=40,default="draft")

    note = models.TextField("备注",null=True,blank=True)
    created_by = models.ForeignKey(HasuraUser, verbose_name="录入人",null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField("录入时间", default=default_cur_datetime)

    updated_by = models.ForeignKey(HasuraUser, verbose_name="更新人",related_name="+",null=True,on_delete=models.SET_NULL)
    updated_at = models.DateTimeField("更新时间", default=default_cur_datetime)



class MthCustomerBillLine(models.Model):
    """月度电量结算单明细

    Args:
        models (_type_): _description_
    """
    mth_customer_bill= models.ForeignKey(MthCustomerBill, verbose_name="月度电量结算单主表",on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, verbose_name="关联客户",null=True,on_delete=models.SET_NULL)

    contract = models.ForeignKey(Contract, verbose_name="关联合同",null=True,on_delete=models.SET_NULL)
    # contract_name = models.CharField("合同名称",max_length=40)
    #结算电量
    act_common= models.DecimalField("月结算电量-常规",max_digits=20,decimal_places=4,default=0)
    act_flat= models.DecimalField("月结算电量-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley= models.DecimalField("月结算电量-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak= models.DecimalField("月结算电量-峰时段",max_digits=20,decimal_places=4,default=0)

    #结算价格
    price_common = models.DecimalField("常规时段电价(元/KWA)",max_digits=20,decimal_places=4,default=0)
    price_peak = models.DecimalField("峰时段电价(元/KWA)",max_digits=20,decimal_places=4,default=0)
    price_flat= models.DecimalField("平时段电价(元/KWA)",max_digits=20,decimal_places=4,default=0)
    price_valley = models.DecimalField("谷时段电价(元/KWA)",max_digits=20,decimal_places=4,default=0)

    service_rate = models.DecimalField("代理服务费比例",max_digits=20,decimal_places=4,default=0)
    service_fee = models.DecimalField("代理服务费",max_digits=20,decimal_places=4,default=0)

    state = models.CharField("状态",max_length=40,default="draft")
    note = models.TextField("备注",null=True,blank=True)
    created_by = models.ForeignKey(HasuraUser, verbose_name="录入人",null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField("录入时间", default=default_cur_datetime)

    updated_by = models.ForeignKey(HasuraUser, verbose_name="更新人",related_name="+",null=True,on_delete=models.SET_NULL)
    updated_at = models.DateTimeField("更新时间", default=default_cur_datetime)



class MthAgentBill(models.Model):
    """月度电量居间结算单主表 

    Args:
        models (_type_): _description_
    """
    organization = models.ForeignKey(Organization, verbose_name="所属机构",null=True,on_delete=models.SET_NULL)
    mth = models.CharField("月份",max_length=7,default=default_last_mth)

    state = models.CharField("状态",max_length=40,default="draft")

    note = models.TextField("备注",null=True,blank=True)
    created_by = models.ForeignKey(HasuraUser, verbose_name="录入人",null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField("录入时间", default=default_cur_datetime)

    updated_by = models.ForeignKey(HasuraUser, verbose_name="更新人",related_name="+",null=True,on_delete=models.SET_NULL)
    updated_at = models.DateTimeField("更新时间", default=default_cur_datetime)



class MthAgentBillLine(models.Model):
    """月度电量结算单明细

    Args:
        models (_type_): _description_
    """
    mth_agent_bill= models.ForeignKey(MthAgentBill, verbose_name="月度电量结算单主表",on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, verbose_name="居间",null=True,on_delete=models.SET_NULL)

    customer = models.ForeignKey(Customer, verbose_name="关联客户",null=True,on_delete=models.SET_NULL)
    contract = models.ForeignKey(Contract, verbose_name="关联合同",null=True,on_delete=models.SET_NULL)
 
    #结算电量
    act_common= models.DecimalField("月结算电量-常规",max_digits=20,decimal_places=4,default=0)
    act_flat= models.DecimalField("月结算电量-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley= models.DecimalField("月结算电量-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak= models.DecimalField("月结算电量-峰时段",max_digits=20,decimal_places=4,default=0)

    #结算价格
    price_common = models.DecimalField("常规时段电价(元/KWA)",max_digits=20,decimal_places=4,default=0)
    price_peak = models.DecimalField("峰时段电价(元/KWA)",max_digits=20,decimal_places=4,default=0)
    price_flat= models.DecimalField("平时段电价(元/KWA)",max_digits=20,decimal_places=4,default=0)
    price_valley = models.DecimalField("谷时段电价(元/KWA)",max_digits=20,decimal_places=4,default=0)

    service_rate = models.DecimalField("代理服务费比例",max_digits=20,decimal_places=4,default=0)
    service_fee = models.DecimalField("代理服务费",max_digits=20,decimal_places=4,default=0)

    agent_rate = models.DecimalField("居间分成比例",max_digits=20,decimal_places=4,default=0)
    agent_fee = models.DecimalField("居间分成金额",max_digits=20,decimal_places=4,default=0)
    tax_diff = models.DecimalField("增值税差额",max_digits=20,decimal_places=4,default=0)
    act_agent_fee= models.DecimalField("实际结算居间分成费",max_digits=20,decimal_places=4,default=0)


    agent_confirm_date= models.DateField("居间确认时间",null=True,blank=True, default=default_cur_date)

    state = models.CharField("状态",max_length=40,default="draft")
    note = models.TextField("备注",null=True,blank=True)

    created_by = models.ForeignKey(HasuraUser, verbose_name="录入人",null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField("录入时间", default=default_cur_datetime)

    updated_by = models.ForeignKey(HasuraUser, verbose_name="更新人",related_name="+",null=True,on_delete=models.SET_NULL)
    updated_at = models.DateTimeField("更新时间", default=default_cur_datetime)



class MthDraftCustomerBill(models.Model):
    """月度电量确认单主表 

    Args:
        models (_type_): _description_
    """
    organization = models.ForeignKey(Organization, verbose_name="所属机构",null=True,on_delete=models.SET_NULL)
    mth = models.CharField("月份",max_length=7,default=default_last_mth)

    state = models.CharField("状态",max_length=40,default="draft")

    note = models.TextField("备注",null=True,blank=True)
    created_by = models.ForeignKey(HasuraUser, verbose_name="录入人",null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField("录入时间", default=default_cur_datetime)

    updated_by = models.ForeignKey(HasuraUser, verbose_name="更新人",related_name="+",null=True,on_delete=models.SET_NULL)
    updated_at = models.DateTimeField("更新时间", default=default_cur_datetime)



class MthDraftCustomerBillLine(models.Model):
    """月度电量确认单明细

    Args:
        models (_type_): _description_
    """
    mth_draft_customer_bill= models.ForeignKey(MthDraftCustomerBill, verbose_name="月度电量确认单主表",on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, verbose_name="关联客户",null=True,on_delete=models.SET_NULL)
    customer_device_no = models.CharField("户号",max_length=40)

   
    #结算电量
    act_common= models.DecimalField("月结算电量-常规",max_digits=20,decimal_places=4,default=0)
    act_flat= models.DecimalField("月结算电量-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley= models.DecimalField("月结算电量-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak= models.DecimalField("月结算电量-峰时段",max_digits=20,decimal_places=4,default=0)
    state = models.CharField("状态",max_length=40,default="draft")
    note = models.TextField("备注",null=True,blank=True)

    created_by = models.ForeignKey(HasuraUser, verbose_name="录入人",null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField("录入时间", default=default_cur_datetime)

    updated_by = models.ForeignKey(HasuraUser, verbose_name="更新人",related_name="+",null=True,on_delete=models.SET_NULL)
    updated_at = models.DateTimeField("更新时间", default=default_cur_datetime)


class MthDiffCustomerBill(models.Model):
    """月度电量偏差控制主表 

    Args:
        models (_type_): _description_
    """
    organization = models.ForeignKey(Organization, verbose_name="所属机构",null=True,on_delete=models.SET_NULL)
    mth = models.CharField("月份",max_length=7,default=default_last_mth)

    state = models.CharField("状态",max_length=40,default="draft")

    note = models.TextField("备注",null=True,blank=True)
    created_by = models.ForeignKey(HasuraUser, verbose_name="录入人",null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField("录入时间", default=default_cur_datetime)

    updated_by = models.ForeignKey(HasuraUser, verbose_name="更新人",related_name="+",null=True,on_delete=models.SET_NULL)
    updated_at = models.DateTimeField("更新时间", default=default_cur_datetime)



    
class MthDiffCustomerBillLine(models.Model):
    """月度电量偏差控制表明细

    Args:
        models (_type_): _description_
    """
    mth_diff_customer_bill= models.ForeignKey(MthDiffCustomerBill, verbose_name="月度电量偏差控制主表",on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, verbose_name="关联客户",null=True,on_delete=models.SET_NULL)
    customer_device_no = models.CharField("户号",max_length=40)

    #计划电量
    plan_common= models.DecimalField("调整前计划电量-常规",max_digits=20,decimal_places=4,default=0)
    plan_flat= models.DecimalField("调整前计划电量-平时段",max_digits=20,decimal_places=4,default=0)
    plan_valley= models.DecimalField("调整前计划电量-谷时段",max_digits=20,decimal_places=4,default=0)
    plan_peak= models.DecimalField("调整前计划电量-峰时段",max_digits=20,decimal_places=4,default=0)


    #结算电量
    act_common= models.DecimalField("月结算电量-常规",max_digits=20,decimal_places=4,default=0)
    act_flat= models.DecimalField("月结算电量-平时段",max_digits=20,decimal_places=4,default=0)
    act_valley= models.DecimalField("月结算电量-谷时段",max_digits=20,decimal_places=4,default=0)
    act_peak= models.DecimalField("月结算电量-峰时段",max_digits=20,decimal_places=4,default=0)

    state = models.CharField("状态",max_length=40,default="draft")
    note = models.TextField("备注",null=True,blank=True)
    created_by = models.ForeignKey(HasuraUser, verbose_name="录入人",null=True,on_delete=models.SET_NULL)
    created_at = models.DateTimeField("录入时间", default=default_cur_datetime)

    updated_by = models.ForeignKey(HasuraUser, verbose_name="更新人",related_name="+",null=True,on_delete=models.SET_NULL)
    updated_at = models.DateTimeField("更新时间", default=default_cur_datetime)


