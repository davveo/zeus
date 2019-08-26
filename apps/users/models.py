from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from enums.user import BACK_TYPE, USER_STATUS
from rbac.models import Role


class UserProfile(AbstractUser):
    """
    用户: makemigration提示错误：sers.UserProfile.user_permissions: (fields.E304)，
    需要在settings中指定自定义认证模型：AUTH_USER_MODEL = 'users.UserProfile'
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


class Structure(models.Model):
    """
    组织架构
    """
    type_choices = (("firm", "公司"), ("department", "部门"))
    title = models.CharField(max_length=60, verbose_name="名称")
    type = models.CharField(max_length=20, choices=type_choices, default="department", verbose_name="类型")
    parent = models.ForeignKey("self", null=True, blank=True, verbose_name="父类架构")

    class Meta:
        verbose_name = "组织架构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class User(models.Model):
    class Meta:
        pass






    username = models.CharField('用户名', max_length=255, default='')
    recommend_user_phone = models.CharField('推荐人手机号', max_length=255, default='')
    phone = models.CharField("手机号", max_length=255, unique=True)
    status = models.IntegerField('状态', choices=USER_STATUS, default=USER_STATUS.FREEZE)
    login_password = models.CharField('登陆密码', max_length=255)
    safe_password = models.CharField("安全密码", max_length=255)
    static_money = models.FloatField("静态钱包", default=0)
    dynamic_money = models.FloatField("动态钱包", default=0)
    wechat = models.CharField('微信', max_length=255, default='')
    alipay = models.CharField('支付宝', max_length=255, default='')
    register_time = models.DateTimeField("注册时间", auto_now_add=True)
    is_active = models.BooleanField('是否激活', default=False)
    active_code = models.IntegerField('激活码', default=0)
    money_for_arrange = models.IntegerField('排单币', default=0)
    bank_no = models.CharField('银行卡号', max_length=255, default='')
    bank_type = models.CharField('卡号类型', max_length=255, choices=BACK_TYPE, default=BACK_TYPE.GONGSHANG)


