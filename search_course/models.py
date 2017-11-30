from django.db import models
from multiselectfield import MultiSelectField

am = 'a'
pm = 'p'
am_pm = (('a', 'am'), ('p', 'pm'))
hours = tuple((str(i).zfill(2), str(i).zfill(2)) for i in range(13))
minutes = tuple((str(i*5).zfill(2), str(i*5).zfill(2)) for i in range(12))
attribute_type = (
    ("%", 'All'),
    ("COOP", 'Coop'),
    ("CTL", 'Core Transfer Library'),
    ("CREX", 'Credit By Exam'),
    ("DPCR", 'Dept Credit'),
    ("DUAL", 'Dual Credit Transfer Work'),
    ("FTPV", 'Full-Time Privileges'),
    ("TC05", 'GTC-Humanistic-Artistic'),
    ("TC07", 'GTC-Information Literacy'),
    ("TC04", 'GTC-Quantitative Reasoning'),
    ("TC03", 'GTC-Science'),
    ("TC08", 'GTC-Science, Tech &amp; Society'),
    ("TC06", 'GTC-Social-Behavioral'),
    ("TC02", 'GTC-Speaking &amp; Listening'),
    ("TC01", 'GTC-Written Communication'),
    ("HONR", 'Honors'),
    ("IMPC", 'Impact Courses'),
    ("INTR", 'Internship'),
    ("LOWR", 'Lower Division'),
    ("MILT", 'Military'),
    ("PCOP", 'Parallel Coop'),
    ("PRCT", 'Practicum'),
    ("REMD", 'Remedial'),
    ("S01", 'S General Education'),
    ("S03", 'S Language &amp; Culture'),
    ("SL", 'Service Learning'),
    ("SGNL", 'Signal Courses'),
    ("STCH", 'Student Teaching'),
    ("TRIN", 'TransferIN'),
    ("UC06", 'UC-Behavior/Social Science'),
    ("UC05", 'UC-Humanities'),
    ("UC02", 'UC-Information Literacy'),
    ("UC03", 'UC-Oral Communications'),
    ("UC07", 'UC-Quantitative Reasoning'),
    ("UC04", 'UC-Science'),
    ("UC08", 'UC-Science, Tech &amp; Society'),
    ("UC01", 'UC-Written Communication'),
    ("UPPR", 'Upper Division'),
    ("VART", 'Variable Title'),
)

schedule_type = (
    ("%" , 'All'),
    ("CLN", 'Clinic'),
    ("DIS", 'Distance Learning'),
    ("EX", 'Experiential'),
    ("IND", 'Individual Study'),
    ("LAB", 'Laboratory'),
    ("LBP", 'Laboratory Preparation'),
    ("LEC", 'Lecture'),
    ("PSO", 'Practice Study Observation'),
    ("PRS", 'Presentation'),
    ("REC", 'Recitation'),
    ("RES", 'Research'),
    ("SD", 'Studio'),
)

instructional_method = (
    ("%",'All'),
    ("B/H", 'Hybrid'),
    ("DO", 'Online'),
    ("DPO", 'Primarily Online'),
)

campus = (
    ("%" , 'All'),
    ("ICN", 'Indiana College Network'),
    ("TLF", 'Lafayette'),
    ("PWL", 'West Lafayette'),
    ("CEC", 'West Lafayette Continuing Ed'),
)

part_of_term = (
    ("%", 'All'),
    ("F8", 'First 8 Weeks'),
    ("1", 'Full Term'),
    ("LF", 'Lafayette'),
    ("S8", 'Second 8 Weeks'),
)

session = (
    ("%", 'All'),
    ("D", 'Day'),
    ("E", 'Evening'),
    ("I", 'Indiana College Network'),
    ("W", 'Weekend'),
)

days = (
    ('m', "Monday"),
    ('t', "Tuesday"),
    ('w', "Wednsay"),
    ('th', "Thursday"),
    ('f', "Friday"),
)
# Create your models here.
class User(models.Model):
    default_list = "['dummy', '%']"
    email = models.EmailField()


    begin_ap = models.CharField(max_length=1, choices=am_pm, default=am)
    begin_hh = models.CharField(max_length=2, choices=hours, default='00')
    begin_mi = models.CharField(max_length=2, choices=minutes, default='00')
    end_ap = models.CharField(max_length=1, choices=am_pm, default=am)
    end_hh = models.CharField(max_length=2, choices=hours, default='00')
    end_mi = models.CharField(max_length=2, choices=minutes, default='00')
    
    # list of strings
    sel_attr = models.CharField(max_length=50, choices=attribute_type, default='%')
    sel_camp = models.CharField(max_length=50, choices=campus, default='%')
    # sel_day = MultiSelectField(choices=days, default='%')
    sel_insm = models.CharField(max_length=50, choices=instructional_method, default='%')
    # sel_instr = models.CharField(max_length=100, null=True, default=default_list)    
    sel_ptrm = models.CharField(max_length=50, choices=part_of_term, default='%')
    sel_schd = models.CharField(max_length=50, choices=schedule_type, default='%')
    sel_sess = models.CharField(max_length=50, choices=session, default='%')
    sel_subj = models.CharField(max_length=50)
    
    sel_title = models.CharField(max_length=100, blank=True)
    sel_crse = models.CharField(max_length=10)
    
    sel_from_cred = models.CharField(max_length=2, blank=True)
    sel_to_cred = models.CharField(max_length=2,blank=True)

    def __str__(self):
        return self.email
