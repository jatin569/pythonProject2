def get_next_highest_salary_in_same_dept(employee_lst, employee_name, salary, department):
    next_highest_salary = None
    employee_next_highest_salary = ""
    for i in range(len(employee_lst)):
        if employee_lst[i][0] == employee_name:
            pass
        if employee_lst[i][2] == department and employee_lst[i][1] > salary:
            if next_highest_salary == None or employee_lst[i][1] < next_highest_salary:
                next_highest_salary = employee_lst[i][1]
                employee_next_highest_salary = employee_lst[i][0]
    return next_highest_salary, employee_next_highest_salary

employee_lst = [["A", 1000, "IT"], ["C", 3000, "IT"], ["B", 2000, "IT"], ["D", 4000, "HR"], ["E", 2000, "HR"], ["F", 1500, "IT"], ["G", 7000, "HR"]]
for i in range(len(employee_lst)):
    next_highest_salary, employee_next_highest_salary = get_next_highest_salary_in_same_dept(employee_lst, employee_lst[i][0], employee_lst[i][1], employee_lst[i][2])
    print(employee_lst[i][0], employee_lst[i][1], employee_lst[i][2], next_highest_salary, employee_next_highest_salary)