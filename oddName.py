def main():
    name = get_name()
    num=int(intput("Enter the skip value"))
    print_name(name,num)

def print_name(name,num):
    print(name(::num)

def get_name():
    name=input("enter name")
    while len(name)<1:
        name = input("Enter looper names>>1 ")
        return name
main()