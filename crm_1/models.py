from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """用户信息表"""
    user=models.ForeignKey(User)
    name=models.CharField(max_length=64,verbose_name="姓名")
    role=models.ManyToManyField("Role",blank=True,null=True)


    def __str__(self):
        return self.name

class Role(models.Model):
    """角色表"""
    name = models.CharField(max_length=64, verbose_name="角色名",unique=True)


    def __str__(self):
        return self.name

class CustomerInfo(models.Model):
    """客户信息表"""
    name = models.CharField(max_length=64, verbose_name="客户名", default=None)
    contact_type_choices=((0,'qq'),(1,'微信'),(2,'手机'))
    contact_type=models.SmallIntegerField(choices=contact_type_choices,default=0)
    contact=models.CharField(max_length=64,unique=True)
    source_choices=((0,'QQ群'),(1,'51CTO'),(2,'百度推广'),(3,'知乎'),(4,'转介绍'),(5,'其他'))
    source=models.SmallIntegerField(choices=source_choices)
    referral_from=models.ForeignKey("CustomerInfo",blank=True,null=True,verbose_name="转介绍")
    consult_courses=models.ManyToManyField("Course",verbose_name="咨询课程")
    consult_content=models.TextField(verbose_name="咨询内容")
    status_choices=((0,'未报名'),(1,'已报名'),(2,'已退学'))
    status=models.SmallIntegerField(choices=status_choices)
    consultant=models.ForeignKey("UserProfile",verbose_name="课程顾问")
    date=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

class CustomerFollowUp(models.Model):
    """客户跟踪记录表"""
    customer=models.ForeignKey("CustomerInfo")
    content=models.TextField(verbose_name="跟踪内容")
    user=models.ForeignKey("UserProfile",verbose_name="跟进人")
    status_choices=(
                    (0,"近期无报名计划"),
                    (0,"一个月内报名"),
                    (0,"2周内报名"),
                    (0,"已报名报名"),
                    )
    status=models.SmallIntegerField(choices=status_choices)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.content

class Course(models.Model):
    """课程表"""
    name=models.CharField(max_length=64,unique=True,verbose_name="课程名称")
    price=models.SmallIntegerField()
    period=models.PositiveSmallIntegerField(verbose_name="课程周期（月）",default=5)
    outline=models.TextField(verbose_name="大纲")


    def __str__(self):
        return self.name


class ClassList(models.Model):
    """班级表"""
    course = models.ForeignKey("course")
    semester = models.SmallIntegerField(verbose_name="学期")
    teachers = models.ManyToManyField("UserProfile",verbose_name="讲师")
    start_date = models.DateField(verbose_name="开班日期")
    garduate_date = models.DateField(verbose_name="毕业日期",blank=True,null=True)

    def __str__(self):
        return self.course.name+self.semester+"期"

    class Meta:
        unique_together = ("course", "semester")

class CourseRecord(models.Model):
    """上课记录表"""
    class_grade = models.ForeignKey("ClassList", verbose_name="上课班级")
    day_num = models.SmallIntegerField(verbose_name="课程节次")
    teacher = models.ForeignKey("UserProfile")
    title = models.CharField(max_length=64, verbose_name="本节主题")
    content = models.TextField(verbose_name="本节内容")
    has_homework = models.BooleanField(verbose_name="是否有作业", default=True)
    homework = models.TextField(verbose_name="作业内容", blank=True, null=True)
    def __str__(self):
        return "{}第{}节课".format(self.class_grade, self.day_num)


class StudyRecord(models.Model):
    """学习记录表"""
    pass

class Branch(models.Model):
    """校区表"""
    pass