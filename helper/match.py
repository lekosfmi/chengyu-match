# Matching methods
#
# vocab_to_match:
# - Are the vocabularies that
#   the user is going to see
#
# vocab_by_user:
# - Are the vocabularies that the
#   user is going to input
#

def match(vocab_to_match, vocab_by_user):

    for i in range(len(vocab_to_match)):
        print("### " + vocab_to_match[i] + " ###")
        user_input = input("> ")

        if user_input == vocab_by_user[i]:
            print('>> 👍  <<<')
        else:
            print(">>> " + vocab_to_match[i] + " <<<")
