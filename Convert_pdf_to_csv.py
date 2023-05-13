import tabula
import pandas as pd
import csv

file = "data.pdf"
pdfData = tabula.read_pdf(file, pages=[2,3]) #Read the pages needs to be checked
# print(pdfData) #Show in console the information

output = tabula.convert_into(file, "data_converted_end.csv", output_format="csv", pages=[2,3]) #Process that convert the pdt into csv
# print(output)

csv_file = "data_converted_end.csv" #File name
output_file = "data_converted_temp.csv"  #Output file name


df = pd.read_csv(csv_file) #Readfile using pandas
df.dropna(how="all", inplace=True) #Delete all empty rows
df.to_csv(output_file, index=False)

headers = ["Nombre Comercio", "Soles", "Dolares"]

with open('data_converted_temp.csv', 'r', newline='') as input_file, open('data_converted_end.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Write the headers to the output file
    writer.writerow(headers)

    # Copy the data from the input file to the output file
    for row in reader:
        writer.writerow(row)


csv_file = "data_converted_end.csv" #File name
output_file = "data_converted_temp.csv"  #Output file name


df = pd.read_csv(csv_file) #Readfile using pandas

# Define the condition for row deletion
condition1 = df["Nombre Comercio"] == ("PAGO TARJ WEB APP")
condition2 = df["Nombre Comercio"] == ("Debías en el estado de cuenta anterior *")
condition3 = df["Nombre Comercio"] == ("BENNY PEREZ")
condition4 = df["Nombre Comercio"] == ("Fecha Comercio")
condition5 = df["Nombre Comercio"] == ("JESSIKA MEDINA")
condition6 = df["Nombre Comercio"] == ("SUBTOTAL --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Drop rows that match the condition
df = df[~(condition1 | condition2 | condition3 | condition4 | condition5 | condition6)]

# Write the cleaned DataFrame to a new CSV file
df.to_csv(output_file, index=False)
#s-------------------------------------------------------------------------------------------------
with open('data_converted_temp.csv', 'r', newline='') as input_file, open('data_converted_end.csv', 'w', newline='') as output_file:
    # Create a CSV reader object
    reader = csv.reader(input_file)

    # Create a CSV writer object
    writer = csv.writer(output_file)

    # Iterate over each row in the CSV file
    for row in reader:
        # Check if the value in the first column is equal num
    
        if row[0][:1].isdigit():

            # Rewrite the value in the second column to 'bar'
            row[0] = row[0][7:]
            # print(row)

        # Write the modified row to the CSV file
        writer.writerow(row)

print("Task Completed")