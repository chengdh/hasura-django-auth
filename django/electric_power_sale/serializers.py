from rest_framework import serializers
from .models import Customer,Agent,Contract,ContractLine
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

    class Meta:
        model = Contract 
        fields = ["name" ,"organization" ,"customer" ,"contract_no" ,"contract_year" ,"contract_start_date" ,"lines","contract_end_date" ,"contract_price_type" ,"price_common" ,"price_peak" ,"price_flat" ,"price_valley" ,"state"] 