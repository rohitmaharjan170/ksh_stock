from django.db import models
from django.conf import settings


class PersonalInfos(models.Model):
    personal_id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    dp_boid = models.CharField(max_length=16) 
    crn = models.CharField(max_length=10) 
    tms = models.CharField(max_length=10) 
    email = models.CharField(max_length=60) 


class MemberTypes(models.Model):
    member_type_id = models.AutoField(primary_key=True, editable=False)
    member_type_description = models.CharField(max_length=50)
    member_type_status = models.BooleanField(default=True)

    #found coutom id in stackoverflow, may be its for unique and retuning unique id i guess
    # @property
    # def s_member_type_id(self):
    #     return "A%05d" % self.member_type_id


class Members(models.Model):
    member_id = models.AutoField(primary_key=True, editable=False)
    personnel = models.ForeignKey('PersonalInfos', on_delete=models.CASCADE)
    member_type = models.ForeignKey('MemberTypes', on_delete=models.CASCADE)

class ScriptCategories(models.Model):
    script_category_id = models.AutoField(primary_key=True, editable=False)
    script_category = models.CharField(max_length=50)



class Scripts(models.Model):
    script_id = models.AutoField(primary_key=True, editable=False)
    symbol = models.CharField(max_length=5)
    script_description = models.CharField(max_length=50)
    category = models.ForeignKey('ScriptCategories', on_delete=models.CASCADE)
    estd_date = models.DateField()


class MemberStocks(models.Model):
    member_stock_id = models.AutoField(primary_key=True, editable=False)
    personnel = models.ForeignKey('PersonalInfos', on_delete=models.CASCADE)
    member = models.ForeignKey('Members', on_delete=models.CASCADE)
    symbol = models.ForeignKey('Scripts', on_delete=models.CASCADE)
    qty = models.IntegerField()
    buy_date = models.DateField()
    sell_date = models.DateField()
    buy_rate = models.IntegerField()
    sell_rate = models.IntegerField()



class TaxCharges(models.Model):
    tax_charge_id = models.AutoField(primary_key=True, editable=False)
    tax_charge_type = models.CharField(max_length=20)
    tax_charge_description = models.CharField(max_length=50)
    porf = models.CharField(max_length=20)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    from_date = models.DateField()
    to_date = models.DateField()
