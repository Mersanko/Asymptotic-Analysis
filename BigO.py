import matplotlib.pyplot as plt
import time
import math

class BigO:
    def __init__(self):
        self.inputs = list()
        self.listinputs = ""
    def logarithmic(self,n):
        return math.log(n)
    def linearithmic(self,n):
        return n*(math.log(n))
    def linear(self,n):
        return n
    def quadratic(self,n):
        return pow(n,2)
    def polynomial(self,n):
        return pow(n,3)
    def exponential(self,n):
        return pow(2,n)
    def execution_time(self):
        execution_time_logarithmic_list= list()
        execution_time_linearithmic_list = list()
        execution_time_linear_list =list()
        execution_time_quadratic_list = list()
        execution_time_polynomial_list = list()
        execution_time_exponential_list = list()

        input1 = str(input("Input integers separated with commas in increasing order:"))
        BigO.listinputs+=input1
        split_inputs = BigO.listinputs.split(",")
        for i in split_inputs:
            BigO.inputs.append(int(i))


        for n in BigO.inputs:
            start_time_logarithmic = time.clock()
            BigO.logarithmic(n)
            end_time_logarithmic = time.clock()
            execution_time_logarithmic = end_time_logarithmic - start_time_logarithmic
            execution_time_logarithmic_list.append(execution_time_logarithmic)

            start_time_linearithmic = time.clock()
            BigO.linearithmic(n)
            end_time_linearithmic = time.clock()
            execution_time_linearithmic = end_time_linearithmic - start_time_linearithmic
            execution_time_linearithmic_list.append(execution_time_linearithmic)

            start_time_linear = time.clock()
            BigO.linear(n)
            end_time_linear = time.clock()
            execution_time_linear = end_time_linear - start_time_linear
            execution_time_linear_list.append(execution_time_linear)

            start_time_quadratic = time.clock()
            BigO.quadratic(n)
            end_time_quadratic = time.clock()
            execution_time_quadratic = end_time_quadratic - start_time_quadratic
            execution_time_quadratic_list.append(execution_time_quadratic)

            start_time_polynomial = time.clock()
            BigO.polynomial(n)
            end_time_polynomial = time.clock()
            execution_time_polynomial = end_time_polynomial - start_time_polynomial
            execution_time_polynomial_list.append(execution_time_polynomial)

            start_time_exponential = time.clock()
            BigO.exponential(n)
            end_time_exponential = time.clock()
            execution_time_exponential = end_time_exponential  - start_time_exponential
            execution_time_exponential_list.append(execution_time_exponential)

        plt.xlabel('Value of n')
        plt.ylabel('Execution Time')

        plt.plot(BigO.inputs,execution_time_logarithmic_list,label = "Logarithmic")
        plt.plot(BigO.inputs,execution_time_linearithmic_list,label = 'Linearithmic')
        plt.plot(BigO.inputs,execution_time_linear_list,label ='Linear')
        plt.plot(BigO.inputs,execution_time_quadratic_list,label = 'Quadratic')
        plt.plot(BigO.inputs,execution_time_polynomial_list,label ='Polynomial')
        plt.plot(BigO.inputs,execution_time_exponential_list,label ='Exponential')

        plt.grid()
        plt.legend()
        plt.show()


BigO = BigO()
BigO.execution_time()
