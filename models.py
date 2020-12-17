from django.db import models


class rules(models.Model):
    rule_id = models.IntegerField()
    project_id = models.IntegerField()
    
    rules=models.CharField(max_length=30)
    def __str__(self):
        return self.rules



class project(models.Model):
    project_id = models.IntegerField()
    project_name=models.CharField(max_length=50)
    user_id = models.IntegerField()
    type_of_project=models.CharField(max_length=50)
    project_details=models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.project_name+' '+self.type_of_project+' '+self.project_details
class user(models.Model):
    user_id = models.IntegerField()
    user_name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    proj=models.ForeignKey(project,related_name='users', on_delete =models.CASCADE)
    rule=models.ForeignKey(rules,related_name='users', on_delete =models.CASCADE)
    
    def __str__(self):
        return self.user_name+' '+self.email