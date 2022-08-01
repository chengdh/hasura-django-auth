from django.db import models
from datetime import date

def default_cur_date():
    return date.today()


class Partner(models.Model):
    """合伙人
    """
    name = models.CharField("姓名",max_length=60,null=True,blank=True)
    mobile = models.CharField("手机",max_length=20)
    email = models.CharField("邮箱",max_length=60,null=True,blank=True)
    note = models.CharField("编号",null=True,blank=True,max_length=60)
 
class Developer(models.Model):
    """创业者
    """
    name = models.CharField("姓名",max_length=60,null=True,blank=True)
    mobile = models.CharField("手机",max_length=20)
    email = models.CharField("邮箱",max_length=60,null=True,blank=True)
    note = models.TextField("备注",null=True,blank=True,max_length=60)

class Schedule(models.Model): 
    """合伙人日程表
    """
    partner = models.ForeignKey(Partner, verbose_name="合伙人",on_delete=models.CASCADE)
    schedule_date = models.DateField("日期",auto_now_add = True)
    note = models.TextField("编号",null=True,blank=True,max_length=60)

class ScheduleLine(models.Model): 
    """合伙人日程表明细
    """
    schedule = models.ForeignKey(Schedule, verbose_name="日程表",on_delete=models.CASCADE)

    #选用整形,前端用moment做转换
    from_time = models.CharField("开始时间",max_length=30)
    to_time = models.CharField("结束时间",max_length=30)

    #状态:已确定/已预定/合伙人已取消/创业者已取消/合伙人已确认
    state = models.CharField("状态",null=True,blank=True,max_length=60)
    developer = models.ForeignKey(Developer, verbose_name="创业者",null=True,blank=True,on_delete=models.SET_NULL)