
print('_'*30,'Welcome to employee management system','_'*30,)

emps = ['David1\t18\tMale\tUK','David2\t28\tMale\tChina']

def choose1(emps):
    print('\t\tName\tAge\tGender\tAddress')
    n = 1
    for emp in emps:
        print(f'\t{n}\t{emp}')
        n += 1

#choose1(emps)

def choose2(emps):
    emp_name = input('Input Name: ')
    emp_age = input('Input Age: ')
    emp_gender = input('Input Gender: ')
    emp_address = input('Input Address: ')
    emp = f'{emp_name}\t\t{emp_age}\t{emp_gender}\t{emp_address}'
    print('_' * 78)
    print('Following employee information will be added to system')
    print('Name\tAge\tGender\tAddress')
    print(emp)
    print('_' * 78)
    user_confirm = input('Confirm? [Y/N]: ')
    if user_confirm == 'y':
        emps.append(emp)
        print('Have added Information')
    else:
        print('Fail to add')

#choose2(emps)

def choose3(a):
    del_num = int(input('Input who you want to delete: '))
    if 0 < del_num <= len(a):
        del_i = del_num - 1
        print('_' * 78)
        print('Following will be deleted')
        print('\tList\tName\tAge\tMale\tAddress')
        print(f'\t{del_num}\t{a[del_i]}')
        user_confirm = input('Confirm? [Y/N]: ')
        if user_confirm == 'y':
            a.pop(del_i)
            print('Deleted')
        else:
            print('Cancel')
        print('_' * 78)

#choose3(emps)

def start():
    print('_' * 78)
    print('Choose what you want to do： ')
    print('\t1. Check Employee information ')
    print('\t2. Add Employee Information')
    print('\t3. Delete Employee')
    print('\t4. Exit System')
    user_choose = input('Please select [1-4]: ')
    print('_' * 78)
    return user_choose

#start()

while True:
    user_choose = start()

    if user_choose == '1':
        choose1(emps)

    elif user_choose == '2':
        choose2(emps)

    elif user_choose == '3':
        choose3(emps)

    elif user_choose == '4':
        input('Welcome Back at any Time!')
        break
    else:
        print('Error, Restart Please!')
print('_'*78)
