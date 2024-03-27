def sum(n):
    sum_divisors = 1  
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors

def Number(x, y):
    for num in range(x, y + 1):
        divisor_sum = sum(num)
        if divisor_sum < num:
            print(f"{num} là deficient.")
        elif divisor_sum == num:
            print(f"{num} là perfect.")
        else:
            print(f"{num} là abundant.")
# Nhập hai số nguyên dương x và y
x = int(input("Nhập số nguyên dương x: "))
y = int(input("Nhập số nguyên dương y (y >= x): "))
while y < x:
    print("Vui lòng nhập y lớn hơn hoặc bằng x!")
    y = int(input("Nhập lại số nguyên dương y: "))
print(f"Các số từ {x} đến {y} được phân loại là:")
Number(x, y)