#Code cleans dataset and stores in clean_solar_data.txt
import re

#Load dirty text
with open(r"C:\Users\ankad\Documents\Project1\dirty_solar_data.txt","r",encoding="utf-8") as f:
    text=f.read()

#Remove references like [1], [23], etc.
#Replace multiple spaces/newlines with a single space
text= re.sub(r"\[\d+\]","",text)
text= re.sub(r"\s+"," ",text)

#Split into sentences by ". "
#Strip whitespace and drop empty strings
sentences=text.split(". ")
sentences = [s.strip() for s in sentences if s.strip()]

#Writing cleaned data
with open(r"C:\Users\ankad\Documents\Project1\clean_solar_data.txt", "w", encoding="utf-8") as f:
    for s in sentences:
        f.write(s + ".\n")
