scores = []

while True:
    user_input = input("შეიყვანეთ ქულა (ან 'stop'): ")

    if user_input == "stop":
        break

    try:
        number = float(user_input)
    except ValueError:
        print("გთხოვთ შეიყვანოთ სწორი რიცხვი ან 'stop'")
        continue

    if number >= 0 and number <= 10:
        scores.append(number)
    else:
        print("ქულა უნდა იყოს 0-დან 10-მდე")
#ქულები
if len(scores) == 0:
    print("ქულები არ შეყვანილა")
else:
    minimum = min(scores)
    maximum = max(scores)
    average = sum(scores) / len(scores)

    print("მინიმალური ქულა:", minimum)
    print("მაქსიმალური ქულა:", maximum)
    print("კლასის საშუალო:", average)

    scores.sort()
    print("ქულები ზრდადობით:", scores)

    print("გამეორებები:")
    already_counted = []
    for score in scores:
        if score not in already_counted:
            print(score, "-", scores.count(score), "ჯერ")
            already_counted.append(score)
