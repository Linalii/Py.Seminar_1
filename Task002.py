x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("Первая четверь")
elif x < 0 and y > 0:
    print("Вторая четверь")
elif x < 0 and y < 0:
    print("Третья четверь")
else:
    print("Четвертая четверь")