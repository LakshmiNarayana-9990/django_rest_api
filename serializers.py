from rest_framework import serializers

from .models import user,project,rules

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ('user_id', 'user_name','email')
class projectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = project
        fields = ('project_id','project_name','user_id', 'type_of_project','project_details')
class rulesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = rules
        fields = ('rule_id', 'project_id','rules')
