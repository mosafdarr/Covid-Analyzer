import argparse

from CovidStats import CovidStats
from CovidMeasure import CovidMeasure
from Calculations import Calculations
from ReadCovidRecords import ReadCovidRecords
from GraphReports import GraphReports

COVIDSTATS_PATH = "datasets/covid_cases_stats.csv"
COVIDMEASURE_PATH = "datasets/covid_safety_measures.csv"

COVIDSTATS_FIELDS = ["country", "total_cases", "new_cases",\
                     "total_deaths", "new_deaths", "total_recovered"]
COVIDMEASURE_FIELDS = ["country", "measure"]

MEASURES = CovidMeasure.measures()
COUNTRIES = CovidStats.countries()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", required=False, help="Country Name for recovered ratio")
    parser.add_argument("-b", required=False, help="Measure to find avg death ratio")
    parser.add_argument("-c", nargs='?', const=" ", required=False, help="Need no argument")

    args = parser.parse_args()

    covid_stats = ReadCovidRecords.read_file(CovidStats, COVIDSTATS_PATH, COVIDSTATS_FIELDS)
    covid_measure = ReadCovidRecords.read_file(CovidMeasure, COVIDMEASURE_PATH, COVIDMEASURE_FIELDS)

    if args.a in COUNTRIES:
        recovered_ratio = Calculations.calculate_recovery_ratio(covid_stats, args.a)
        print(f"Reovered Ratio: {recovered_ratio}")

    if args.b in MEASURES:
        death_avg = Calculations.calculate_death_avg(covid_stats, covid_measure, args.b)
        print(f"{death_avg}% death average found in 89 countries.")

    if args.c:
        measures, efficencies = Calculations.calculate_top_measures(covid_stats, covid_measure)
        GraphReports.barchart_plot(measures, efficencies)

    if not any ([args.a in COUNTRIES, args.b in MEASURES, args.c]):
        print("Key Not Found!")


if __name__ == "__main__":
    main()
