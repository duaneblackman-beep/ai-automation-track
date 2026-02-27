


#lowest even number in a list

def lowest_even(li):
    evennumbers=[]
    for num in li:
        if num % 2 == 0:
            evennumbers.append(num)
    if len(evennumbers) ==0:
        return None    
    else:
        return min(evennumbers)
print(lowest_even([1,4,6,8,9,23,35,8,4,2,6,8,10]))

#count even numbers in a list

def count_even_numbers(li):
    evennumbers=[]
    for num in li:
        if num % 2 == 0:
            evennumbers.append(num)
    if len(evennumbers) ==0:
        return None    
    else:
        return len(evennumbers)
print(count_even_numbers([1,4,6,8,9,23,35,8,4,2,6,8,10]))

def even_odd_summary(li):
    evennumbers=[]
    oddnumbers=[]
    for num in li:
        if num % 2 == 0:
            evennumbers.append(num)
        else:
            oddnumbers.append(num)
    if len(evennumbers) ==0 and len(oddnumbers) == 0:
        return None    
    else:
        return f"Even numbers: {evennumbers}, Odd numbers: {oddnumbers}"
print(even_odd_summary([1,4,6,8,9,23,35,8,4,2,6,8,10]))
    
