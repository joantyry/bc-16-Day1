def fizz_buzz(n):
  '''
  This function returns 'Fizz' if a number is divisible by 3,"Buzz" by 5 and 'FizzBuzz' by both.
  '''
  if n % 15 == 0: # 15 is the LCM of 3 and 5
    return "FizzBuzz"
  elif n % 5 == 0:
    return "Buzz"
  elif n % 3 == 0:
    return "Fizz"
  else:
    return n