# Given an array arr of strings, complete the function by calculating the total perimeter of all the islands. Each piece of land will be marked with 'X' while the water fields are represented as 'O'. Consider each tile being a perfect 1 x 1 piece of land. Some examples for better visualization:

# ['XOOXO',
#  'XOOXO',
#  'OOOXO',
#  'XXOXO',
#  'OXOOO'] 

def land_perimeter(arr):
    perimeter = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'X':
                perimeter += 4
                if i > 0 and arr[i-1][j] == 'X':
                    perimeter -= 2
                if j > 0 and arr[i][j-1] == 'X':
                    perimeter -= 2
    return f"Total land perimeter: {perimeter}"

print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]))