create_tokens_table_query = """ CREATE TABLE IF NOT EXISTS tokens (
                                        id integer PRIMARY KEY,
                                        token text,
                                        frequency integer
                                        ); """

insert_token_query= """ INSERT INTO tokens (token,frequency) VALUES(?,'1')
                         ON CONFLICT (token) DO UPDATE SET frequency=tokens.frequency+1;"""




