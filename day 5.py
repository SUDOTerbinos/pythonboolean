number = 15  

is_divisible_by_3 = number % 3 == 0
is_divisible_by_5 = number % 5 == 0

if is_divisible_by_3 and is_divisible_by_5:
    print(f"{number} is divisible by both 3 and 5.")
elif is_divisible_by_3:
    print(f"{number} is divisible by 3.")
elif is_divisible_by_5:
    print(f"{number} is divisible by 5.")
else:
    print(f"{number} is not divisible by 3 or 5.")
