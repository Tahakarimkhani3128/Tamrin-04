import random

# تابع جمع دو ماتریس
def matrix_sum(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "خطا: ابعاد ماتریس‌ها باید یکسان باشد!"
    
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix1[i][j] + matrix2[i][j])
        result.append(new_row)
    
    return result

# تابع ضرب دو ماتریس
def matrix_multiply(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    if cols1 != rows2:
        return "خطا: تعداد ستون‌های ماتریس اول باید برابر با تعداد سطرهای ماتریس دوم باشد!"
    
    result = []
    for i in range(rows1):
        new_row = []
        for j in range(cols2):
            sum = 0
            for k in range(cols1):
                sum += matrix1[i][k] * matrix2[k][j]
            new_row.append(sum)
        result.append(new_row)
    
    return result

# دریافت کد ملی و ساخت ماتریس اول (10×10)
national_code = input("لطفاً کد ملی خود را وارد کنید (10 رقم): ")
while len(national_code) != 10 or not national_code.isdigit():
    print("کد ملی باید 10 رقم باشد و فقط شامل اعداد باشد!")
    national_code = input("لطفاً کد ملی خود را دوباره وارد کنید: ")

vector_national = [int(digit) for digit in national_code]
matrix1 = []
matrix1.append(vector_national.copy())

# ساخت 9 سطر دیگه برای ماتریس اول (جمعاً 10 سطر)
for _ in range(9):  # 9 سطر دیگه، چون سطر اول رو اضافه کردیم
    random_vector = vector_national.copy()
    for i in range(len(random_vector)):
        j = random.randrange(len(random_vector))
        random_vector[i], random_vector[j] = random_vector[j], random_vector[i]
    matrix1.append(random_vector)

# ساخت ماتریس دوم (10×10)
matrix2 = []
for _ in range(10):
    row = [random.randint(0, 9) for _ in range(10)]
    matrix2.append(row)

# جمع دو ماتریس
sum_result = matrix_sum(matrix1, matrix2)

# ضرب دو ماتریس
multiply_result = matrix_multiply(matrix1, matrix2)

# نمایش نتایج
print("\nماتریس اول (10×10):")
for row in matrix1:
    print(row)

print("\nماتریس دوم (10×10):")
for row in matrix2:
    print(row)

print("\nنتیجه جمع ماتریس‌ها (10×10):")
for row in sum_result:
    print(row)

print("\nنتیجه ضرب ماتریس‌ها (10×10):")
for row in multiply_result:
    print(row)