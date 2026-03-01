# IMPORT PYKAKASI 
import pykakasi 

kks = pykakasi.kakasi()
text = '（リコーダーの演奏）' # kanji subs 

# hepburn = hiragana

result = kks.convert(text);
# print(result[3]['hepburn']);

for item in result: 
    print(item['hepburn']);
    # print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(
    #     item['orig'], 
    #     item['kana'], 
    #     item['hira'], 
    #     item['hepburn']
    # ))