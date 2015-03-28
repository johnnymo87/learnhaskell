import csv

def get_at_bat_sum(filename):
    sum = 0
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            sum += int(row[3])
    return sum

def run(filename):
    summed = get_at_bat_sum(filename)
    print 'Total at bats was: ' + str(summed)

if __name__ == '__main__':
    filename = 'batting.csv'
    run(filename)
