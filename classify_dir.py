# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:02:17 2021

@author: NtRdeMtrX
"""
import copy

def classify_dir(object_in:object, select:str ="all"):
    private_dict = {}
    property_dict = {}
    method_dict = {}
    
    for attr in dir(object_in):
        try:
            attr_info = getattr(object_in, attr)
        except AttributeError as e:
            print(f"\t\tAttributeError: {e}")
            continue
        else:
            if attr.startswith('_'):            
                # Ignores anything starting with underscore 
                # (that is, private and protected attributes)
                private_dict[attr] = attr_info
            else:
                # print((attr, attr_info))
                # print(type(attr_info))
                type_name = type(attr_info).__name__
                if type_name in "builtin_function_or_method": # "method" or "function" or "builtin_function_or_method"
                    method_dict[attr] = attr_info
                else:
                    property_dict[attr] = attr_info
    
    if select in "private": 
        return private_dict
    elif select in ["property", "vars", "properties"]:
        return property_dict
    elif select in "methods":
        return method_dict
    elif select in ["all", "dir"]:
        all_dict = copy.deepcopy(private_dict)
        all_dict.update(property_dict)
        all_dict.update(method_dict)
        return all_dict
    else:
        return private_dict, property_dict, method_dict

def get_private(object_in:object):
    return classify_dir(object_in, "private")        

def get_properties(object_in:object):
    return classify_dir(object_in, "properties")

def get_vars(object_in:object):
    return classify_dir(object_in, "properties")

def get_methods(object_in:object):
    return classify_dir(object_in, "methods")
    
            
if __name__ == "__main__":    
    class NewClass(object):
        def __init__(self, number):
            self.multi = int(number) * 2
            self.str = str(number)
    
        def func_1(self):
            pass
        
    a = NewClass(2)
    x = "a"
    
    from pprint import pprint
    
    
    pprint(get_private(a))
    pprint(get_properties(a))
    pprint(get_vars(a))
    pprint(vars(a))
    pprint(get_methods(a))
    pprint(classify_dir(a, "all"))
    pprint(get_vars(x))
    pprint(get_methods(x))
    # print(dir(a))
    # print(dir(x))
    
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0, 9))
    pprint(get_vars(scaler))
    pprint(get_methods(scaler))

    # pprint(__builtins__.__dict__)