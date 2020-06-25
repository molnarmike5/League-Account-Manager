import riotwatcher as rw, pandas as pd, sys, traceback, os


def __read_key(filename):
    file = open(filename, 'r')
    key = file.readline()
    file.close()
    return key


key = __read_key('../resources/key')
watcher = rw.LolWatcher(key)


def add_Account(accounts):
    new = pd.DataFrame({'AccountName': [str(input('Please enter the summoner name\n'))]})
    new = new.set_index('AccountName')
    new2 = accounts.append(new)
    return new2


def overview(accounts):
    for i in accounts.index:
        print(i)


def deleteAccount(accounts):
    delete = str(input('Which account do you want to delete?\n'))
    accounts.drop(index=delete, inplace=True)
    if os.path.isfile('../resources/summoners/' + delete + '.csv'):
        os.remove('../resources/summoners/' + delete + '.csv')
    if os.path.isfile('../resources/summoners/' + delete + 'rank.csv'):
        os.remove('../resources/summoners/' + delete + 'rank.csv')


def infos(accounts, region):
    for i in accounts.index:
        if not os.path.isfile('../resources/summoners/' + str(i) + '.csv'):
            data = pd.DataFrame.from_dict(watcher.summoner.by_name(region, i), orient='index')
            data.to_csv('../resources/summoners/' + str(i) + '.csv')
            print(data)
        else:
            print(pd.read_csv('../resources/summoners/' + str(i) + '.csv', index_col=0))


def rankedinfos(accounts, region):
    for i in accounts.index:
        if not os.path.isfile('../resources/summoners/' + str(i) + '.csv'):
            print("This summoner hasn't been added yet!")
        elif not os.path.isfile('../resources/summoners/' + str(i) + 'rank.csv'):
            data = pd.read_csv('../resources/summoners/' + str(i) + '.csv', index_col=0)
            id = str(data.values[0]).lstrip("['")
            id = id.rstrip("']")
            ranked = pd.DataFrame.from_dict(watcher.league.by_summoner(region, id))
            ranked.to_csv('../resources/summoners/' + str(i) + 'rank.csv')
            print(ranked)
        else:
            ranked = pd.read_csv('../resources/summoners/' + str(i) + 'rank.csv',  index_col=0)
            print(ranked)


def main():
    print("Welcome to Account Manager!")
    if not os.path.isfile('../resources/Data.csv'):
        data = pd.DataFrame({'AccountName': []})
        data = data.set_index('AccountName')
    else:
        data = pd.read_csv('../resources/Data.csv', index_col=0)
    region = str(input('Please type your region\n'))
    while (1):
        print("[1] Add Account      [2] Account Overview        [3] Delete Account          [4] Get Account Infos     "
              "    [5] Get Ranked Infos        [6] Exit ")
        choice = int(input())
        if choice == 1:
            data = add_Account(data)
        elif choice == 2:
            overview(data)
        elif choice == 3:
            deleteAccount(data)
        elif choice == 4:
            infos(data, region)
        elif choice == 5:
            rankedinfos(data, region)
        elif choice == 6:
            data.to_csv('../resources/Data.csv')
            sys.exit(0)


if __name__ == '__main__':
    main()
