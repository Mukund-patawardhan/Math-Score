import pandas as pd
import statistics
import csv

data = pd.read_csv("StudentsPerformance.csv")

mathScore = data["Height(Inches)"].to_list()
mathScore.pop(0)

mean_mathScore = statistics.mean(mathScore)

standardDeviation = statistics.stdev(mathScore)

first_std_deviation_start , first_std_deviation_end = mean_mathScore - (1 * standardDeviation) , mean_mathScore + (1 * standardDeviation)
second_std_deviation_start , second_std_deviation_end = mean_mathScore - (2 * standardDeviation) , mean_mathScore + (2 * standardDeviation)
third_std_deviation_start , third_std_deviation_end = mean_mathScore - (3 * standardDeviation) , mean_mathScore + (3 * standardDeviation)

listOfDataWithinOneStandardDeviation = [result for result in mathScore if result > first_std_deviation_start and result < first_std_deviation_end]
listOfDataWithinTwoStandardDeviation = [result for result in mathScore if result > second_std_deviation_start and result < second_std_deviation_end]
listOfDataWithinThreeStandardDeviation = [result for result in mathScore if result > third_std_deviation_start and result < third_std_deviation_end]

print ('{} % of height lies within one standard deviation'.format(len(listOfDataWithinOneStandardDeviation)*100/len(height)))
print ('{} % of height lies within two standard deviations'.format(len(listOfDataWithinTwoStandardDeviation)*100/len(height)))
print ('{} % of height lies within three standard deviations'.format(len(listOfDataWithinThreeStandardDeviation)*100/len(height)))