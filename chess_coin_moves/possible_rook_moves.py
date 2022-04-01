def rook_possible_moves_func(name):
    global rook_position
    if name.strip().lower() != "queen" and name.strip().lower() == "rook":
        print(f"Finding Possible {name} Moves")
        rook_position = input(f"Enter {name} Position (Eg: a5) : ").strip().lower()
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    possible_move_list = []
    possible_move_list_2 = []
    possible_move_list_3 = []
    possible_move_list_4 = []

    original_alphabet_index = alphabets.index(rook_position[0])
    alphabet_index = original_alphabet_index

    original_number_coordinate = int(rook_position[-1])
    number_coordinate = original_number_coordinate

    while number_coordinate != 8:
        number_coordinate += 1
        possible_move = f"{rook_position[0]}{number_coordinate}"
        possible_move_list.append(possible_move)

    alphabet_index = original_alphabet_index
    number_coordinate = original_number_coordinate

    while number_coordinate != 1:
        number_coordinate -= 1
        possible_move = f"{rook_position[0]}{number_coordinate}"
        possible_move_list_2.append(possible_move)

    alphabet_index = original_alphabet_index
    number_coordinate = original_number_coordinate

    while alphabet_index != 0:
        alphabet_index -= 1
        possible_move = f"{alphabets[alphabet_index]}{number_coordinate}"
        possible_move_list_3.append(possible_move)

    alphabet_index = original_alphabet_index
    number_coordinate = original_number_coordinate

    while alphabet_index != 7:
        alphabet_index += 1
        possible_move = f"{alphabets[alphabet_index]}{number_coordinate}"
        possible_move_list_4.append(possible_move)

    print(f"{name} possible forward moves : ")
    for i in possible_move_list:
        print(i)

    print(f"{name} possible backward moves : ")
    for i in possible_move_list_2:
        print(i)

    print(f"{name} possible left-side moves : ")
    for i in possible_move_list_3:
        print(i)

    print(f"{name} possible right-side moves : ")
    for i in possible_move_list_4:
        print(i)


# rook_possible_moves_func("Rook")