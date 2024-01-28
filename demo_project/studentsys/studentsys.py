import os


filename = "tmp_polyline_data/studentsys/data.txt"

def menu():
    print('\n')
    print("========== 学生管理系统 ==========")
    print("------------ 功能菜单 ------------")
    print('\n')
    print('\t 1. 录入学生信息')
    print('\t 2. 查找学习信息')
    print('\t 3. 删除学生信息')
    print('\t 4. 修改学生信息')
    print('\t 5. 排序')
    print('\t 6. 统计学生总人数')
    print('\t 7. 显示所有学生信息')
    print('\t 0. 退出')
    print('\n')


def getStudentList():
    student_list = []
    if (os.path.exists(filename)):
        with open(filename, 'r') as f:
            for item in f.readlines():
                if len(item) > 0:
                    student_list.append(dict(eval(item)))
    return student_list

def insert():
    while True:
        id = input('请输入ID (如1001): ')
        name = input('请输入姓名：')
        score = int(input('请输入分数：'))
        student_item = {'id': id, 'name': name, 'score': score}
        save(student_item)
        if input('录入成功, 是否继续录入？(y/n): ') == 'y':
            continue
        else:
            break

def save(student_item):
    with open(filename, 'a') as f:
        f.write(str(student_item) + "\n")


def delete():
    id = input('请输入要删除的学生ID: ')
    isStudentExist = False
    student_list = getStudentList()
    for student in student_list:
        if student['id'] == id:
            isStudentExist = True
            break
    if not isStudentExist:
        print(f'没有找到 id 为 {id} 的学生')
        input('按任意键返回主菜单：')
    else:
        with open(filename, 'w') as f:
            f.write('')
        with open(filename, 'a') as f:
            for item in student_list:
                if item['id'] != id:
                    f.write(str(item) + "\n")
        print(f'id 为 {id} 的学生信息已被删除')
        if (input("是否继续删除？ (y/n): ") == 'y'):
            delete()

def showStudentTotal():
    print("学生总人数为: %d" % len(getStudentList()))
    input('按任意键返回主菜单：')

def list():
    for item in getStudentList():
        print(item)
    input('按任意键返回主菜单：')


def notSupport():
    input('暂不支持。按任意键返回主菜单：')

if __name__ == '__main__':
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))

    while True:
        menu()
        index = int(input('请选择：'))
        if index in range(0, 8):
            if index == 0:
                if (input('您确定要退出系统吗? (y/n): ') == 'y'):
                    print('感谢您的使用，再见！')
                    break
            elif index == 1:
                insert()
            elif index == 2:
                notSupport()
            elif index == 3:
                delete()
            elif index == 4:
                notSupport()
            elif index == 5:
                notSupport()
            elif index == 6:
                showStudentTotal()
            elif index == 7:
                list()
        else:
            print('输入错误，程序退出！')
            break