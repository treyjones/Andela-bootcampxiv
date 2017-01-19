def find_max_min(input_array):
  a = min (input_array)
  b = max (input_array)
  
  if a==b:
    return [len(input_array)]
  return [a,b]
print find_max_min([1,55,2,3])