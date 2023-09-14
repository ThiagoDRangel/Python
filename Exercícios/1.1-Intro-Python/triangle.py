def triangle(side, base, height):
    if (side + base > height and base + height > side and height + side > base):
        print("Is a triangule")
        if side == base == height:
            return print("Equilateral Triangle")
        if side == base or base == height or height == side:
            return print("Isosceles Triangle")
        if side != base and side != height:
            return print("Scalene Triangle")
    else:
        print("Not a triangule")

triangle(4, 5, 3)