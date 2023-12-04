import csv


class ReadCovidRecords:
    
    @staticmethod
    def read_file(covid, file_path, fields):
        covid_records = []

        with open(file_path, "r") as file:
            csv_reader = csv.DictReader(file)
            for line in csv_reader:
                parameters = [line[field] for field in fields]
                covid_records.append(covid(*parameters))        
        
        return covid_records
        
