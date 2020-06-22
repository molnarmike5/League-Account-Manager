"""TODO: Read account data"""
import riotwatcher as rw, pandas as pd, sys, traceback, os

def __read_key(filename):
    file = open(filename, 'r')
    key = file.readline()
    file.close()
    return key

key = __read_key('../resources/key')

def add_Account(file):
    file.write(input() + "\n")

def overview():
    data = open('../resources/Data', 'r')
    print(data.readlines())

def main():
    print("Welcome to Account Manager!")
    while(1):
        if os.path.isfile('../resources/Data') == False:
            data = open('../resources/Data', 'w+')
        else:
            data = open('../resources/Data', 'a')
        print("[1] Add Account      [2] Account Overview        [3] Exit ")
        choice = int(input())
        if choice == 1:
            add_Account(data)
            data.close()
        elif choice == 2:
            overview()
            data.close()
        elif choice == 3:
            data.close()
            os.remove('../resources/Data')
            sys.exit(0)



if __name__ == '__main__':
    main()