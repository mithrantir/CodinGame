
def make_word(word, letters):
    wl = [c for c in word]
    ll = [c for c in letters]
    for c in wl:
        if c not in ll:
            return False
        ll.pop(ll.index(c))
    return True


letter_value = {'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1,
                's': 1, 'u': 1, 'd': 2, 'g': 2, 'b': 3, 'c': 3, 'm': 3, 'p': 3,
                'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8,
                'q':10, 'z':10}


def word_value(word):
    sm = 0
    for c in word:
        sm += letter_value[c]
    return sm


n = int(input())
diction = []
for i in range(n):
    diction.append(input())

letters = input()
best_word, best_value = "", 0
for word in diction:
    if make_word(word, letters):
        temp_value = word_value(word)
        if temp_value > best_value:
            best_word, best_value = word, temp_value

print(best_word)
