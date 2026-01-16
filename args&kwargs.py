# args in the form of tuples
#kwargs keyword arguments
def  args_function(*args):
    print(args)
args_function(1,2,3,4,5,6,7,8,90)

#####################################
def kwargs_function(**kwargs):
    print(kwargs)
kwargs_function(name="hrithik",age=20,city="Pune")
