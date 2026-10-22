scores = []

while True:
    user_input = input("შეიყვანეთ ქულა (ან 'stop'): ")

    # სტოპი თუ შეგვყავს მაშინ გამოდის(ციკლის დასრულება)
    if user_input == "stop":
        break

    
    try:
        number = float(user_input)
    except ValueError:
        print("გთხოვთ შეიყვანოთ სწორი რიცხვი ან 'stop'")
        continue

    # მხოლოდ ციფრები 0-10
    if 0 <= number <= 10:
        scores.append(number)
    else:
        print("ქულა უნდა იყოს 0-დან 10-მდე")

#რეზულტატის ჩვენება აქ:
if scores:
    minimum = min(scores)
    maximum = max(scores)
    average = sum(scores) / len(scores)

    print(f"მინიმალური ქულა: {minimum}")
    print(f"მაქსიმალური ქულა: {maximum}")
    print(f"კლასის საშუალო: {average:.2f}")

    
    sorted_scores = sorted(scores)
    print("ქულები ზრდადობით:", sorted_scores)

    ##ვწერთ რამდენერ განმეორდა 
    print("გამეორებები:")
    for score in sorted(set(scores)):
        print(f"{score} - {scores.count(score)} ჯერ")
else:
    print("ქულები არ შეყვანილა")