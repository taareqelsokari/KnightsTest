from time import time
import csv

st = time()

move_jumps = []

max_moves = 10
max_vowel_moves = 2
vowels = [(0, 0), (4, 0), (3, -1), (4, -2)]

memo = {}

keyboard = []

key_positions = { (0, 0): "A",
         (1, 0): "B",
         (2, 0): "C",
         (3, 0): "D",
         (4, 0): "E",
         (0, -1): "F",
         (1, -1): "G",
         (2, -1): "H",
         (3, -1): "I",
         (4, -1): "J",
         (0, -2): "K",
         (1, -2): "L",
         (2, -2): "M",
         (3, -2): "N",
         (4, -2): "O",
         (1, -3): "1",
         (2, -3): "2",
         (3, -3): "3"
       }


def build_keyboard():
    keyboard = [(x, y) for x in range(5) for y in range(-3, 1)]
    keyboard.remove((0, -3))
    keyboard.remove((4, -3))

    #print(f"keyboard = {keyboard}")

    return keyboard
    
def is_position_valid(pos):
    if pos == (0, -3) or pos == (4, -3):
        return False

    if (-1 < pos[0] < 5) and (-4 < pos[1] < 1):
        return True
    else:
        return False


def get_valid_moves(keyboard):
    moves = [(1, -2), (1, 2), (2, -1), (2, 1), (-1, -2), (-1, 2), (-2, -1), (-2, 1)]
    key_pos = {}
    
    for key in keyboard:
        for move in moves:
            x = key[0] + move[0]
            y = key[1] + move[1]
            if is_position_valid((x, y)):
                key_pos.setdefault(key, []).append((x, y))
    
    return key_pos


def generate_moves_sequence(key, loc_in_seq, moves, vowel_count, keys):
    if key in vowels:
        vowel_count += 1
        if vowel_count > max_vowel_moves:
            vowel_count -= 1
            return 0

    if loc_in_seq == max_moves:
        moves[(key, loc_in_seq, vowel_count)] = 0
        return 1
    else:
        if (key, loc_in_seq, vowel_count) in moves:
            return moves[(key, loc_in_seq, vowel_count)]
        else:
            moves[(key, loc_in_seq, vowel_count)] = 0
            for e in keys[key]:
                moves[(key, loc_in_seq, vowel_count)] += generate_moves_sequence(e, loc_in_seq + 1, moves, vowel_count, keys)

    return moves[(key, loc_in_seq, vowel_count)]


def count_moves(keys):
    sequence_position = 1
    vowel_count = 0
    #memo = {}

    x = sum(generate_moves_sequence(key, sequence_position, memo, vowel_count, keys)
               for key in keys)

    #print(f"length memo = {len(memo)}")
    #print(f"content memo = {memo}")

    return x

my_keyboard = build_keyboard()
valid_moves = get_valid_moves(my_keyboard)

print(valid_moves)

print(f"total moves = {count_moves(valid_moves)}")

lst_moves = {}

for k, v in valid_moves.items():
    valid_move_for_letter = []
    #print(f"valid_moves = {key_positions[k]}")
    c = key_positions[k]
    #print(c)

    for x in v:
        #c = c + key_positions[x]
        #print(c, v)
        valid_move_for_letter.append(key_positions[x])
        #print(key_positions[x])
    
    lst_moves[key_positions[k]] = valid_move_for_letter

print(f"lst_moves = {lst_moves}")
    
print(f'fn took {(time() - st):.3f} seconds' )