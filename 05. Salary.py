def zero_salary_message(salary):
    if salary <= 0:
        return "You have lost your salary."
    else:
        return int(salary)


def salary(tabs, salary):
    for _ in range(tabs):
        if salary <= 0:
            return zero_salary_message(salary)

        tab_name = input()

        if tab_name == "Facebook":
            salary -= 150
        elif tab_name == "Instagram":
            salary -= 100
        elif tab_name == "Reddit":
            salary -= 50

    return zero_salary_message(salary)


opened_tabs = int(input())
mount_salary = float(input())
print(salary(opened_tabs, mount_salary))