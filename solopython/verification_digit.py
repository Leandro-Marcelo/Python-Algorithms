""" algoritmo para obtener el dígito verificador """

def descomposeNumber(num):
    num_str = str(num)
    result = []
    for i in range(len(num_str)):
        push_num = num % 10
        result.append(push_num)
        num = num // 10
    return result

def getVerificationDigit(num):
    numerical_series = [2, 3, 4, 5, 6, 7]
    rut_arr = descomposeNumber(num)
    total = 0
    j = 0
    for i in range(len(rut_arr)):
        if j > 5:
            j = 0
        sum1 = rut_arr[i] * numerical_series[j]
        total += sum1
        j += 1
    rest = total % 11
    result = 11 - rest
    if result == 11:
        result = 0
    if result == 10:
        result = "k"
    return result
    
print(getVerificationDigit(21064139))