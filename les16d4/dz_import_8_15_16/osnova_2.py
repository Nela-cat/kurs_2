#1#import printing_functions
#def prints (arr_python):
    #for text in arr_python:
        #print(f'обьект {text} - напечатался')
        
#arr_models = ['rar','pop','tot','new']
#arr_python = []
#printing_functions.print_models(arr_models,arr_python)
#prints(arr_python)
    

#2#from printing_functions import print_models

#def prints (arr_python):
    #for text in arr_python:
        #print(f'обьект {text} - напечатался')
        
#arr_models = ['rar','pop','tot','new']
#arr_python = []
#print_models(arr_models,arr_python)
#prints(arr_python)

    
#3#from printing_functions import print_models as pip

#def prints (arr_python):
    #for text in arr_python:
        #print(f'обьект {text} - напечатался')
        
#arr_models = ['rar','pop','tot','new']
#arr_python = []
#pip(arr_models,arr_python)
#prints(arr_python)


#4#import printing_functions  as pop

#def prints (arr_python):
    #for text in arr_python:
        #print(f'обьект {text} - напечатался')
        
#arr_models = ['rar','pop','tot','new']
#arr_python = []
#pop.print_models(arr_models,arr_python)
#prints(arr_python)


from printing_functions  import *

def prints (arr_python):
    for text in arr_python:
        print(f'обьект {text} - напечатался')
        
arr_models = ['rar','pop','tot','new']
arr_python = []
print_models(arr_models,arr_python)
prints(arr_python)
        
