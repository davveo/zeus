from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

from rbac.models import Role


class Order(models.Model):
    """
    订单表
    """
    name = models.CharField(max_length=20, default="", verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生日期")
    gender = models.CharField(max_length=10, choices=(("male", "男"), ("famale", "女")), default="male",
                              verbose_name="性别")
    mobile = models.CharField(max_length=11, default="", verbose_name="电话")
    email = models.EmailField(max_length=100, verbose_name="邮箱")
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.jpg", max_length=100, null=True,
                              blank=True)
    department = models.ForeignKey("Structure", null=True, blank=True, verbose_name="部门")
    post = models.CharField(max_length=50, null=True, blank=True, verbose_name="职位")
    superior = models.ForeignKey("self", null=True, blank=True, verbose_name="上级主管")
    roles = models.ManyToManyField("rbac.Role", verbose_name="角色", blank=True)
    joined_date = models.DateField(null=True, blank=True, verbose_name="入职日期")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name


class Settlement(models.Model):
    class Meta:
        verbose_name = "订单拆分表"
        verbose_name_plural = verbose_name
        ordering = ['id']

    order = models.ForeignKey(Order)
    money = models.IntegerField()
    operate_user = models.CharField()


