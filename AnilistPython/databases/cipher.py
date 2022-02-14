'''
Script not in use (Ver 0.1.1)
'''

import os
import sys
import time
import random

class EncryptDatabase():
    def __init__(self):
        self.output_dir = os.path.dirname(os.path.abspath(__file__))
        self.encrypted_filename = 'Anime-Storage-Encrypted.txt'
        self.decrypted_filename = 'Anime-Storage-Decrypted.txt'

        self.encryption_key = 'key.tsv'
        self.databse_file = 'test_dataset.json'

    def encrypt(self):
        data = []
        encrypted_data = []
        key = []

        with open(f"{self.output_dir}/{self.databse_file}", "r", encoding="utf-8") as file_ptr:
                data = file_ptr.readlines()

        # Kevin-Encryption (not very robust but works haha)
        count = 0
        for line in data:

            encrypted_line = ''
            encryption_key = ''
            for char in line:
                if char == '\n':
                    encrypted_line += '\n'
                    encryption_key += f'z-z\t'
                    break

                rand_subtractor = random.randint(ord(char) - 31, ord(char) - 1)
                min_char_val = int(32 / (ord(char) - rand_subtractor))
                max_char_val = int(126 / (ord(char) - rand_subtractor))

                rand_multiplier = random.randint(min_char_val + 1, max_char_val)

                assert ord(char) - rand_subtractor > 0
                assert rand_subtractor > 0

                char_val = (ord(char) - rand_subtractor) * rand_multiplier
                new_char = chr(int(char_val))

                encrypted_line += new_char
                encryption_key += f'{rand_subtractor}-{rand_multiplier}\t'

            # print(f'Original Line: >{line}<, Encrypted Line: >{encrypted_line}<')
            encrypted_data.append(f'{encrypted_line}')
            key.append(encryption_key)
            
            count += 1

            if count % 1000 == 0:
                print(f'Encrypt Count: {count}')


        print('Logging encrypted data and encryption keys...')
        with open(f"{self.output_dir}/{self.encrypted_filename}", "w", encoding="utf-8") as file_ptr:
            for encry_line in encrypted_data:
                file_ptr.write(f'{encry_line}')

        with open(f"{self.output_dir}/{self.encryption_key}", "w", encoding="utf-8") as file_ptr:
            for val in key:
                file_ptr.write(f'{val}\n')

        time.sleep(5) # avoid PC lag

    def decrypt(self):
        keys = []
        encrypted_data = []
        encry_key_dict = {}
        decrypted_data = []
        

        with open(f"{self.output_dir}/{self.encryption_key}", "r", encoding="utf-8") as file_ptr:
            keys = file_ptr.readlines()

        with open(f"{self.output_dir}/{self.encrypted_filename}", "r", encoding="utf-8") as file_ptr:
            encrypted_data = file_ptr.readlines()

        encry_key_dict = dict(zip(keys, encrypted_data))

        decryption_count = 0
        for line_keys in encry_key_dict:
            key_count = 0
            key = line_keys.strip('\n').split('\t')
            decrypted_line = ''

            for encrypted_char in encry_key_dict[line_keys]:
                decryption_multipliers = key[key_count].split('-') #[rand_subtractor - rand_multiplier]
                key_count += 1

                if encrypted_char == '\n': break
                decrypted_char_val = int(ord(encrypted_char) / int(decryption_multipliers[1]) + int(decryption_multipliers[0]))
                decrypted_line += chr(decrypted_char_val)

            decrypted_data.append(decrypted_line)
            if decryption_count % 1000 == 0: print(f'Decryption Count: {decryption_count}')
            decryption_count += 1
            

        with open(f"{self.output_dir}/{self.decrypted_filename}", "w", encoding="utf-8") as file_ptr:
            for line in decrypted_data:
                file_ptr.write(f'{line}\n')



if __name__ == '__main__':
    start_time = time.time()
    
    encryptor = EncryptDatabase()
    encryptor.encrypt()
    encryptor.decrypt()

    print(f'Total Time Spent: [{time.time() - start_time} seconds]')



# if char_val < 32:
#     print(f'RandSub = {rand_subtractor}, min_multi = {min_char_val}, max_multi = {max_char_val}, randMulti = {rand_multiplier}, orgVal = {ord(char)}')
#     sys.exit(0)