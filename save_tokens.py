import time

import sqlite3
from tqdm import tqdm

import queries
import configs
from helpers import measure_time,measure_insertions,log_analytics
from duplicate_remover import DuplicateRemover


class TokenSaver:


    def __init__(self, chunk_size):
        self.chunk_size = chunk_size
        con = sqlite3.connect('tokens.db')
        self.cur = con.cursor()
        self.cur.execute(queries.create_tokens_table_query)


        
        
    @measure_time
    @measure_insertions
    def save_tokens(self):

        print(f'\nchunk size : {self.chunk_size}\n')

        # duplicate_remover=DuplicateRemover(configs.token_file)
        # duplicate_remover.remove_duplicates_counting()
        pbar = tqdm(total=configs.token_count)

        with open(configs.counted_token_file, 'r') as f:

            pbar.update(0)
            
            for piece in self.read_in_chunks(f, self.chunk_size):

                self.cur.execute('BEGIN TRANSACTION')

                lines = piece.split('\n')[:-1]
                for line in lines:
                    
                    line_elements=line.split(',')
                    token=line_elements[0]
                    frequency=line_elements[1]
                    self.cur.execute(f"INSERT INTO tokens (token,frequency) VALUES('{token}','{frequency}')")

                pbar.update(self.chunk_size / 10)
                self.cur.execute('COMMIT')

        pbar.close()


       

    # number of character plus newline
    def read_in_chunks(self, file_object, chunk_size):
        while True:
            data = file_object.read(chunk_size)
        
            if not data:
                break
            yield data




if __name__ == '__main__':
    token_saver = TokenSaver(10 * 100000)
    token_saver.save_tokens()
