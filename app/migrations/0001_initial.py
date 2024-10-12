# Generated by Django 5.1.1 on 2024-10-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255, verbose_name='景区名')),
                ('level', models.CharField(default='', max_length=255, verbose_name='等级')),
                ('discount', models.CharField(default='', max_length=255, verbose_name='折扣')),
                ('saleCount', models.CharField(default='', max_length=255, verbose_name='销量')),
                ('province', models.CharField(default='', max_length=255, verbose_name='省份')),
                ('star', models.CharField(default='', max_length=255, verbose_name='热度')),
                ('detailAddress', models.CharField(default='', max_length=255, verbose_name='详情地址')),
                ('shortIntro', models.CharField(default='', max_length=255, verbose_name='短评')),
                ('detailUrl', models.CharField(default='', max_length=255, verbose_name='详细链接')),
                ('score', models.CharField(default='', max_length=255, verbose_name='分数')),
                ('price', models.CharField(default='', max_length=255, verbose_name='价格')),
                ('commentsLen', models.CharField(default='', max_length=255, verbose_name='评论个数')),
                ('detailIntro', models.CharField(default='', max_length=2555, verbose_name='详情介绍')),
                ('img_list', models.CharField(default='', max_length=255, verbose_name='图片列表')),
                ('comments', models.CharField(default='', max_length=255, verbose_name='用户评论')),
                ('cover', models.CharField(default='', max_length=255, verbose_name='封面')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='爬取时间')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=255, verbose_name='用户名')),
                ('password', models.CharField(default='', max_length=255, verbose_name='密码')),
                ('sex', models.CharField(default='', max_length=255, verbose_name='性别')),
                ('address', models.CharField(default='', max_length=255, verbose_name='地址')),
                ('avatar', models.ImageField(default='avatar/default.png', upload_to='avatar', verbose_name='头像')),
                ('textarea', models.CharField(default='这个人很懒，什么也没留下', max_length=255, verbose_name='个人简介')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('score', models.CharField(default='', max_length=255, verbose_name='分数')),
                ('commentsLen', models.CharField(default='', max_length=255, verbose_name='评论个数')),
                ('img_list', models.CharField(default='', max_length=255, verbose_name='图片列表')),
                ('comments', models.CharField(default='', max_length=255, verbose_name='用户评论')),
            ],
        ),
    ]
