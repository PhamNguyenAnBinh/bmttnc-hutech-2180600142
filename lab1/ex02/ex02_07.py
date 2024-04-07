<<<<<<< HEAD
print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\nCác dòng đã nhập sau khi chuyển thành chữ in hoa: ")
for line in lines:
=======
print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\nCác dòng đã nhập sau khi chuyển thành chữ in hoa: ")
for line in lines:
>>>>>>> 83cfea7421cd9b531629103b160a32341d2d17f3
    print(line.upper())