'''
Exercise 3
Calculate all of the base statistics for the following different data structure

class_grades = {'Anton': [88, 78,83,85,87],
               'Rebecca': [92,97,95, 92, 88],
               'Franklin': [77, 78, 73,88, 90],
               'Orin': [88,78,98,92,85],
               'Rose': [90,92,94,96,98]}

Calculate each individuals grade statistics and the class statistics
'''

class_grades = {'Anton': [88, 78,83,85,87],
               'Rebecca': [92,97,95, 92, 88],
               'Franklin': [77, 78, 73,88, 90],
               'Orin': [88,78,98,92,85],
               'Rose': [90,92,94,96,98]}

class ClassBaseStatistics:
    def __init__(self, lst):
        self.lst = lst

    def calc_mean(self):
        return (sum(self.lst)/len(self.lst))

    def calc_median(self):
        self.lst.sort()
        if len(self.lst) % 2 == 1:
            index = int(len(self.lst)/2)
            median = self.lst[index]
        else:
            indexLeft = int(len(self.lst)/2) - 1
            indexRight = indexLeft + 1
            median = (self.lst[indexLeft] + self.lst[indexRight]) / 2
        return median
       
    def calc_mode(self):
        grade_counts = {}
        for grade in self.lst:
            if grade in grade_counts:
                grade_counts[grade] += 1
            else:
                grade_counts[grade] = 1
        max_count = max(grade_counts.values())
        mode = [x for x in grade_counts if grade_counts[x] == max_count]
        if len(mode) == 1:
            return mode[0]
        else:
            return min(mode)
    
    def calc_min(self):
        return min(self.lst)
    
    def calc_max(self):
        return max(self.lst)
    
    def calc_range(self):
        return max(self.lst) - min(self.lst)
    
    def calc_weighted_mean(weights, regular_scores, midterm_scores, final_score):
        weighted_scores = regular_scores + midterm_scores + final_score
        weighted_mean = 0
        for i in range(len(weights)):
            weighted_mean += weights[i] * weighted_scores[i]
        return weighted_mean
    

cbsA = ClassBaseStatistics(class_grades['Anton'])
print("Base Statistics for Anton")
print("Mean:") 
print(cbsA.calc_mean())
print("Median: ") 
print(cbsA.calc_median())
print("Mode: ") 
print(cbsA.calc_mode())
print("Mode: ")
print(cbsA.calc_min())
print("Max: ")
print(cbsA.calc_max())
print("Range: ")
print(cbsA.calc_range())
print("**********************")

cbsR = ClassBaseStatistics(class_grades['Rebecca'])
print("Base Statistics for Rebecca")
print("Mean: ")
print(cbsR.calc_mean())
print("Median: ")
print(cbsR.calc_median())
print("Mode: ")
print(cbsR.calc_mode())
print("Mode: ")
print(cbsR.calc_min())
print("Max: ")
print(cbsR.calc_max())
print("Range: ")
print(cbsR.calc_range())
print("**********************")

cbsF = ClassBaseStatistics(class_grades['Franklin'])
print("Base Statistics for Franklin")
print("Mean: ")
print(cbsF.calc_mean())
print("Median: ")
print(cbsF.calc_median())
print("Mode: ")
print(cbsF.calc_mode())
print("Mode: ")
print(cbsF.calc_min())
print("Max: ")
print(cbsF.calc_max())
print("Range: ")
print(cbsF.calc_range())
print("**********************")

cbsO = ClassBaseStatistics(class_grades['Orin'])
print("Base Statistics for Orin")
print("Mean: ")
print(cbsO.calc_mean())
print("Median: ")
print(cbsO.calc_median())
print("Mode: ")
print(cbsO.calc_mode())
print("Mode: ")
print(cbsO.calc_min())
print("Max: ")
print(cbsO.calc_max())
print("Range: ")
print(cbsO.calc_range())
print("**********************")

cbsRo = ClassBaseStatistics(class_grades['Rose'])
print("Base Statistics for Rose")
print("Mean: ")
print(cbsRo.calc_mean())
print("Median: ")
print(cbsRo.calc_median())
print("Mode: ")
print(cbsRo.calc_mode())
print("Min: ")
print(cbsRo.calc_min())
print("Max: ")
print(cbsRo.calc_max())
print("Range: ")
print(cbsRo.calc_range())
print("**********************")


total_class = []
for grades in class_grades.values():
    total_class += grades

cbsClass = ClassBaseStatistics(total_class)
print("Base Statistics for Class")
print("Mean: ")
print(cbsClass.calc_mean())
print("Median: ")
print(cbsClass.calc_median())
print("Mode: ")
print(cbsClass.calc_mode())
print("Min: ")
print(cbsClass.calc_min())
print("Max: ")
print(cbsClass.calc_max())
print("Range: ")
print(cbsClass.calc_range())
print("**********************")