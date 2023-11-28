#!python3

def boxPrint(symbol, width, height):

    #error checks
    if len(symbol) != 1:
        raise Exception('The Symbol can only be one character long.')
    if (width < 2) or (height < 2):
        raise Exception('Width and Height must be greater or equal to 2')

    #actually prints the box
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (int(width) - 2)) + symbol)
    print(symbol * width)



print('Choose a symbol.')
symbol = input()
print('Choose a width.')
width = int(input())
print('Choose a height.')
height =  int(input())

boxPrint(symbol, width, height)
#boxPrint('*',5,5)


