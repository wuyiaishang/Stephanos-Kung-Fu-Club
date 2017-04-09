from django.db import models


COMODITIES = (
    ('Produt', 'Product'),
    ('Membership', 'Membership'),
    ('Test', 'Test'),
)

WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday')
)

TIME = (
    ('8:00 am', '8:00 am'),
    ('9:00 am', '9:00 am'),
    ('10:00 am', '10:00 am'),
    ('11:00 am', '11:00 am'),
    ('12:00 pm', '12:00 pm'),
    ('1:00 pm', '1:00 pm'),
    ('2:00 pm', '2:00 pm'),
    ('3:00 pm', '3:00 pm'),
    ('4:00 pm', '4:00 pm'),
    ('5:00 pm', '5:00 pm'),
    ('6:00 pm', '6:00 pm'),
    ('7:00 pm', '7:00 pm'),
    ('8:00 pm', '8:00 pm'),
    ('9:00 pm', '9:00 pm'),
)

LEVEL = (
    ('Primary', 'Primary'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
)

# students table  source model
class Student(models.Model):
    student_num = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=500)
    # date of birth
    dob = models.DateField(editable=True, blank=True)
    # date of joining to school
    djs = models.DateField(editable=True, blank=True)
    mobile = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name + '-' + self.student_num


# parent table (many to many with Student)
class Parent(models.Model):
    students = models.ManyToManyField(Student)
    name = models.CharField(max_length=500)
    relation = models.CharField(max_length=500)
    mobile = models.CharField(max_length=500)
    email = models.CharField(max_length=500)

    def __str__(self):
        return self.name + '-' + self.relation


# payment table (many to one with Student)
class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    money = models.CharField(max_length=500)
    commodity = models.CharField(max_length=500, choices=COMODITIES, default="Product")
    sdate = models.DateField(editable=True, blank=True)
    edate = models.DateField(editable=True, blank=True)

    def __str__(self):
        return self.student.name + '-' + self.commodity


# course table (many to many with Student)
class Course(models.Model):
    students = models.ManyToManyField(Student)
    level = models.CharField(max_length=500, choices=LEVEL, default="Primary")
    week = models.CharField(max_length=500, choices=WEEK, default="Monday")
    time = models.CharField(max_length=500, choices=TIME, default="8:00 am")

    def __str__(self):
        return self.level + '-' + self.week + '-' + self.time


# rank table (extra many to many with Student) target model
class Rank(models.Model):
    student = models.ManyToManyField(Student, through='RankRecord')
    name = models.CharField(max_length=500, primary_key=True)
    bcolor = models.CharField(max_length=500)

    def __str__(self):
        return self.name + ' level' + '-' + self.bcolor


# intermediate class between Rank and Student
class RankRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    rdate = models.DateField(editable=True, blank=True)

    def __str__(self):
        return self.student.name + '-' + self.rank.bcolor


# rank requirement table (many to one with Rank)
class RankRequirement(models.Model):
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.rank.bcolor + '-' + self.content
