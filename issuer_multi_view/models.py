from django.db import models
from django.core.urlresolvers import reverse

OPTIONS = [("single family", "Single Family"), ("multifamily", "Multifamily"), ("single and multifamily", "Single and multifamily"), ("enrolment administrator", "Enrolment administrator"), ]
class Issuer(models.Model):
    name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    initial_password = models.CharField("Password", max_length=100)
    initial_role = models.CharField(max_length=100, choices=OPTIONS)
    company_name = models.CharField(max_length=100)
    approval = models.BooleanField(default=True)

    def __str__(self):
       return str(self.id)

    #def __unicode__(self):
    #   return str(self.id)

    def get_absolute_url(self):
       return reverse('issuer_multi_view:issuer_edit', kwargs={'pk': self.pk})


    class Meta:
        managed = False
        db_table = 'issuer_multi_view_issuer'
        app_label = 'issuer_multi_view'

OPTIONS_pool_type = [("single family", "Single Family"), ("multifamily", "Multifamily"),]
class Pool(models.Model):
    poolType= models.CharField("Pool Type", max_length=100, choices=OPTIONS_pool_type)
    numberOfLoans= models.IntegerField
    mortgageInterstRate= models.CharField(max_length=100)
    securityInterestRate= models.CharField(max_length=100)
    IssueDate= models.CharField(max_length=100)
    maturityDate= models.CharField(max_length=100)
    issuerId= models.ForeignKey('Issuer', models.DO_NOTHING)

    def __unicode__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('issuer_multi_view:pool_edit', kwargs={'pk': self.pk})


    class Meta:
        managed = False
        db_table = 'issuer_multi_view_pool'
        app_label = 'issuer_multi_view'

class Loan (models.Model):
    loanNum= models.IntegerField(primary_key= True)
    poolId = models.ForeignKey(Pool)
    issuerId= models.ForeignKey(Issuer)
    activityDate= models.CharField(max_length=100)
    loanInterestRate= models.CharField(max_length=100)
    totalAmount= models.CharField(max_length=100)
    outstandingAmount= models.CharField(max_length=100)

    def __unicode__(self):
       return str(self.poolId)

    def get_absolute_url(self):
        return reverse('issuer_multi_view:pool_view', kwargs={'pk': self.pk})


    class Meta:
        managed = False
        db_table = 'issuer_multi_view_loan'
        app_label = 'issuer_multi_view'
