tup_1=('Saini','Thapa','Magar','Magar')
print(tup_1)
print(type(tup_1))
# tup_1[1]="Tarami"  // It is immutable hence data cannot be modified
# print(tup_1)
print(tup_1[1:]) # Tuple Slicing
print(tup_1.count("Magar"))

print(tup_1.index("Saini"))

tup_2=("Saini","Thapa")
print(tup_2 is tup_1)

# FUNCTION IN PYTHON

def basic_function(name,age):
    print(f"This is the new function Mr. {name} ({age} years old)")
    return True
    
def tuplename(names):
    for name in names:
        print(f"Hello {name}")


def namefind(names):
    name=input("Enter your name: ")
    if name in names:
        print("Name already used")
    else:
        names.append(name)
        return names
def main():
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    
    if basic_function(name,age):
        print("RAN SUCCESSFULLY")

    names=('Sushil','Nishant',"Suraj",'Gundey')
    tuplename(names)
    Firstnames=['Sushil','Nishant',"Suraj",'Gundey']
    if(namefind(Firstnames)):
        print(Firstnames)
    else:
        print("TRY AGAIn")

if __name__=="__main__":
    main()