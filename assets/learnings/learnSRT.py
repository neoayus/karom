# IMPORT SRT LIB
import srt 
from datetime import timedelta 

# PARSING A FILE 
with open("./naruto_ep01.srt", "r", encoding="utf-8") as s:  
  srt_content = s.read()

subtitles = list(srt.parse(srt_content))

# getting total length of subtitle blocks 
# print(len(subtitles))

# access subtitle content 
# print(subtitles[321].content)

# Composing SRT from python objects 
# print(srt.compose(subtitles)) 

# Convert current subtitle to SRT Block 
# sub = srt.Subtitle(
#   index=1, 
#   start=timedelta(minutes=3, seconds=36, milliseconds=804),
#   end=timedelta(minutes=3, seconds=40, milliseconds=365),
#   content="Darn, you really are rough..."
# )
# print(sub.to_srt())

