from django.shortcuts import render
from django.views import generic
from .models import Student, Course, Payment, Rank, RankRecord, RankRequirement, Parent


# index page
def index(request):
    return render(request, 'skf/index.html')


# students page
class StudentView(generic.ListView):
    context_object_name = "students"
    template_name = 'skf/student.html'

    def get_queryset(self):
        return Student.objects.all()


class StuParentView(generic.ListView):
    context_object_name = "parents"
    template_name = 'skf/parent.html'

    def get_queryset(self):
        stu_num = self.kwargs['student_num']
        return Student.objects.get(student_num=stu_num).parent_set.all()


class StuCourseView(generic.ListView):
    context_object_name = "courses"
    template_name = 'skf/course.html'

    def get_queryset(self):
        stu_num = self.kwargs['student_num']
        return Student.objects.get(student_num=stu_num).course_set.all()


class StuRankView(generic.ListView):
    context_object_name = "ranks"
    template_name = 'skf/rank.html'

    def get_queryset(self):
        stu_num = self.kwargs['student_num']
        return Student.objects.get(student_num=stu_num).rank_set.all()


class StuPaymentView(generic.ListView):
    context_object_name = "payments"
    template_name = 'skf/payment.html'

    def get_queryset(self):
        stu_num = self.kwargs['student_num']
        return Student.objects.get(student_num=stu_num).payment_set.all()


# course page
class CourseView(generic.ListView):
    context_object_name = "courses"
    template_name = 'skf/course.html'

    def get_queryset(self):
        return Course.objects.all()


class CouStudentView(generic.ListView):
    context_object_name = "students"
    template_name = 'skf/student.html'

    def get_queryset(self):
        cou_id = self.kwargs['pk']
        return Student.objects.filter(course__id=cou_id)


# rank page
class RankView(generic.ListView):
    context_object_name = "ranks"
    template_name = 'skf/rank.html'

    def get_queryset(self):
        return Rank.objects.all()


class RanRequirementView(generic.ListView):
    context_object_name = "rank_requirements"
    template_name = 'skf/rank_requirement.html'

    def get_queryset(self):
        rank_name = self.kwargs['rank_name']
        return Rank.objects.get(name=rank_name).rankrequirement_set.all()


class RanStudentView(generic.ListView):
    context_object_name = "students"
    template_name = 'skf/student.html'

    def get_queryset(self):
        rank_name = self.kwargs['rank_name']
        return Student.objects.filter(rank__name=rank_name)


# parent page
class ParentView(generic.ListView):
    context_object_name = "parents"
    template_name = 'skf/parent.html'

    def get_queryset(self):
        return Parent.objects.all()


class ParStudentView(generic.ListView):
    context_object_name = "students"
    template_name = 'skf/student.html'

    def get_queryset(self):
        parent_id = self.kwargs['pk']
        return Student.objects.filter(parent__id=parent_id)


# payment page
class PaymentView(generic.ListView):
    context_object_name = "payments"
    template_name = 'skf/payment.html'

    def get_queryset(self):
        return Payment.objects.all()


class PayStudentView(generic.ListView):
    context_object_name = "students"
    template_name = 'skf/student.html'

    def get_queryset(self):
        payment_id = self.kwargs['pk']
        return Student.objects.filter(payment__id=payment_id)


# student record page
class RankRecordView(generic.ListView):
    context_object_name = "rank_records"
    template_name = 'skf/rank_record.html'

    def get_queryset(self):
        return RankRecord.objects.all()


class RRStudentView(generic.ListView):
    context_object_name = "students"
    template_name = 'skf/student.html'

    def get_queryset(self):
        rrecord_id = self.kwargs['pk']
        return Student.objects.filter(rankrecord__id=rrecord_id)


class RRRankView(generic.ListView):
    context_object_name = "ranks"
    template_name = 'skf/rank.html'

    def get_queryset(self):
        rrecord_id = self.kwargs['pk']
        return Rank.objects.filter(rankrecord__id=rrecord_id)


# rank requirement page
class RankRequirementView(generic.ListView):
    context_object_name = "rank_requirements"
    template_name = 'skf/rank_requirement.html'

    def get_queryset(self):
        return RankRequirement.objects.all()


class RReqRankView(generic.ListView):
    context_object_name = "ranks"
    template_name = 'skf/rank.html'

    def get_queryset(self):
        rreq_id = self.kwargs['pk']
        return Rank.objects.filter(rankrequirement__id=rreq_id)
