import srt
import pykakasi

# load file and open it in srt.  : 
with open("./japanese_sub.srt", "r", encoding="utf-8") as s:  
  srt_content = s.read()

subtitles = list(srt.parse(srt_content))

# assign converter 
kks = pykakasi.kakasi()

# read total length of subtitle block 
total_blocks = len(subtitles)-1 # -1 cause, list is indexed from 0

# Composing SRT from python objects 
# print(srt.compose(subtitles)) 

# print content of subtitle block
print(subtitles[0].content)
textForConversion = subtitles[0].content; 

# for s in subtitles: 
  # print(s.content) 


conversionResult = kks.convert(textForConversion);

for item in conversionResult: 
    print(item['hepburn'], end=" ");