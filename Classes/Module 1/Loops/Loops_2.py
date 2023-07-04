"""
nums = [1,3,5,7,9, 12, 34, 55]
for num in nums:
    if num > 5:
        break
    print(num)


nums = [1,3,5,7,9, 12, 34, 55]
for num in nums:
    if num == 9:
        continue
    print(num)    

"""
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")