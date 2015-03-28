import csv

def run():
    with open('batting.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print row

if __name__ == '__main__':
    run()
