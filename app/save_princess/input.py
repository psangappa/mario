from app.save_princess.save_princess import save_princess

if __name__ == '__main__':
    n = int(input("enter the size of the grid: "))
    grid = input("enter the grid rows and columns, rows separated by commas. For example --m,-x-,-p- : ")
    print(save_princess(n, grid))
