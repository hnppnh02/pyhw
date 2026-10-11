import csv
import traceback


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



