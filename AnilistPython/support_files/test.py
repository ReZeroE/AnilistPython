
import time

# start2 = time.time()
# from deep_translator import GoogleTranslator

# translator = GoogleTranslator(source='auto', target='japanese')

# for i in range(500):
#     line = 'owari no seraph'
#     text = translator.translate(f'{line} anime')
#     print(text)
#     if i % 50 == 0:
#         print(f'Count: {i}')

# end2 = time.time()


start = time.time()
from translate import AnilistPythonTranslate

translator = AnilistPythonTranslate(source='english', target='japanese')

for j in range(500):
    line = 'owari no seraph'
    text = translator.translate(f'{line} anime')
    text = text.replace(' ', '')
    print(text)