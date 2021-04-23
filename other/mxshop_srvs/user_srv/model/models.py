from peewee import *
from user_srv.settings import settings


class BaseModel(Model):
    class Meta:
        database = settings.DB


class User(BaseModel):
    #用户模型
    GENDER_CHOICES = (
        ("female", "女"),
        ("male", "男")
    )

    ROLE_CHOICES = (
        (1, "普通用户"),
        (2, "管理员")
    )

    mobile = CharField(max_length=11, index=True, unique=True, verbose_name="手机号码")
    password = CharField(max_length=100, verbose_name="密码") #1. 密文 2. 密文不可反解
    nick_name = CharField(max_length=20, null=True, verbose_name="昵称")
    head_url = CharField(max_length=200, null=True, verbose_name="头像")
    birthday = DateField(null=True, verbose_name="生日")
    address = CharField(max_length=200, null=True, verbose_name="地址")
    desc = TextField(null=True, verbose_name="个人简介")
    # salt = CharField(max_length=200, null=True, verbose_name="地址")
    gender = CharField(max_length=6, choices=GENDER_CHOICES, null=True, verbose_name="性别")
    role = IntegerField(default=1, choices=ROLE_CHOICES, verbose_name="用户角色")


if __name__ == "__main__":
    settings.DB.create_tables([User])
    #1. 对称加密 2. 非对称加密 无法知道原始密码是什么
    from passlib.hash import pbkdf2_sha256
    # for i in range(10):
    #     user = User()
    #     user.nick_name = f"bobby{i}"
    #     user.mobile = f"1878222222{i}"
    #     user.password = pbkdf2_sha256.hash("admin123")
    #     user.save()

    users = User.select()
    users = users.limit(2).offset(2)
    for user in users:
        print(user.mobile)
        # import time
        # from datetime import date
        # if user.birthday:
        #     print(user.birthday)
        #     u_time = int(time.mktime(user.birthday.timetuple()))
        #     print(u_time)
        #     print(date.fromtimestamp(u_time))

        # print(pbkdf2_sha256.verify("admin123", user.password))
