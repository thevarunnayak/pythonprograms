string = input()
no_rotation = int(input())
rotation_list = []

for _ in range(no_rotation):
    rotation_list.append(input().split())  # L 3

firstchar_string = ""
for r_type, nor in rotation_list:
    nor = int(nor)
    if r_type == "L":
        firstchar_string += (string[nor:] + string[:nor])[0]
    elif r_type == "R":
        firstchar_string += (string[nor * -1:] + string[:len(string) - nor])[0]

sub_list = []
for index1 in range(1, len(string) + 1):
    for index2 in range(index1, len(string) + 1):
        if len(string[index1 - 1:index2]) == 3:
            sub_list.append(string[index1 - 1:index2])

for substring in sub_list:
    if sorted(firstchar_string) == sorted(substring):
        print("Yes")
        break
    else:
        print("No")
        break
