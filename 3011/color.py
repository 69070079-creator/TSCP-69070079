"""color"""
def main():
    """color"""
    color1 = input()
    color2 = input()
    colors = {"Red","Blue","Yellow"}
    if color1 not in colors or color2 not in colors:
        print("Error")
    else:
        mixed = {color1,color2}
        if mixed == {"Red","Yellow"}:
            print("Orange")
        elif mixed == {"Red","Blue"}:
            print("Violet")
        elif mixed == {"Blue","Yellow"}:
            print("Green")
        elif len(mixed) == 1:
            print(color1)

main()
