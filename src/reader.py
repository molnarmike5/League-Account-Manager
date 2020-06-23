import riotwatcher as rw, pandas as pd, sys, traceback, os

def __read_key(filename):
    file = open(filename, 'r')
    key = file.readline()
    file.close()
    return key

key = __read_key('../resources/key')

def add_Account(accounts):
    new = pd.DataFrame({'AccountName' : [str(input())]})
    new = new.set_index('AccountName')
    new2 = accounts.append(new)
    return new2



def overview(accounts):
    print(accounts)

def deleteAccount(accounts):
    accounts.drop(index=str(input()), inplace=True)

def main():
    print("Welcome to Account Manager!")
    if os.path.isfile('../resources/Data.csv') == False:
        data = pd.DataFrame({'AccountName' : []})
        data = data.set_index('AccountName')
    else:
        data = pd.read_csv('../resources/Data.csv', index_col=0)
    while(1):
        print("[1] Add Account      [2] Account Overview        [3] Delete Account        [4] Exit ")
        choice = int(input())
        if choice == 1:
            data = add_Account(data)
        elif choice == 2:
            overview(data)
        elif choice == 3:
            deleteAccount(data)
        elif choice == 4:
            data.to_csv('../resources/Data.csv')
            sys.exit(0)



if __name__ == '__main__':
    main()