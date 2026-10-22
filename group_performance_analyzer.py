scores = []

while True:
    user_input = input("Enter score or <stop>: ")

    if user_input == "stop":
        break

    try:
        number = float(user_input)
    except ValueError:
        print("Enter the number or <stop>")
        continue

    if number >= 0 and number <= 10:
        scores.append(number)
    else:
        print("Please write number from 0 to 10")

if len(scores) == 0:
    print("There is no scores")
else:
    minimum = min(scores)
    maximum = max(scores)
    average = sum(scores) / len(scores)

    print("Min. points:", minimum)
    print("Max. points:", maximum)
    print("Average:", average)

    scores.sort()
    print("points by growing:", scores)

    print("Repeats:")
    already_counted = []
    for score in scores:
        if score not in already_counted:
            print(score, "-", scores.count(score), "time(s)")
            already_counted.append(score)
