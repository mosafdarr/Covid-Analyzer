import matplotlib.pyplot as plt


class GraphReports:
    
    @staticmethod
    def barchart_plot(keys, data):
        plt.figure(figsize=(20,5))
        plt.bar(keys, data, color="red")

        plt.ylabel("Efficeincy")
        plt.xlabel("Safety Measures")
        plt.title("Top Five Saftery Measures")

        plt.tight_layout()
        plt.show()
