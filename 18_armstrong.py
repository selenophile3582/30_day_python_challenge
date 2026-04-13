"""🔥 Q18 – Check Armstrong Number
Take a number and check whether it is an Armstrong number.
Example: 153 → 1³ + 5³ + 3³ = 153 ✅
💡 Hint: Count digits first, then no_of_digit each digit."""

num_str = (input("Enter a number :"))
no_of_digit = len(num_str)
num = tempt= int(num_str)

if tempt < 0:
    print("Negative numbers cannot be Armstrong .")
else:
    total = 0
    while tempt > 0:
        total += (tempt % 10) ** no_of_digit
        tempt //= 10

    if num == total:
        print("The entered number is Armstrong .")
    else:
        print("The entered number is not an Armstong number .")
