# 1) while ციკლის გამოყენებით დაპრინტეთ 1-დან 50-მდე ყველა 4-ის ჯერადი რიცხვის კუბი 

# შემოგვაქვს ცვლადი
number = 1
# ვაძლევთ მითითებას while loop- ის დახმარებით
while number <= 50:
    # ბოლოს ვაძლევთ ვუბრძანებთ რომ თუ 4 ზე გაყოპისას ნაშთი გვექნება 0 აიყვანოს კუბში და დაპრინტოს number
    if number % 4 == 0:
        cube = number ** 3
        print(cube)
        # ვუმატებთ number - ს 1 - ს 
    number += 1
# 2) შექმენით რიცხვების დიაპაზონი 1-დან 100-მდე, შეამოწმეთ თუ რიცხვი იყოფა 3-ზე დაბეჭდეთ "Fizz" და გვერდზე მიუწერეთ რიცხვი. თუ რიცხვი იყოფა 5-ზე დაბეჭდეთ "Buzz" და გვერდზე მიუწერეთ რიცხვი, ხოლო თუ იყოფა 3-ზეც და 5-ზეც დაბეჭდეთ "FizzBuzz" და გვერდზე მიუწერეთ რიცხვი
num = 1
while num <= 99:
    if num % 3 == 0:
        print("fizz",num)
    elif num % 5 == 0:
        print("buzz", num)
    elif num % 5 and num % 3 == 0:
        print("fuzzbuzz",num)
    num +=1
print(num)
# 3) შექმენით ორი ცვლადი, პირველში შეინახეთ 1-დან 20-ის ჩათვლით ყველა ლუწი რიცხვის ჯამი, მეორეში კი ყველა კენტის. აიყვანეთ ორივე მე-5 ხარისხში და დაპრინტეთ ის, რომელიც არის მეტი

#  შემოგვაქვს ცვლადები even და odd (ლუწი და კენტი)
even =sum(i for i in range(1,21) if i % 2 == 0) 
odd = sum(i for i in range(1,21) if i % 2 != 0)
# აგვყავს ორივე მეხუთე ხარისხში  
even_sum = even ** 5
even_odd = odd ** 5
#  და ვაძლევთ მითითებას ,თუ even_sum არის მეტი  even_odd -ზე დაპრინტოს even_sum
if even_sum > even_odd:
    print(even_sum)
    # ხოლო სხვა შემთხვევაში even_odd
else:
    print(even_odd)
# 4) True or False and 5 > 3 or "name" == "name" and 123 == "123" and 5 >= 5 <--- გაიგეთ რას გამოიტანს ეს კოდი და ახსენით რატომ.
# ის პირობა ტერმინალში გამოიტანს true - ს

# 5) მომხარებელს შემოატანინეთ რიცხვი და გაიგეთ არის თუ არა ის მარტივი, თუ მარტივია დაპრინტეთ "Number is prime", სხვა შემთხვევაში "Number is not prime"(მარტივია რიცხვი, რომელიც იყოფა მარტო თავის თავზე და ერთზე)
num = int(input("Enter any number: "))
if num % 2 == 0 and num % 4 ==0:
    print("number is not prime ")
elif num % num == 0:
    print("number is prime ")
    


