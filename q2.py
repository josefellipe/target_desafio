num = 55

def is_fibo(number):
    result = " não"
    num1 = 0
    num2 = 1
    if number == num1 or number == num2:
        result = " "
    else:
        while num2<number:
            soma = num1 + num2
            num1 = num2
            num2 = soma
            if soma == number:
                result = ""
    return f"O número {number}{result} pertence a sequência de Fibonacci"

print(is_fibo(num))
