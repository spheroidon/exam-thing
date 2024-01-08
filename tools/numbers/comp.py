def sum_digits(num):
    sum = 0
    for digit in str(num):  
      sum += int(digit)       
    return sum

def ispal(num):
    reverse = ''
    for digit in str(num):
        reverse = digit + reverse
    return str(reverse) == str(num)