COUNTRIES = []


class CovidStats:

    def __init__(self, country, total_cases, new_cases, total_deaths, new_deaths, total_recovered):
        self.country = country
        self.total_cases = self.process_value(total_cases)
        self.new_cases = self.process_value(new_cases)
        self.total_deaths = self.process_value(total_deaths)
        self.new_deaths = self.process_value(new_deaths)
        self.total_recovered = self.process_value(total_recovered)
        COUNTRIES.append(country)

    @staticmethod
    def countries():
        return COUNTRIES
    
    def process_value(self, value):
        return int(value[1:]) if value.startswith("+") else self.convert_to_int(value)
    
    def convert_to_int(self, value):
        return 0 if self.is_empty(value) else int(value)
    
    def is_empty(self, value):
        return value in ["", " "]
    
