temps = [221, 234, 222, 340, 500, -99]

new_temp = [temp / 10 for temp in temps]

print('#1')
print(new_temp)

print('#2 if')
if_temp = [temp / 10 for temp in temps if temp > 0]
print(if_temp)

print('#3 if else')
if_temp1 = [temp / 10 if temp > 0 else '-' for temp in temps]
print(if_temp1)