# while

value: int = 8
count: int = 0

while value % 2 == 0:
    print(f"{value} can be divided by 2")
    count += 1
    print(f"Count: {count}")
    value = int(value / 2)

other_counter: int = 8
while other_counter > 0:
    if other_counter % 2 == 0:
        other_counter -= 1
        continue
    else:
        print(other_counter)
        other_counter -= 1
