import csv

formatted_data = []

csv_files = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']

for csv_file in csv_files:
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['product'] == 'pink morsel':
                if row['quantity'] and row['price']:
                    try:
                        quantity = int(row['quantity'])
                        price = float(row['price'])
                        sales = quantity * price
                        
                        formatted_data.append({
                            'Sales': sales,
                            'Date': row['date'],
                            'Region': row['region']
                        })
                    except ValueError:
                        print(f"Invalid quantity or price in row: {row}")
                else:
                    print(f"Empty quantity or price in row: {row}")

output_file = 'formatted_output.csv'
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['Sales', 'Date', 'Region']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(formatted_data)

print(f"Formatted data is written to {output_file}.")

