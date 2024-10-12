from django.db import models

# Create your models here.
class Travel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('景区名', max_length=255,default='')
    level = models.CharField('等级',max_length=255,default='')
    discount = models.CharField('折扣', max_length=255, default='')
    saleCount=models.CharField('销量',max_length=255,default='')
    province = models.CharField('省份', max_length=255, default='')
    star = models.CharField('热度', max_length=255, default='')
    detailAddress = models.CharField('详情地址', max_length=255, default='')
    shortIntro = models.CharField('短评', max_length=255, default='')
    detailUrl = models.CharField('详细链接', max_length=255, default='')
    score = models.CharField('分数', max_length=255, default='')
    price= models.CharField('价格',max_length=255, default='')
    commentsLen = models.CharField('评论个数', max_length=255, default='')
    detailIntro=models.CharField('详情介绍',max_length=2555, default='')
    img_list = models.CharField('图片列表', max_length=255, default='')
    comments = models.CharField('用户评论', max_length=255, default='')
    cover = models.CharField('封面', max_length=255, default='')
    createTime = models.DateTimeField('爬取时间', auto_now_add=True)

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField('用户名', max_length=255,default='')
    password = models.CharField('密码',max_length=255,default='')
    sex = models.CharField('性别', max_length=255, default='')
    address = models.CharField('地址', max_length=255, default='')
    avatar = models.ImageField('头像', upload_to='avatar', default='avatar/default.png')
    textarea = models.CharField('个人简介', max_length=255, default='这个人很懒，什么也没留下')
    createTime =models.DateTimeField('创建时间',  auto_now_add=True)
    score = models.CharField('分数', max_length=255, default='')
    commentsLen = models.CharField('评论个数', max_length=255, default='')
    img_list = models.CharField('图片列表', max_length=255, default='')
    comments = models.CharField('用户评论', max_length=255, default='')


