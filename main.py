import csv

def parse_last_element(lst):
    return int(lst[-1])

def get_rows_from_csv(filename):
    with open(filename) as csvfile:
        return list(csv.reader(csvfile))


def get_at_bats_sum(filename):
    list_of_rows = get_rows_from_csv(filename)
    return sum(map(parse_last_element, list_of_rows))

if __name__ == '__main__':
    filename = 'batting.csv'
    summed = get_at_bats_sum(filename)
    print 'Total at bats was: ' + str(summed)
