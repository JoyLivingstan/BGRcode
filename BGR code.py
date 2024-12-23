a = ["R", "G", "B", "G", "G", "R", "B", "B", "G"]
result_B = []
result_G = []
result_R = []
for i in a:
    if i == "B":
        result_B.append(i)
    elif i == "G":
        result_G.append(i)
    else:
        result_R.append(i)
print(result_B+result_G+result_R)