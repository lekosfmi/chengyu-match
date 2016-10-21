# Main app file

from vocab.chin import chin_chengyu
from vocab.eng import eng_chengyu

from helper.match import match


which_match = input("Chinese or English? ").replace(" ", "").lower()

if which_match == "chinese":
    match(eng_chengyu, chin_chengyu)
elif which_match == "english":
    match(chin_chengyu, eng_chengyu)
