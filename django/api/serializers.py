from .models import HasuraUser,FunctionCategory, Organization,SystemFunction,SystemFunctionOperate,Role,Organization 
from rest_framework import serializers

class OrganizationSerializer(serializers.ModelSerializer):
    """系统功能
    """
    class Meta:
        model = Organization 
        fields = ["id","name","address","parent_org","is_active" ]


class FunctionCategorySerializer(serializers.ModelSerializer):
    """功能类别
    """
    # children = SystemFunctionSerializer(many = True)
    class Meta:
        model = FunctionCategory
        fields = ["id","name","icon","is_active","rank" ]

class SystemFunctionOperateSerializer(serializers.ModelSerializer):
    """系统功能操作按钮
    """
    # system_function = SystemFunctionSerializer()
    class Meta:
        model = SystemFunctionOperate
        fields = ["id","code","name","is_active","rank","note" ]


class SystemFunctionSerializer(serializers.ModelSerializer):
    """系统功能
    """
    function_category = FunctionCategorySerializer()
    operates = SystemFunctionOperateSerializer(many=True)
    class Meta:
        model = SystemFunction
        fields = ["id","name","icon","is_active","rank","function_category" ]


class RoleSerializer(serializers.ModelSerializer):
    """角色
    """
    system_function_operates = SystemFunctionOperateSerializer(many = True)
    routers = serializers.SerializerMethodField() 

    def get_routers(self,role_obj):
        """得到当前角色的权限列表
        """
        """
        routers = [] 
        system_function_operate_ids = [sfo.id for sfo in role_obj.system_function_operates.all()]
        system_function_ids = set([ sf.system_function.id for sf in role_obj.system_function_operates.all()])
        system_functions = set([ sf.system_function for sf in role_obj.system_function_operates.all()])
        function_categories = set([sf.function_category for sf in system_functions])
        for fc in function_categories:
            route = {
                "path" : fc.frontend_router_path,
                "name" : fc.frontend_router_name,
                "meta": {
                    "title": fc.frontend_router_meta_title,
                    "icon": fc.frontend_router_meta_icon,
                }
            }
            if fc.frontend_router_redirect:
                route['redirect'] = fc.frontend_router_redirect

            sf_children = []
            for sf in fc.children.filter(pk__in = system_function_ids):
                child_route = {
                    "path" : sf.frontend_router_path,
                    "name" : sf.frontend_router_name,
                    "meta": {
                        "title": sf.frontend_router_meta_title,
                        "icon": sf.frontend_router_meta_icon,
                    }
                }
                if sf.frontend_router_redirect:
                    child_route['redirect'] = sf.frontend_router_redirect


                sfo_children = []
                for sfo in sf.operates.filter(pk__in = system_function_operate_ids):
                    sfo_child = {
                        "name" : sfo.name,
                        "code" : sfo.code,
                    }
 
                    sfo_children.append(sfo_child)
                if len(sfo_children) > 0:
                    child_route["authority"] = sfo_children
 
                sf_children.append(child_route)

            if len(sf_children) > 0:
                route["children"] = sf_children
            
            routers.append(route)

    """
        return [] 

    class Meta:
        model = Role 
        fields = ["id","name","is_active","rank","note","system_function_operates","routers" ]

class HasuraUserSerializer(serializers.ModelSerializer):
    """用户信息序列化器

    Args:
        serializers (_type_): _description_
    """

    roles = RoleSerializer(many = True)
    organizations = OrganizationSerializer(many = True)
    class Meta:
        model = HasuraUser
        fields = ["pk","username","email","roles","organizations"]