from django.contrib import admin
from .models import Student, Parent, Payment, Rank, RankRecord, RankRequirement, Course

# Register your models here.
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Course)
admin.site.register(Rank)
admin.site.register(RankRecord)
admin.site.register(RankRequirement)
admin.site.register(Payment)