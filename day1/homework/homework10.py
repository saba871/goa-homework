#  მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ, რამდენჯერ შედის შემოტანილი რიცხვი 100-ში. გააკეთეთ ყველაზე მოკლე გზით(ამისათვის გამოიყენეთ გაყოფის სწორი ტიპი)
num = int(input("what's your number? "))
print("This is how many times your number was placed in 100:",100 // num)
# while ციკლის გამოყენებით გამოიტანეთ 1-დან 20-მდე ყველა კენტი რიცხვის ჯამი
sum = 0
number = 0
while number <= 18:
        number = number + 1
        if number % 2 != 0:
                sum = sum + number
                print(number)
print("odd number's sum is: ", sum)
# 4)მომხარებელს შემოატანინეთ ორი რიცხვი და დაბეჭდეთ ის, რომელიც არის მეტი. თუ ორივე რიცხვი ტოლია დაბეჭდეთ "Both numbers are equal"
num1 =int(input("Enter any first number: "))
num2 =int(input("Enter any second number: "))
if num1 > num2:
        print("your first number is higher ")
elif num1 < num2:
        print("your second number is higher ")         
else:
        print("both number are equal")
# მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ შემოტანილი რიცხვის ფაქტორიალი(დასერჩეთ რა არის ფაქტორიალი)
any_number = int(input("enter any number to find your num's factorial: "))
factorial = 0
if any_number < 0:
        print("I can't calculate your num's fsctorial sorry: ")
elif any_number == 0:
        print("0! = 1")
else:
        print()
# მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში. შემდეგ დაბეჭდეთ შემოტანილი რიცხვის ჩათვლით ყველა რიცხვის კვადრატის ჯამი
random_number = int(input("Enter any number : "))
sum_of_squares = sum(i * 2 for i in range(random_number + 1))
print(sum_of_squares)
