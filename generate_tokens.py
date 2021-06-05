import string
import random
import configs


def generate_tokens():
    with open(configs.token_file, 'a') as f:
        for i in range(configs.token_count):
            token = "".join(random.choice(string.ascii_lowercase) for i in range(configs.token_length))
            f.write(f'{token}\n')


if __name__ == '__main__':
    generate_tokens()
