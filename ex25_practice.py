import ex25

sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)
print(f"words = {words}")
sorted_words = ex25.sort_words(words)
print(f"sorted_words = {sorted_words}")
ex25.print_first_word(words)
ex25.print_last_word(words)
print(f"After pop words, words = {words}")
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
print(f"After pop words, sorted_words = {sorted_words}")
sorted_words = ex25.sort_sentence(sentence)
print(f"sorted_words = {sorted_words}")
ex25.print_first_and_last(sentence)
print(f"After pop sentence, sentence = {sentence}")
ex25.print_first_and_last_sorted(sentence)
print(f"After pop sentence, sentence = {sentence}")
