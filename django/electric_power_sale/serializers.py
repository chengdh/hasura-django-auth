from rest_framework import serializers
from .models import Customer
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