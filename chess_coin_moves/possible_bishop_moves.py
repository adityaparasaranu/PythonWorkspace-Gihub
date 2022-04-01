def bishop_possible_move_func(name):
    print(f"Finding Possible {name} Moves")
    bishop_position = input(f"Enter {name} Position (Eg: a5) : ").strip().lower()
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    possible_move_list = []
    possible_move_list_2 = []
    possible_move_list_3 = []
    possible_move_list_4 = []

    alphabet_coordinate = bishop_position[0]

    original_alphabet_index = alphabets.index(alphabet_coordinate)
    alphabet_index = original_alphabet_index

    original_number_coordinate = int(bishop_position[-1])
    number_coordinate = original_number_coordinate

    while number_coordinate != 8 and alphabet_index != 7:
        possible_move = f"{alphabets[alphabet_index + 1]}{number_coordinate + 1}"
        possible_move_list.append(possible_move)
        alphabet_index += 1
        number_coordinate += 1

    alphabet_index = original_alphabet_index
    number_coordinate = original_number_coordinate

    while alphabet_index != 0 and number_coordinate != 1:
        possible_move = f"{alphabets[alphabet_index - 1]}{number_coordinate - 1}"
        alphabet_index -= 1
        possible_move_list_2.append(possible_move)
        number_coordinate -= 1

    alphabet_index = original_alphabet_index
    number_coordinate = original_number_coordinate

    while alphabet_index != 0 and number_coordinate != 8 :
        possible_move = f"{alphabets[alphabet_index - 1]}{number_coordinate + 1}"
        alphabet_index -= 1
        possible_move_list_3.append(possible_move)
        number_coordinate += 1

    alphabet_index = original_alphabet_index
    number_coordinate = original_number_coordinate

    while number_coordinate != 1 and alphabet_index != 7:
        possible_move = f"{alphabets[alphabet_index + 1]}{number_coordinate - 1}"
        alphabet_index += 1
        possible_move_list_4.append(possible_move)
        number_coordinate -= 1

    print(f"{name} possible forward moves : ")
    for i in possible_move_list:
        print(i)

    print(f"{name} possible backward moves : ")
    for i in possible_move_list_2:
        print(i)

    print(f"{name} possible left-side diagonal moves : ")
    for i in possible_move_list_3:
        print(i)

    print(f"{name} possible right-side diagonal moves : ")
    for i in possible_move_list_4:
        print(i)


# bishop_possible_move_func("Bishop")
