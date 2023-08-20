# def reverse(number):
#     # reversenumber = ''
#     # while number != 0:
#     #     n = number % 10


def reverse(number):
    number = list(number)
    number = number[::-1]
    for i in number:
        print(str(i), end= '')
    return
number = input('Enter a number: ')
reverse(number)
