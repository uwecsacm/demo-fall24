import math
from math import isclose

if __name__ == '__main__':

  a = 1.412 
  b = math.sqrt(2)

  print("Pretty close...") if isclose(a, b, abs_tol=0.002) else print("Not even..")
    
  print ("Really Close") if isclose(a, b, abs_tol=0.001) else print("Almost")
