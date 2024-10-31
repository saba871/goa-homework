# თქვენი დავალებაა შექმნათ მარტივი ჩატ-ბოტი, რომელიც კოდის გაშვებისთანავე მიესალმება მომხარებელს და ჰკითხავს "How are your?", თუ მომხარებელი შეიყვანს, "Normal" დაბეჭდეთ "Bot:I hope you will get better", სხვა შემთხვევაში თუ შემოიყვანს "Great", დაუბეჭდეთ "Bot:Good! Have a nice day", ხოლო თუ შემოიყვანა "Sad" ან "Super Sad" დაუბეჭდეთ "Bot:It's sad". საბოლოოდ დაბეჭდეთ "Good bye!" და გათიშეთ while ციკლი. ამისათვის მას გადაეცით სწორი პირობა(მინიშნება: შექმენით ცვლადი რომლის მნიშვნელობა თავიდან იქნება False, while ციკლს პირობად გაუწერეთ ეს ცვლადი, თუ მომხარებელმა სწორი ინფორმაცია შემოიყვანა მისი ნიშვნელობა გახდება True და როცა ყველა პირობა შესრულდება while ციკლი გაითიშება).
# თუ მომხარებელი შემოიყვანს ისეთ ინფორმაციას რაზეც თქვენი ბოტი არ არის დაპროგრამირებული, დაბეჭდეთ "Bot: Sorry, I didn't understand, repeat."(ამ შემთხვევაში while ციკლისთვის შექმნილი ცვლადის მნიშვნელობა არ იცვლება და ციკლი არ წყვეტს მუშაობას)
# დაგჭირდებათ: while loop; input; if/else; and or.
# თქვენი სურვილით დაამატეთ სხვა ფუნქციები და გააუმჯობესეთ ჩატ-ბოტი

print("Bot: Hello! I am steve,your new virtual friend, so tell me how are you fell today? ")

while True:

    user = input("user: ")

    if "i am not good" in user:

        print("bot: Everything will be fine, the main thing is to believe in yourself and not to give up <3")

    elif "i am so good" in user:

        print("bot: Woww I am happy to you,")

    elif "thanks" in user:

        print("bot: Not a problem, have a nice day ")

    elif "I have bad life " in user:

        print("Remember there is no such thing as a bad life, there are bad days, never give up, I believe in you ")

        # break

    else:

        print("bot: sorry, i can't undestand :( ")

        break
