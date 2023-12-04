class Calculations:

    @staticmethod
    def calculate_recovery_ratio(covidstats_record, country):    
        for covid in covidstats_record:
            if covid.country == country:
                return round(covid.total_recovered / Calculations.updated_cases(covid), 3) 
    
    @staticmethod
    def calculate_death_avg(covid_stats, covid_measure, measure):
        total_deaths = [Calculations.updated_deaths(covid) for covid in covid_stats \
                        if Calculations.verify_country(covid.country)]
        
        regulated_countries = list(set(covid.country for covid in covid_measure if covid.measure == measure))
        regulated_countries_deaths = [Calculations.updated_deaths(covid) for covid in covid_stats \
                                      if covid.country in regulated_countries]

        return round((sum(regulated_countries_deaths) / sum(total_deaths)) * 100)
    
    @staticmethod
    def calculate_top_measures(covid_stats, covid_measure):
        measures_data = Calculations.measures_data(covid_measure)
        efficiencies = {}

        for measure, countries in measures_data.items():
            efficiencies[measure] = Calculations.calculate_efficiency(covid_stats, countries)

        top_five_keys = sorted(efficiencies, key=efficiencies.get, reverse=True)[:5]
        top_five_measures = [(key, efficiencies[key]) for key in top_five_keys]

        return zip(*top_five_measures)
    
    @staticmethod
    def calculate_efficiency(covid_stats, countries):
        total_cases = [Calculations.updated_cases(covid) for covid in covid_stats \
                       if covid.country in countries]
        total_recovered = [covid.total_recovered for covid in covid_stats if covid.country in countries]

        return sum(total_recovered) if sum(total_cases) == 0 else \
               round((sum(total_recovered) / sum(total_cases)), 3)
    
    @staticmethod
    def measures_data(covid_measures):
        measures = {}

        for covid in covid_measures:
            if covid.measure in measures.keys():
                if covid.country not in measures[covid.measure]:
                     measures[covid.measure].append(covid.country)            
            else:  measures[covid.measure] = [covid.country]  
        
        return measures
    
    @staticmethod
    def updated_cases(covid):
        return covid.total_cases if covid.new_cases in ["", " "] else covid.total_cases + covid.new_cases
    
    @staticmethod
    def updated_deaths(covid):
        return covid.total_deaths if covid.new_deaths in ["", " "] else covid.total_deaths + covid.new_deaths

    @staticmethod
    def verify_country(country):
        return True if country not in ["", " ", "World", "Total:"] else False

