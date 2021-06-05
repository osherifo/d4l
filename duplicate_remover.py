import configs
from helpers import measure_time


class DuplicateRemover:

    def __init__(self, token_file):
        self.token_file = token_file

    @measure_time
    def sort_tokens(self):
        print('Sorting tokens...')
        with open(self.token_file, 'r') as f:
            tokens = f.read().splitlines()
        tokens.sort()
        return tokens

    @measure_time
    def hash_tokens(self, tokens):
        print('Hashing tokens...')
        token_counts = {}
        for token in tokens:
            if token not in token_counts:
                token_counts[token] = 1
            else:
                token_counts[token] = token_counts[token] + 1
        return token_counts

    # generates two arrays , one for the indices of the tokens and the other with corresponding counts of these indices
    @measure_time
    def count_tokens(self, tokens):
        print('Counting duplicate tokens...')
        token_counts = []
        indices = []

        current_element = tokens[0]
        current_count = 1
        current_index = 0

        for i in range(1, len(tokens)):
            if tokens[i] == current_element:
                current_count = current_count + 1
            else:
                indices.append(current_index)
                token_counts.append(current_count)

                current_index = i
                current_element = tokens[i]
                current_count = 1

        return [tokens, indices, token_counts]

    @measure_time
    def write_hashed_tokens(self, token_counts):
        print(f'Writing tokens to {configs.hashed_token_file}')
        with open(configs.hashed_token_file, 'w') as f:
            for key, value in token_counts.items():
                f.write(f'{key[:]},{value}\n')

    @measure_time
    def write_counted_tokens(self, token_data):
        print(f'Writing tokens to {configs.counted_token_file}')
        tokens = token_data[0]
        indices = token_data[1]
        token_counts = token_data[2]
        with open(configs.counted_token_file, 'w') as f:
            for i in range(len(indices)):
                f.write(f'{tokens[indices[i]][:]},{token_counts[i]}\n')

    @measure_time
    def remove_duplicates_hashing(self):
        self.write_hashed_tokens(self.hash_tokens(self.sort_tokens()))

    # performs slightly better
    @measure_time
    def remove_duplicates_counting(self):
        self.write_counted_tokens(self.count_tokens(self.sort_tokens()))
