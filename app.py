# Main app file

from vocab.chin import chin_chengyu
from vocab.eng import eng_chengyu

from helper.match import chin_match
from helper.match import eng_match


which_match = input("Chinese or English? ").lower()

if which_match == "chinese":
    chin_match()
elif which_match == "english":
    eng_match()
