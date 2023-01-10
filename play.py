def draw_cube(size):
    def space_filler(num):
        return " " * num

    def letter_filler(l, num):
        return l * num

    cube = []
    
    i = 1
    while i <= size:
        cube.append(
            space_filler(size - i)
            + letter_filler("/\\", i)
            + letter_filler("_\\", size)
        )
        i += 1
    
    b = size
    while b > 0:
        cube.append(
            space_filler(size - b) + letter_filler("\\/", b) + letter_filler("_/", size)
        )
        b -= 1

    return "\n".join(cube)


print(draw_cube(10))
