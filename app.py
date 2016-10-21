# Main app file

from vocab.chin import chin_chengyu
from vocab.eng import eng_chengyu

from helper.match import match


which_match = input("Chinese or English? ").replace(" ", "").lower()

if which_match[:4] == "chin":
    match(eng_chengyu, chin_chengyu)
elif which_match[:3] == "eng":
    match(chin_chengyu, eng_chengyu)
