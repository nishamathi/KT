# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 10:54:15 2021

@author: nisha
"""
my_list = ["A", "B", "C", "D", 1, 2, 3, 4, 5]
my_tuple = ("A", "B", "C", "D", "EF", "GHI", 1.0, 2.35)
my_dict = {"A":"a", "B":"b", "C":"c", "D":"d", "G":"g", "X":"x", "Z":"z"}
my_set = {'A', 'B', 'C', 'D', 'E'}

class myClass:
    a = 10
    def __init__(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = a
 
 
    def add(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state + a
        return self.state
 
 
    def subtract(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state - a
        return self.state
 
 
    def multiply(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state * a
        return self.state
 
 
    def divide(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state / a
        return self.state
        
# Import pandas library
import pandas as pd
  
# Initialize list of lists
my_data = [['Nisha', 50, 10.2, 5], ['Thom', 55, 15.2,5], ['Yogita', 54, 11.2,5]]
my_df=pd.DataFrame(my_data, columns = ['Name', 'Score', 'Age', 'Rating'])

def datatype_check(dat_type):       
       if(type(dat_type)) in (list,set,tuple,dict):
              print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=====~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
              print ("Type of input dataset : ", type(dat_type))
              print("No. of unique elements in my input dataset is ", len(dat_type))
              my_vars = [type(item) for item in dat_type]
              j=1
              for i in my_vars:
                     print("Datatype of item  #%s in my input dataset is:" %j, i)
                     j=j+1
       
       elif(isinstance(dat_type,pd.DataFrame)):
              print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=====~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
              print ("Type of input dataset : ", type(dat_type))
              print("No. of rows : ",dat_type.shape[0])
              print("No. of columns : ",dat_type.shape[1])
              print("Total no. of elements: ", dat_type.size)
              print("Columns in the dataframe are : ", dat_type.columns)
              print("Columns type within a dataframe: ", dat_type.info())
              for dtype in ['float64','uint8','uint16','object', 'float', 'int64']:
                     selected_dtype = dat_type.select_dtypes(include=[dtype])
                     print("Columns with datatype : %s are \n" %dtype , selected_dtype)
                     
       elif(isinstance(dat_type,dat_type.__class__)):
              print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=====~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
              print ("Type of input dataset : ", type(dat_type))
              method_list = [attribute for attribute in dir(dat_type) if callable(getattr(dat_type, attribute)) and attribute.startswith('__') is False]
              print("Callable methods of the class are :", method_list)
             
       else :
              print("Type of input dataset not defined in the function yet :-)")
              
datatype_check(my_list)
datatype_check(my_tuple)
datatype_check(my_dict)
datatype_check(my_set)
datatype_check(my_data)
datatype_check(my_df)
datatype_check(myClass)
# class instantiation
myClassInst=myClass(5.2)
datatype_check(myClassInst)
datatype_check(datatype_check)