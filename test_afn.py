import afn

input_file_data = {
        'afns': [
            {
                'accepted_states': [0],
                'initial_state': 0,
                'quantity_accepted_states': 1,
                'quantity_states': 2,
                'quantity_symbols': 3,
                'quantity_transitions': 4,
                'test_strings': [
                    [1],
                    [1, 1],
                    [1, 1, 1],
                    [1, 2, 2, 1, 1, 1, 2, 2, 1],        
                    [2, 2, 2, 1],
                    [2, 1, 2, 2]
                ],
                'transitions': [
                    {'current_state': 0,
                    'new_state': 0,
                    'symbol_read': 1},
                    {'current_state': 0,
                    'new_state': 1,
                    'symbol_read': 1},
                    {'current_state': 0,
                    'new_state': 1,
                    'symbol_read': 2},
                    {'current_state': 1,
                    'new_state': 0,
                    'symbol_read': 2}
                ]
            }
        ],
        'quantity_afns': 1
    }

def test_read_input_file():
    input_file = open('t1.txt', 'r')

    received = afn.read_input_file(input_file)

    to_be = input_file_data

    assert received == to_be

def test_get_quantity_afns():
    input_file = open('t1.txt', 'r')
    assert afn.get_quantity_afns(input_file) == 1

def test_get_afn():
    input_file = open('t1.txt', 'r')
    input_file.readline()

    afn_dictionary = {
        'initial_state': 0, 
        'quantity_accepted_states': 1,
        'quantity_states': 2, 
        'quantity_symbols': 3,
        'quantity_transitions': 4,
    }

    assert afn.get_afn(input_file) == afn_dictionary

def test_get_accepted_states():
    input_file = open('t1.txt', 'r')
    input_file.readline()
    input_file.readline()
    afn_dictionary = {
        'initial_state': 0, 
        'quantity_accepted_states': 1,
        'quantity_states': 2, 
        'quantity_symbols': 3,
        'quantity_transitions': 4,
    }


    assert afn.get_accepted_states(input_file, afn_dictionary) == [0]

def test_get_transitions():
    input_file = open('t1.txt', 'r')
    input_file.readline()
    input_file.readline()
    input_file.readline()
    afn_dictionary = {
        'initial_state': 0, 
        'quantity_accepted_states': 1,
        'quantity_states': 2, 
        'quantity_symbols': 3,
        'quantity_transitions': 4,
    }
    transitions = [
        {'current_state': 0,
        'new_state': 0,
        'symbol_read': 1},
        {'current_state': 0,
        'new_state': 1,
        'symbol_read': 1},
        {'current_state': 0,
        'new_state': 1,
        'symbol_read': 2},
        {'current_state': 1,
        'new_state': 0,
        'symbol_read': 2}
    ]


    assert afn.get_transitions(input_file, afn_dictionary) == transitions

def test_get_test_strings():
    input_file = open('t1.txt', 'r')
    input_file.readline()
    input_file.readline()
    input_file.readline()
    input_file.readline()
    input_file.readline()
    input_file.readline()
    input_file.readline()

    afn_dictionary = {
        'initial_state': 0, 
        'quantity_accepted_states': 1,
        'quantity_states': 2, 
        'quantity_symbols': 3,
        'quantity_transitions': 4,
    }
    test_strings = [
        [1],
        [1, 1],
        [1, 1, 1],
        [1, 2, 2, 1, 1, 1, 2, 2, 1],        
        [2, 2, 2, 1],
        [2, 1, 2, 2]
    ]

    assert afn.get_test_strings(input_file) == test_strings

# def test_test_afns():
#     response = afn.test_afns(input_file_data)

#     to_be = '1 1 1 1 0 0'

#     assert response == to_be

# def test_run_test_strings():
#     first_afn = input_file_data['afns'][0]
#     response = afn.run_test_strings(first_afn)
#     to_be = [1, 1, 1, 1, 0, 0]
#     assert response == to_be

def test_run_test_string_1():
    first_afn = input_file_data['afns'][0]
    response = afn.run_test_string(first_afn, [1], first_afn['initial_state'])
    to_be = 1
    assert response == to_be

def test_run_test_string_2():
    first_afn = input_file_data['afns'][0]
    response = afn.run_test_string(first_afn, [1, 1], first_afn['initial_state'])
    to_be = 1
    assert response == to_be


def test_run_test_string_3():
    first_afn = input_file_data['afns'][0]
    response = afn.run_test_string(first_afn, [1, 2, 2, 1, 1, 1, 2, 2, 1], first_afn['initial_state'])
    to_be = 1
    assert response == to_be

def test_run_test_string_4():
    first_afn = input_file_data['afns'][0]
    response = afn.run_test_string(first_afn, [2, 2, 2, 1], first_afn['initial_state'])
    to_be = 0
    assert response == to_be


