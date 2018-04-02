# -*-coding: utf-8 -*-
# Auther： Henry Yuan
import sys
from lib import views
from . import operators

user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}
student_view = views.StudentView()
teacher_view = views.TeacherView()
admin_view = views.AdminView()


def interactive(menu, menu_dict, obj, flag):
    """ 主菜单接口。
        用户首先登录主菜单，选择进入具体的通道。

    :return:
    """
    exit_flag = True
    while exit_flag:
        print(menu)
        cmd = input('>>:').strip()
        if cmd in menu_dict:
            result = eval(menu_dict[cmd])
            # print(result)
            #exit_flag = result
        else:
            print('选项不存在')


def homepage(obj=None):
    while True:
        menu = '''
===============欢迎进入老男孩学校===============
                1. 学生登录通道
                2. 教师登录通道
                3. 管理员登录通道
                4. 退出
================================================
        '''
        menu_dict = {'1': 'student_homepage()',
                     '2': 'teacher_homepage()',
                     '3': 'admin_homepage()',
                     '4': 'exit_system()'}
        interactive(menu, menu_dict, obj, flag=True)


def student_homepage(obj=student_view):

    menu = '''
===============欢迎进入学员视图===============
               1. 注册账号
               2. 填写账户信息
               3. 查看账户信息
               4. 选择课程并付费
               5. 查看学习记录
               6. 修改密码
               7. 注销
==============================================
    '''
    menu_dict = {'1': 'sign_up(obj)',
                 '2': 'set_information(obj)',
                 '3': 'tell_information(obj)',
                 '4': 'choice_course(obj)',
                 '5': 'tell_record(obj)',
                 '6': 'change_password(obj)',
                 '7': 'sign_out(obj)'}
    # menu_dict = {'1': 'operators.sign_up(obj)',
    #              '2': 'operators.set_information(obj)',
    #              '3': 'operators.tell_information(obj)',
    #              '4': 'operators.choice_course(obj)',
    #              '5': 'operators.tell_record(obj)',
    #              '6': 'operators.change_password(obj)',
    #              '7': 'operators.sign_out(obj)'}
    interactive(menu, menu_dict, obj, flag=True)


def teacher_homepage(obj=teacher_view):

    menu = '''
===============欢迎进入学员视图===============
               1. 注册账号
               2. 补充个人信息
               3. 查看账户信息
               4. 选择课程
==============================================
    '''
    menu_dict = {'1': 'register(obj)',
                 '2': 'set(obj)',
                 '3': 'tell(obj)',
                 '4': 'choice_pay(obj)'}
    # menu_dict = {'1': 'operators.register(obj)',
    #              '2':  'operators.set(obj)',
    #              '3': 'operators.tell(obj)',
    #              '4': 'operators.choice_pay(obj)'}
    interactive(menu, menu_dict, obj, flag=True)


def admin_homepage(obj=admin_view):
    menu = '''
===============欢迎进入学员视图===============

               1. 创建学校
               2. 创建课程
               3. 创建班级
               4. 创建讲师
               5. 创建学员
               6. 修改密码
               7. 注销
==============================================
        '''
    # menu_dict = {'1': 'operators.create_school(obj)',
    #              '2': 'operators.create_courses(obj)',
    #              '3': 'operators.create_classes(obj)',
    #              '4': 'operators.create_teachers(obj)',
    #              '5': 'operators.create_students(obj)',
    #              '6': 'operators.change_password(obj)',
    #              '7': 'operators.sign_out(obj)'}
    menu_dict = {'1': 'create_school(obj)',
                 '2': 'create_courses(obj)',
                 '3': 'create_classes(obj)',
                 '4': 'create_teachers(obj)',
                 '5': 'create_students(obj)',
                 '6': 'change_password(obj)',
                 '7': 'sign_out(obj)'}
    interactive(menu, menu_dict, obj, flag=True)


def login(func):
    """ 登录函数

    :param func:
    :return:
    """
    def inner(*args, **kwargs):
        if args[0].login():
            func(*args, **kwargs)
    return inner


def sign_up(obj):
    """ 注册函数

    :param obj: 传入需要的视图对象
    :return:
    """
    obj.register()


@login
def change_password(obj):
    """ 修改账号的密码

    :param obj: 传入需要的视图对象
    :return:
    """
    obj.change_password()


@login
def set_information(obj):
    """ 设置账号信息函数

    :param obj: 传入需要的视图对象
    :return:
    """
    obj.set_info()


@login
def tell_information(obj):
    """ 查看账户信息函数

    :param obj: 传入需要的视图对象
    :return:
    """
    obj.tell_info()


@login
def choice_course(obj):
    """ 选择课程函数

    :param obj: 传入需要的视图对象
    :return:
    """
    obj.choise_courses()


@login
def tell_record(obj):
    """ 查看学习记录函数

    :param obj: 传入需要的视图对象
    :return:
    """
    pass


def sign_out(obj):
    """ 注销函数

    :param obj: 传入需要的视图对象
    :return:
    """
    obj.logout()
    homepage()


def exit_system():
    """ 退出系统函数

    :return:
    """
    print('\033[34;1m欢迎使用本系统，下次再见！\033[0m')
    sys.exit()

@login
def create_school(obj):
    """ 创建学校函数

    :param obj: 传入需要的视图对象
    :return:
    """
    obj.create_school()


@login
def create_courses(obj):
    """ 创建课程函数

    :param obj: 传入需要的视图对象
    :return:
    """
    obj.create_courses()


@login
def create_classes(obj):
    """ 创建班级函数

    :param obj: 传入需要的视图对象
    :return:
    """
    obj.create_school()


@login
def create_teachers(obj):
    pass


@login
def create_students(obj):
    pass


def run():
    homepage()

