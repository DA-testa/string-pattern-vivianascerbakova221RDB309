# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function

    text = input()
    if "F" in text:
        folder = "./tests/" + "06"
        with open(folder, "r") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip
            return (pattern, text)

    if "I" in text:
        pattern = input().rstrip()
        text = input().rstrip()
        return (pattern, text)

    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

B = 13
Q = 256

def hashing(pattern: str) -> int:
    global B, Q
    a = len(pattern)
    result = 0
    for i in range(a):
        result = (B * result + ord(pattern[i])) % Q
    return result


def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    global B, Q
    p_len = len(pattern)
    t_len = len(text)

    mult = 1
    for i in range(1, p_len):
        mult = (mult * B) % Q

    p_hash = hashing(pattern)
    t_hash = hashing(text[:p_len])

    occurences = []
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if pattern == text[i:i + p_len]:
                occurences.append(i)
        if i < t_len - p_len:
            t_hash = ((t_hash - ord(text[i]) * mult) * B + ord(text[i + p_len])) % Q
        

    # and return an iterable variable
    return occurences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
