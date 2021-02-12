#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
    employee_list = []
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    #with open(csv_file_location,"r") as f :
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    for data in employee_file:
        employee_list.append(data)

    return employee_list

# to test the function
employee_list = read_employees('/home/student-04-64d5779d7587/data/employees.csv')

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data


dictionary = process_data(employee_list)

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()

write_report(dictionary, '/home/student-04-64d5779d7587/test_report.txt')