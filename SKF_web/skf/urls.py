from django.conf.urls import url
from . import views

app_name = 'skf'

urlpatterns = [
    # index page
    url(r'^$', views.index, name='index'),
    # student page
    url(r'^student/$', views.StudentView.as_view(), name='student'),
    url(r'^student/parent/(?P<student_num>\w+)/$', views.StuParentView.as_view(), name='stu_parent'),
    url(r'^student/course/(?P<student_num>\w+)/$', views.StuCourseView.as_view(), name='stu_course'),
    url(r'^student/rank/(?P<student_num>\w+)/$', views.StuRankView.as_view(), name='stu_rank'),
    url(r'^student/payment/(?P<student_num>\w+)/$', views.StuPaymentView.as_view(), name='stu_payment'),
    # course page
    url(r'^course/$', views.CourseView.as_view(), name='course'),
    url(r'^course/student/(?P<pk>[0-9]+)/$', views.CouStudentView.as_view(), name='cou_student'),
    # payment page
    url(r'^payment/$', views.PaymentView.as_view(), name='payment'),
    url(r'^payment/student/(?P<pk>[0-9]+)/$', views.PayStudentView.as_view(), name='pay_student'),
    # parent page
    url(r'^parent/$', views.ParentView.as_view(), name='parent'),
    url(r'^parent/student/(?P<pk>[0-9]+)/$', views.ParStudentView.as_view(), name='par_student'),
    # rank  page
    url(r'^rank/$', views.RankView.as_view(), name='rank'),
    url(r'^rank/requirement/(?P<rank_name>\w+)/$', views.RanRequirementView.as_view(), name='ran_requirement'),
    url(r'^rank/student/(?P<rank_name>\w+)/$', views.RanStudentView.as_view(), name='ran_student'),
    # rank record page
    url(r'^rank_record/$', views.RankRecordView.as_view(), name='rank_record'),
    url(r'^rank_record/student/(?P<pk>[0-9]+)/$', views.RRStudentView.as_view(), name='rr_student'),
    url(r'^rank_record/rank/(?P<pk>[0-9]+)/$', views.RRRankView.as_view(), name='rr_rank'),
    # rank requirement page
    url(r'^rank_requirement/$', views.RankRequirementView.as_view(), name='rank_requirement'),
    url(r'^rank_requirement/rank/(?P<pk>[0-9]+)/$', views.RReqRankView.as_view(), name='rreq_rank'),

]
