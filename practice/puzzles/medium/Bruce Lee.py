
def check_message(msg):
    if len(msg) % 2 == 1:
        return False
    for s in msg:
        if len(set(s)) > 1 or s[0] != '0':
            return False

    sm = 0
    for i in range(0, len(msg)-1, 2):
        sm += len(msg[i+1])
        if len(msg[i]) > 2:
            return False
    if sm % 7 != 0:
        return False
    return True


decode = {'0': '1', '00': '0'}
encrypt = input().split()
if check_message(encrypt):
    binary_msg, decrypt = "", ""
    while len(encrypt) > 0:
        bin_dig = decode[encrypt.pop(0)]
        binary_msg += len(encrypt.pop(0)) * bin_dig
    for i in range(0, len(binary_msg), 7):
        decrypt += chr(int(binary_msg[i:i+7],2))
    print(decrypt)
else:
    print("INVALID")
