import statistics

def mean(numbers):
  total = 0
  for number in range(0,len(numbers)):
    total += numbers[number]

  result = total/len(numbers)

  return result
    
def median(numbers):
  result = statistics.median(numbers)

  return result
  print()

  mean(result)

