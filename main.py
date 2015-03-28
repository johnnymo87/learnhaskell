import csv

def last_of(lst):
    return int(lst[-1])

def get_at_bat_sum(filename):
    with open(filename) as csvfile:
        list_of_lists = list(csv.reader(csvfile))
    return sum(map(last_of, list_of_lists))

def run(filename):
    summed = get_at_bat_sum(filename)
    print 'Total at bats was: ' + str(summed)

if __name__ == '__main__':
    filename = 'batting.csv'
    run(filename)
