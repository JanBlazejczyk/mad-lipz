def replace_words(list_of_words_arg):
    for i in range(len(list_of_words_arg)):
        if list_of_words_arg[i] == 'ADJECTIVE':
            users_word = input('Type your adjective!')
            list_of_words_arg[i] = users_word
        elif list_of_words_arg[i] == 'ADJECTIVE,':
            users_word = input('Type your adjective!')
            list_of_words_arg[i] = users_word + ','
        elif list_of_words_arg[i] == 'ADJECTIVE.':
            users_word = input('Type your adjective!')
            list_of_words_arg[i] = users_word + '.'
        elif list_of_words_arg[i] == 'NOUN':
            users_word = input('Type your noun!')
            list_of_words_arg[i] = users_word
        elif list_of_words_arg[i] == 'NOUN,':
            users_word = input('Type your noun!')
            list_of_words_arg[i] = users_word + ','
        elif list_of_words_arg[i] == 'NOUN.':
            users_word = input('Type your noun!')
            list_of_words_arg[i] = users_word + '. '
        elif list_of_words_arg[i] == 'VERB':
            users_word = input('Type your verb!')
            list_of_words_arg[i] = users_word
        elif list_of_words_arg[i] == 'VERB,':
            users_word = input('Type your verb!')
            list_of_words_arg[i] = users_word + ','
        elif list_of_words_arg[i] == 'VERB.':
            users_word = input('Type your verb!')
            list_of_words_arg[i] = users_word + '.'


def list_to_string(our_list):
    final_sentence = ''
    for word in our_list:
        final_sentence += word
        final_sentence += ' '
    print(final_sentence)
