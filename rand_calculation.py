import random

def generate_triangle():
    triangle = []
    for row in range(76, -1, -1):  # From 76 down to 0
        # Create row with (row+1) numbers, all equal to row
        row_numbers = [row] * (row + 1)
        triangle.append(row_numbers)
    return triangle

def find_valid_sequences(triangle):
    valid_lengths = [3, 7, 11, 13]
    unique_sequences = set()
    
    # For each row
    for row_idx, row in enumerate(triangle):
        # For each position in row
        for col_idx in range(len(row)):
            # For each valid sequence length
            for length in valid_lengths:
                # Try to build sequences starting from this position
                current_row = 76 - row_idx  # Convert triangle index to actual row number
                sequences = build_sequences(current_row, length, set())
                for seq in sequences:
                    # Convert sequence to string for uniqueness check
                    seq_str = ''.join(map(str, sorted(seq)))
                    unique_sequences.add(seq_str)
    
    return unique_sequences

def build_sequences(start_row, length, used):
    if length == 1:
        return [[start_row]]
    
    sequences = []
    # Try both up and down
    for next_row in [start_row + 1, start_row - 1]:
        if 0 <= next_row <= 76 and next_row not in used:
            new_used = used | {start_row}
            sub_sequences = build_sequences(next_row, length - 1, new_used)
            for sub_seq in sub_sequences:
                sequences.append([start_row] + sub_seq)
    
    return sequences

def generate_position_aware_sequence(sequence):
    """Generate a position-aware sequence number from a base sequence"""
    import random
    
    # Convert string sequence back to numbers if needed
    if isinstance(sequence, str):
        sequence = [int(sequence[i:i+2]) for i in range(0, len(sequence), 2)]
    
    # Sort sequence to get lowest and highest row numbers
    sorted_seq = sorted(sequence)
    lowest_row = sorted_seq[0]
    highest_row = sorted_seq[-1]
    
    # Generate random valid positions for these rows
    lowest_pos = random.randint(0, lowest_row)  # Position must be within row length
    highest_pos = random.randint(0, highest_row)  # Position must be within row length
    
    # Format the sequence number
    sequence_number = f"{lowest_row:02d}{lowest_pos:02d}{highest_row:02d}{highest_pos:02d}{len(sequence):02d}"
    
    return sequence_number

def calculate_possible_sequences():
    """Calculate total possible sequences without generating them"""
    total = 0
    base_sequences_by_factor = {}
    
    print(f"\nCreate sequences [Blocks] of length 3, 7, 11 or 13 - prime factors of 3003."
          "\nBlocks are made tapping next row up or down."
          "\nSame base sequence Block can not be made twice."
          "\nOnly 278 Blocks can be validated out of 531,017 possible."
          "\nBe the first to validate a Block, win rewards!")

    # For each valid sequence length
    for length in [3, 7, 11, 13]:
        length_total = 0
        base_total = 0
        for start_row in range(77):
            max_up = min(start_row + (length - 1), 76)
            min_down = max(start_row - (length - 1), 0)
            
            if max_up - start_row >= length - 1:
                base_total += 1
                lowest_row = start_row
                highest_row = start_row + (length - 1)
                position_combinations = (lowest_row + 1) * (highest_row + 1)
                length_total += position_combinations
        
        base_sequences_by_factor[length] = base_total
        print(f"Factor {length}:")
        print(f"  Base sequences: {base_total}")
        print(f"  Position-aware sequences: {length_total:,}")
        total += length_total
    
    return total

# Generate triangle and find base sequences
triangle = generate_triangle()

# Find and count unique sequences
sequences = find_valid_sequences(triangle)

# Calculate without generating
total_sequences = calculate_possible_sequences()
print(f"\nTotal possible position-aware sequences: {total_sequences:,}")

# Get user input
while True:
    try:
        num_sequences = input("How many sequences would you like generated? ")
        num_sequences = int(num_sequences)
        if num_sequences <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer.")

# Convert sequences set to list for random sampling
sequences_list = list(sequences)

# Generate and print requested number of sequences
print(f"\nGenerating {num_sequences} position-aware sequences:")
for i in range(num_sequences):
    # Randomly select a base sequence
    base_sequence = random.choice(sequences_list)
    position_aware = generate_position_aware_sequence(base_sequence)
    print(f"{position_aware}")
