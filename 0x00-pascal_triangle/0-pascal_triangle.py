#!/usr/bin/python3
"""
This is an ALX of 0-pascal_triangle project
"""


def pascal_triangle(n):
  """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
  triangle = [] 
   
  # Loop through each row 
  for i in range(n): 
    # Create a list to hold the values in the row 
    row = [] 
     
    # Loop through each position in the row 
    for j in range(i + 1): 
      # Calculate the value using the binomial coefficient formula 
      value = int(math.factorial(i) / (math.factorial(j) * math.factorial(i - j))) 
       
      # Append the value to the row 
      row.append(value) 
       
    # Append the row to the triangle 
    triangle.append(row) 
     
  return triangle
