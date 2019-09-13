#!/usr/bin/env python
# !coding=utf-8
import sys

class Simplex_Operation:
    def __init__(self):
        self.long_x = 11
        print"请输入目标函数及其约束条件: "
        function, condition = self.get_function_and_condition()
        maxZ = self.operate_function(function)
        self.operate_condition(condition, maxZ)


    def get_function_and_condition(self):
        function = raw_input()
        condition = []
        for i in range(self.long_x):
            condition.append(raw_input())
            if condition[-1] == '':
                del condition[-1]
                break
        return function, condition

    def operate_function(self, function):
        ###########################################################分析function的求解并化成标准形式
        maxZ = function
        maxZ = maxZ.lower()
        for number in range(self.long_x):
            x = 'x' + str(number)
            if x in maxZ:
                maxZ = maxZ.replace(x, '*x[' + str(number) + ']')
                if ' *x' in maxZ:
                    maxZ = maxZ.replace(' *x', ' 1*x')
        if "min" in maxZ:
            maxZ = maxZ.replace('min', 'max')
            if 'maxz = -' not in maxZ:
                maxZ = maxZ.replace('maxz = ', 'maxz = + ')
            maxZ = maxZ.replace('+', '__waitstr__')
            maxZ = maxZ.replace('-', '+')
            maxZ = maxZ.replace('__waitstr__', '-')
        maxZ = maxZ.replace('maxz =', '')
        return maxZ

    def operate_condition(self, condition, function):
        ############################################################分析conditon并化成标准形式
        max_number = 0
        for i in range(len(condition) - 1):
            for number in range(self.long_x):
                x = 'x' + str(number)
                if x in condition[i]:
                    condition[i] = condition[i].replace(x, '*x[' + str(number) + ']')
                    max_number = number
                    if ' *x' in condition[i]:
                        condition[i] = condition[i].replace(' *x', ' 1*x')
            the_string = condition[i]
            if the_string[0] == '-':
                pass
            else:
                condition[i] = '+ ' + the_string

        for i in range(len(condition) - 1):
            if '>=' in condition[i]:
                condition[i] = condition[i].replace('>=', '=')
                max_number = max_number + 1
                condition[i] = condition[i].replace(' =', ' - 1*x[' + str(max_number) + '] =')
            elif '<=' in condition[i]:
                condition[i] = condition[i].replace('<=', '=')
                max_number = max_number + 1
                condition[i] = condition[i].replace(' =', ' + 1*x[' + str(max_number) + '] =')
            else:
                pass

        for i in range(len(condition) - 1):
            location = condition[i].find('=')
            change = condition[i]

            if change[location + 2] == '-':
                condition[i] = condition[i].replace('+', '__waitstr__')
                condition[i] = condition[i].replace('-', '+')
                condition[i] = condition[i].replace('__waitstr__', '-')

        change1, change2= ['', '']
        last_condition = condition[-1]
        for number in range(self.long_x):
            x = 'x' + str(number)
            if x in last_condition:
                last_condition = last_condition.replace(x, 'x[' + str(number) + ']')
        if '<=' in last_condition:
            location1 = last_condition.find('<')
            change1 = last_condition[location1 - 5: location1 - 1]
        if '取' in last_condition:
            location2 = last_condition.find('取')
            change2 = last_condition[location2 - 5: location2 - 1]

        for i in range(len(condition) - 1):
            condition[i] = condition[i].replace(change1, '(-1)*' + change1)
            condition[i] = condition[i].replace(change2, '(x[{:.0f}] - x[{:.0f}])'.format(max_number + 2, max_number + 1))


        condition[-1] = ''
        for i in range(1, max_number + 3):
            if i != max_number + 2:
                condition[-1] += 'x[{:.0f}], '.format(i)
            else:
                condition[-1] += 'x[{:.0f}] '.format(i)
        condition[-1] += '>= 0'
        function = function.replace(change1, '(-1)*' + change1)
        function = function.replace(change2, '(x[{:.0f}] - x[{:.0f}])'.format(max_number + 2, max_number + 1))
        print '其标准形式为: \n'
        print 'maxZ =' + function
        for i in range(len(condition)):
            if i == 0:
                print 's.t. =  | ' + condition[i]
            else:
                print '\t| ' + condition[i]

class hello_world:
    def __init__(self):
        print'helloworld'


if __name__== "__main__":
    Simplex_Operation()
    hello_world()
