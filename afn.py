# Gabriel Hoffman Silva - 10783250
# python3 --version
# 3.8.5

from pprint import pprint

def main(input_file):
  quantity_afns = get_quantity_afns(input_file)

  for i in range(quantity_afns):
    afn = get_afn(input_file)
    accepted_states = get_accepted_states(input_file,afn)
    transitions = get_transitions(input_file,afn)
    test_strings = get_test_strings(input_file)

    if (i == 3):
      result = run_test_string(afn['initial_state'], transitions, [1, 1, 1, 1, 2], accepted_states)
      print(result, end =" ")

    # for test_string in test_strings:
    #   result = run_test_string(afn['initial_state'], transitions, test_string, accepted_states)
    #   print(result, end =" ")
    # print()

def run_test_string(current_state, transitions, test_string, accepted_states):
  for i in range(len(transitions)):
    if (
      transitions[i]['current_state'] == current_state 
      and transitions[i]['symbol_read'] == 0
    ):
      if (test_string == [0]):
        new_test_string = test_string.copy()
        new_test_string.pop(0)
      else:
        new_test_string = test_string.copy()
      
      result = run_test_string(transitions[i]['new_state'], transitions, new_test_string, accepted_states)
      if (result == 1):
        return 1

    if (len(test_string) == 0):
      if current_state in accepted_states:
        return 1
      else:
        return 0

    if (
      transitions[i]['current_state'] == current_state 
      and transitions[i]['symbol_read'] == test_string[0]
    ):
      new_test_string = test_string.copy()
      new_test_string.pop(0)

      result = run_test_string(transitions[i]['new_state'], transitions, new_test_string, accepted_states)
      if (result == 1):
        return 1

    if (
      transitions[i]['current_state'] == current_state 
      and transitions[i]['symbol_read'] == 0
    ):
      result = run_test_string(transitions[i]['new_state'], transitions, test_string, accepted_states)
      if (result == 1):
        return 1
  return 0


def read_input_file(input_file):
  quantity_afns = get_quantity_afns(input_file)

  response = {
    'quantity_afns': quantity_afns,
    'afns': []
  }

  for i in range(quantity_afns):
    afn = get_afn(input_file)
    accepted_states = get_accepted_states(input_file, afn)
    transitions = get_transitions(input_file, afn)
    test_strings = get_test_strings(input_file)

    afn_attributes = {}
    afn_attributes = afn
    afn_attributes['accepted_states'] = accepted_states
    afn_attributes['transitions'] = transitions
    afn_attributes['test_strings'] = test_strings

    response['afns'].append(afn_attributes)

  return response

def get_quantity_afns(input_file):
  afns = input_file.readline()
  afns = int(afns)
  return afns

def get_afn(input_file):
  afn = input_file.readline().split(' ')

  for j in range(len(afn)):
    afn[j] = int(afn[j])

  afn = {
    'quantity_states': afn[0],
    'quantity_symbols': afn[1],
    'quantity_transitions': afn[2],
    'initial_state': afn[3],
    'quantity_accepted_states': afn[4]
  }

  return afn

def get_accepted_states(input_file, afn):
  accepted_states = input_file.readline().split()

  map_object = map(int, accepted_states)
  list_of_integers = list(map_object)

  return list_of_integers

def get_transitions(input_file, afn):
  transitions = []

  for i in range(afn['quantity_transitions']):
    transition = input_file.readline().split(' ')
    
    for j in range(len(transition)):
      transition[j] = int(transition[j])
    
    transitions.append({
      'current_state': transition[0],
      'symbol_read': transition[1],
      'new_state': transition[2]
    })

  return transitions

def get_quantity_test_strings(input_file):
  quantity_test_strings = int(input_file.readline())
  return quantity_test_strings

def get_test_strings(input_file):
  test_strings = []

  quantity_test_strings = get_quantity_test_strings(input_file)

  for i in range(quantity_test_strings):
    test_string = input_file.readline().split(' ')

    for j in range(len(test_string)):
      test_string[j] = int(test_string[j])

    test_strings.append(test_string)

  return test_strings

input_file = open('entrada.txt', 'r')
main(input_file)
