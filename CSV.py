import csv


#with open('DemoCSV.csv','r') as csvfile:
#    csvReader=csv.reader(csvfile)
#    #next(csvReader)
#    with open('DemoCSV_Copy.csv','w') as csvcopyfile:
#        csv_writer=csv.writer(csvcopyfile)
#        for line in csvReader:
#            csv_writer.writerow(line) 


#with open('DemoCSV.csv','r') as file:
#    csvFileReader=csv.DictReader(file)
#    for line in csvFileReader:
#        print(line["Code"])

try:
    with open('DemoCSV.csv','r') as file:
        csvFileReader=csv.DictReader(file)
        with open('DemoCSVDict_Copy.csv','w') as file1:
            fieldsName=['Birthplace','Code','Census_night_population_count','Census_usually_resident_population_count']
            csvwriter=csv.DictWriter(file1,fieldnames=fieldsName,delimiter="\t")
            csvwriter.writeheader()
            for line in csvFileReader:
                csvwriter.writerow(line)
except FileNotFound as e:
    print(e)
    print("File Not Found")



