from django.db import models

# Create your models here.

class University(models.Model):
    Rank_in_2020 = models.CharField(max_length=10)
    Rank_in_2019 = models.CharField(max_length=10)
    Institution_Name = models.CharField(max_length=50)
    Country = models.CharField(max_length=30)
    Classification_SIZE = models.CharField(max_length=3)
    Classification_FOCUS = models.CharField(max_length=3)
    Classification_RESEARCH_INTENSITY = models.CharField(max_length=3)
    Classification_AGE = models.IntegerField()
    Classification_STATUS = models.CharField(max_length=8)
    Academic_Reputation_SCORE = models.IntegerField()
    Academic_Reputation_RANK = models.CharField(max_length=8)
    Employer_Reputation_SCORE = models.IntegerField()
    Employer_Reputation_RANK = models.CharField(max_length=8)
    Faculty_Student_SCORE = models.IntegerField()
    Faculty_Student_RANK = models.CharField(max_length=8)
    Citations_per_Faculty_SCORE = models.IntegerField()
    Citations_per_Faculty_RANK = models.CharField(max_length=8)
    International_Faculty_SCORE = models.IntegerField()
    International_Faculty_RANK = models.CharField(max_length=8)
    International_Students_SCORE = models.IntegerField()
    International_Students_RANK = models.CharField(max_length=8)

    class Meta:
        db_table = '2020-QS-World-University-Rankings_CLEANED'

    def __str__(self):
        return self.Institution_Name
