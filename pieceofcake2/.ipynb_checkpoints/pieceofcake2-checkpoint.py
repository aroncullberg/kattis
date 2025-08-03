cake_side, cut_horizontal, cut_vertical = map(int, input().split())

cake_height = 4

pieces = [
    (cut_horizontal, cut_vertical),
    (cut_horizontal, cake_side - cut_vertical),
    (cake_side - cut_horizontal, cut_vertical),
    (cake_side - cut_horizontal, cake_side - cut_vertical)
]
#print(pieces)

max_square_side = max(w * h for w, h in pieces)
print(max_square_side * cake_height)