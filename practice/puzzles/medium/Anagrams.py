alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def reverse_phase_4(phrase):
    words, ln, line, decoded = phrase.split(), [], "", ""
    for w in words:
        ln.append(len(w))
        line += w
    ln.reverse()
    ind = 0
    for i in range(len(ln)):
        decoded += line[ind:ind+ln[i]] + " "
        ind += ln[i]
    return decoded.strip()


def reverse_phase_3(phrase):
    phrase_list, hold_let, hold_ind = [c for c in phrase], [], []
    for i in range(len(phrase_list)):
        if phrase_list[i].isalpha() and alpha.index(phrase_list[i]) % 4 == 3:
            hold_ind.append(i)
            hold_let.append(phrase_list[i])

    if len(hold_let) > 1:
        hold_let_shift = [hold_let[-1]] + hold_let[0:len(hold_let)-1]
        for i in range(len(hold_ind)):
            phrase_list[hold_ind[i]] = hold_let_shift[i]
    return "".join(c for c in phrase_list)


def reverse_phase_2(phrase):
    phrase_list, hold_let, hold_ind = [c for c in phrase], [], []
    for i in range(len(phrase_list)):
        if phrase_list[i].isalpha() and alpha.index(phrase_list[i]) % 3 == 2:
            hold_ind.append(i)
            hold_let.append(phrase_list[i])

    if len(hold_let) > 1:
        hold_let_shift = hold_let[1:len(hold_let)] + [hold_let[0]]
        for i in range(len(hold_ind)):
            phrase_list[hold_ind[i]] = hold_let_shift[i]
    return "".join(c for c in phrase_list)


def reverse_phase_1(phrase):
    phrase_list, hold_let, hold_ind = [c for c in phrase], [], []
    for i in range(len(phrase_list)):
        if phrase_list[i].isalpha() and alpha.index(phrase_list[i]) % 2 == 1:
            hold_ind.append(i)
            hold_let.append(phrase_list[i])

    if len(hold_let) > 1:
        hold_let_shift = list(reversed(hold_let))
        for i in range(len(hold_ind)):
            phrase_list[hold_ind[i]] = hold_let_shift[i]
    return "".join(c for c in phrase_list)


phrase = input()
phrase = reverse_phase_4(phrase)
phrase = reverse_phase_3(phrase)
phrase = reverse_phase_2(phrase)
phrase = reverse_phase_1(phrase)
print(phrase)
