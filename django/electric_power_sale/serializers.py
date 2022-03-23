from rest_framework import serializers
from .models import Customer,Agent,Contract,ContractLine,PRICE_TYPE_COMMON,PRICE_TYPE_SEPRATE_TIME

class MethodField(serializers.SerializerMethodField):
    """扩展methodField,使之可以接收其他参数
        ref https://stackoverflow.com/questions/61500411/drf-serializermethodfield-how-to-pass-parameters

    Args:
        SerializerMethodField (_type_): _description_
    """
    def __init__(self, method_name=None, **kwargs):
        # use kwargs for our function instead, not the base class

        #处理参数,保留原有field参数,将其他参数传给method
        reserv_arg_names = ["read_only","write_only","required","default","allow_null","source","validators","error_messages","label","help_text","initial","style"]
        field_args = {key: kwargs[key] for key in kwargs.keys() if key in reserv_arg_names}
        extra_args = {key: kwargs[key] for key in kwargs.keys() if not key in reserv_arg_names}
        super().__init__(method_name,**field_args) 
        self.func_kwargs = extra_args

    def to_representation(self, value):
        method = getattr(self.parent, self.method_name)
        return method(value, **self.func_kwargs)

class CustomerSerializer(serializers.ModelSerializer):
    """客户资料
    """
    transformer_type = serializers.CharField(label="变压器容量类型",source='get_transformer_type_display')
    income_type = serializers.CharField(label="收入结算方式",source='get_income_type_display')
    use_type = serializers.CharField(label="用电方式",source='get_use_type_display')
    organization = serializers.SlugRelatedField(
        label="所属机构",
        read_only=True,
        slug_field='name'
     )

    agent = serializers.SlugRelatedField(
        label="所属居间",
        read_only=True,
        slug_field='name'
     )
 
    class Meta:
        model = Customer 
        fields = ["name","organization","agent" ,"address" , "toucher_1", "toucher_mobile_1","toucher_2" , "toucher_mobile_2", "transformer_type","use_type","grid_account" , "grid_password" ,"elect_level" ,"transformer_volume","income_type", "rate" ,"fix_fee" ,"divide_rate" ,"agent_rate" ]
    
class AgentSerializer(serializers.ModelSerializer):
    """居间资料
    """
    organization = serializers.SlugRelatedField(
        label="所属机构",
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model = Agent 
        fields = [ "name" ,"organization" ,"address" ,"toucher_1" ,"toucher_2" ,"toucher_mobile_1" ,"toucher_mobile_2" ,"default_agent_rate" ,"note"] 


class ContractLineSerializer(serializers.ModelSerializer):
    """售电合同明细

    Args:
        serializers (_type_): _description_
    """
    contract = serializers.SlugRelatedField(
        label="合同",
        read_only=True,
        slug_field='name'
     )
    class Meta:
        model = ContractLine 
        fields = ["plan_common_mth_1","plan_common_mth_2","plan_common_mth3"]
     
     
 
class ContractSerializer(serializers.ModelSerializer):
    """售电合同
    """
    organization = serializers.SlugRelatedField(
        label="所属机构",
        read_only=True,
        slug_field='name'
     )
    customer = serializers.SlugRelatedField(
        label="客户",
        read_only=True,
        slug_field='name'
     )


    contract_price_type = serializers.CharField(label="计费方式",source='get_contract_price_type_display')
    state = serializers.CharField(label="合同状态",source='get_state_display')

    #定义1至12月电量数据
    mths = range(1,13)
    for mth in mths:
        str_plan_common = "plan_common_mth_{}".format(mth) 
        locals()[str_plan_common] = MethodField(label="{}月计划".format(mth),method_name="get_field_by_name_and_mth",field_name="plan_common" ,mth=mth)
        str_plan_flat = "plan_flat_mth_{}".format(mth) 
        locals()[str_plan_flat] = MethodField(label="{}月计划(平)".format(mth),method_name="get_field_by_name_and_mth",field_name="plan_flat" ,mth=mth)
        str_plan_peak = "plan_peak_mth_{}".format(mth) 
        locals()[str_plan_peak] = MethodField(label="{}月计划(峰)".format(mth),method_name="get_field_by_name_and_mth",field_name="plan_peak" ,mth=mth)
        str_plan_valley = "plan_valley_mth_{}".format(mth) 
        locals()[str_plan_valley] = MethodField(label="{}月计划(谷)".format(mth),method_name="get_field_by_name_and_mth",field_name="plan_valley" ,mth=mth)


    def get_field_by_name_and_mth(self,obj,field_name,mth):
        line = obj.contractline_set.all()[0]
        if obj.contract_price_type == PRICE_TYPE_COMMON:
            if field_name == 'plan_common':
                return getattr(line,"{}_mth_{}".format(field_name,mth))
            else:
                return "/"
        else:
            if field_name == 'plan_common':
                return "/"
            else:
                return getattr(line,"{}_mth_{}".format(field_name,mth))
     

    class Meta:
        model = Contract
        plan_common_fields = list("plan_common_mth_{}".format(mth) for mth in range(1,13))
        plan_flat_fields = list("plan_flat_mth_{}".format(mth) for mth in range(1,13))
        plan_valley_fields = list("plan_valley_mth_{}".format(mth) for mth in range(1,13))
        plan_peak_fields = list("plan_peak_mth_{}".format(mth) for mth in range(1,13))
        fields = ["name" ,"organization" ,"customer" ,"contract_no" ,"contract_year" ,"contract_start_date","contract_end_date" ,"contract_price_type" ,"price_common" ,"price_peak" ,"price_flat" ,"price_valley" ,"state"] + plan_common_fields + plan_flat_fields + plan_valley_fields + plan_peak_fields   

class MthAdjustLineSerializer(serializers.ModelSerializer):
    """月度电量调整明细
    """
    contract = serializers.SlugRelatedField(
        label="合同名称",
        read_only=True,
        slug_field='name'
     )
    customer = serializers.SlugRelatedField(
        label="客户",
        read_only=True,
        slug_field='name'
     )


    #定义1至12月电量数据
    mths = range(1,13)
    for mth in mths:
        str_plan_common = "adjust_plan_common_mth_{}".format(mth) 
        locals()[str_plan_common] = MethodField(label="{}月计划".format(mth),method_name="get_field_by_name_and_mth",field_name="plan_common" ,mth=mth)
        str_plan_flat = "adjust_plan_flat_mth_{}".format(mth) 
        locals()[str_plan_flat] = MethodField(label="{}月计划(平)".format(mth),method_name="get_field_by_name_and_mth",field_name="plan_flat" ,mth=mth)
        str_plan_peak = "adjust_plan_peak_mth_{}".format(mth) 
        locals()[str_plan_peak] = MethodField(label="{}月计划(峰)".format(mth),method_name="get_field_by_name_and_mth",field_name="plan_peak" ,mth=mth)
        str_plan_valley = "adjust_plan_valley_mth_{}".format(mth) 
        locals()[str_plan_valley] = MethodField(label="{}月计划(谷)".format(mth),method_name="get_field_by_name_and_mth",field_name="plan_valley" ,mth=mth)


    def get_field_by_name_and_mth(self,obj,field_name,mth):
        previous_plan= getattr(obj,"previous_{}_mth_{}".format(field_name,mth))
        adjust_plan= getattr(obj,"adjust_{}_mth_{}".format(field_name,mth))
        if not obj.contract:
            return "/"
        if obj.contract.contract_price_type == PRICE_TYPE_COMMON:
            if field_name == 'plan_common':
                return "计:{} / 调:{}".format(previous_plan,adjust_plan)
            else:
                return "/"
        else:
            if field_name == 'plan_common':
                return "/"
            else:
                return "计:{} / 调:{}".format(previous_plan,adjust_plan)
            

    class Meta:
        model = Contract
        adjust_plan_common_fields = list("adjust_plan_common_mth_{}".format(mth) for mth in range(1,13))
        adjust_plan_flat_fields = list("adjust_plan_flat_mth_{}".format(mth) for mth in range(1,13))
        adjust_plan_valley_fields = list("adjust_plan_valley_mth_{}".format(mth) for mth in range(1,13))
        adjust_plan_peak_fields = list("adjust_plan_peak_mth_{}".format(mth) for mth in range(1,13))
        fields = ["customer" ,"contract"] + adjust_plan_common_fields + adjust_plan_flat_fields + adjust_plan_valley_fields + adjust_plan_peak_fields
 