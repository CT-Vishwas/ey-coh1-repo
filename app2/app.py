import csv


def main():
    cities = []
    # Read the Data 
    try:
        
        with open('../Data/Retail Analytics Dataset.csv') as fh:
            data = csv.DictReader(fh)
            
            for row in data:
                cities.append(row['City'])
            
            cities = set(cities)

    except FileNotFoundError:
        print("File does not exist")

    print(f"Unique Cities in Dataset are: {cities}")

if __name__ == '__main__':
    main()