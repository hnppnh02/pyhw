import csv
import os
import traceback
import custom_module


def read_employees():
    employees = {}
    rows = []
    try:
        with open("../csv/employees.csv", newline="") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    employees["fields"] = row
                else:
                    rows.append(row)
        employees["rows"] = rows
        return employees
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit(1)

employees = read_employees()
# print(employees)



def column_index(name):
    return employees["fields"].index(name)

employee_id_column = column_index("employee_id")


def first_name(row_number):
    first_name_column = column_index("first_name")
    row = employees["rows"][row_number]
    return row[first_name_column]


def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches


def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]


def employee_dict(row):
    result = {}
    for i, field in enumerate(employees["fields"]):
        if i != employee_id_column:
            result[field] = row[i]
    return result

print(employee_dict(employees["rows"][0]))


def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        result[row[employee_id_column]] = employee_dict(row)
    return result

print(all_employees_dict())


def get_this_value():
    return os.environ.get("THISVALUE")


def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("swordfish")
print(custom_module.secret)


def read_minutes_file(path):
    result = {}
    rows = []
    with open(path, newline="") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                result["fields"] = row
            else:
                rows.append(tuple(row))
    result["rows"] = rows
    return result


def read_minutes():
    minutes1 = read_minutes_file("../csv/minutes1.csv")
    minutes2 = read_minutes_file("../csv/minutes2.csv")
    return minutes1, minutes2


minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)



