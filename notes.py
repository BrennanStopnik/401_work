
# Average

list = [8, 5, 3, 2, 1]
def average(list):
  average = sum(list) / len(list)
  return average

print(' **Average** ')
print(average(list))
print('--------------')


# Sort

list.sort()

print(' **Sort** ')
print(list)
print('--------------')


# Median

scores = [91, 88, 83, 84, 92, 95, 88, 91, 88, 86]

def median(scores):
  scores.sort()
  n = len(scores)
  if n % 2 == 0:
    median = (scores[len(scores) // 2 - 1] + scores[len(scores) // 2]) / 2
  else:
    median = scores[len(scores) // 2]
  return median

print(' **Median** ')
print(median(scores))
print('--------------')