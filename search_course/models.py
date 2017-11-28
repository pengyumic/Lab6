from django.db import models

# Create your models here.
class User(models.Model):
    default_list = "['dummy', '%']"
    email = models.EmailField()

    begin_ap = models.CharField(max_length=1)
    begin_hh = models.CharField(max_length=2)
    begin_mi = models.CharField(max_length=2)
    end_ap = models.CharField(max_length=1)
    end_hh = models.CharField(max_length=2)
    end_mi = models.CharField(max_length=2)
    
    # list of strings
    sel_attr = models.CharField(max_length=50, null=True, default=default_list)
    sel_camp = models.CharField(max_length=50, null=True, default=default_list)
    sel_day = models.CharField(max_length=50, null=True, default=default_list)
    sel_insm = models.CharField(max_length=50, null=True, default=default_list)
    sel_instr = models.CharField(max_length=100, null=True, default=default_list)
    sel_levl = models.CharField(max_length=50, null=True, default=default_list)
    sel_ptrm = models.CharField(max_length=50, null=True, default=default_list)
    sel_schd = models.CharField(max_length=50, null=True, default=default_list)
    sel_sess = models.CharField(max_length=50, null=True, default=default_list)
    sel_subj = models.CharField(max_length=50, null=True, default=default_list)
    
    sel_title = models.CharField(max_length=100, blank=True)
    sel_crse = models.CharField(max_length=10)
    
    sel_from_cred = models.CharField(max_length=2, blank=True)
    sel_to_cred = models.CharField(max_length=2,blank=True)

    def __str__(self):
        return self.email
