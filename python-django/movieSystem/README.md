# movierecomend

python3+django

## Virtualenv 的安装的使用

```python
pip install virtualenv
virtual django_env
```

```bash
Scripts\activate #激活当前环境
Scripts\deactivate #销毁当前环境
```

## Django 的安装

```python
pip install django
```

## Django 项目的创建

```python
django-admin startproject movierecomend
python manage.py -h #查看manage.py支持的功能
```

1. 修改中文语言和时区 settings.py

    ```python
    LANGUAGE_CODE = 'zh-hans'
    TIME_ZONE = 'Asia/Shanghai'
    ```

2. 设置模板目录 settings.py

    ```python
    'DIRS': [
                os.path.join(BASE_DIR,'templates')
            ],
    ```

3. 设置静态文件

    ```python
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR,'static')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR,'media')
    ```

## 测试运行 Django 项目

```python
python manage.py runserver # http://127.0.0.1:8000/
```

## Django 应用的创建

```python
python manage.py startapp movie #创建app项目
```

1. 添加到应用列表 settings.py  INSTALLED_APPS变量

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'video'
    ]
    ```

2. 数据模型的创建和更改

    ```python
    python manage.py migrate movie #创建数据表
    python manage.py makemigrations #检测项目中数据模型的数据迁移变化
    ```

3. 创建超级用户

    ```python
    python manage.py createsuperuser #Superuser creation skipped due to not running in a TTY. You can run `manage.py createsuperuser` in your project to create one manually.
    ```

## 前台

    http://127.0.0.1:8000/

## 后台

    http://127.0.0.1:8000/admin/

>账号 junhey
密码 jun123456
或
账号 admin
密码 admin123

## 总体功能

    1. 实现电影列表和详情页面
    2. 实现导入movielens数据
    3. 实现电影推荐列表的展示

## 需要完善

    1. 数据库模型
    2. 界面操作
    3. 数据载入

## 数据库

    电影类别

    电影

    评分

    系统参数
