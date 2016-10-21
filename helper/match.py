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

    counter = 0

    for i in range(len(vocab_to_match)):
        print("### " + vocab_to_match[i] + " ###")
        user_input = input("> ").replace(" ", "")

        if user_input == vocab_by_user[i]:
            counter += 1
            print('>> 👍  <<<')
        else:
            print(">>> " + vocab_to_match[i] + " <<<")

    print('Score: {0}/{1} 🚀'.format(counter, len(vocab_to_match)))
