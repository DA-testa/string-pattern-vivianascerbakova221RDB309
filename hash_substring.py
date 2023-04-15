# python3
# Viviāna Ščerbakova 221RDB309 3.grupa

def read_input():
    # this function needs to acquire input both from keyboard and file
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
            text = file.readline().rstrip()
            return pattern, text

    if "I" in text:
        pattern = input().rstrip()
        text = input().rstrip()
        return pattern, text

    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def hashing(pattern: str, B: int, Q: int) -> int:
    result = 0
    for i in range(len(pattern)):
        result = (B * result + ord(pattern[i])) % Q
    return result


def get_occurrences(pattern: str, text: str, B: int, Q: int) -> list[int]:
    p_len = len(pattern)
    t_len = len(text)

    mult = pow(B, p_len - 1, Q)
    p_hash = hashing(pattern, B, Q)
    t_hash = hashing(text[:p_len], B, Q)

    occurrences = []
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash and pattern == text[i:i + p_len]:
            occurrences.append(i)
        if i < t_len - p_len:
            t_hash = ((t_hash - ord(text[i]) * mult) * B + ord(text[i + p_len])) % Q
        
    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    B = 13
    Q = 256
    print_occurrences(get_occurrences(*read_input(), B, Q))
