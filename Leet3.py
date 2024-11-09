# Finds longest substring from a string
def longest(string):
    count = 0
    longest = 0
    chars = []
    for i in range(len(string)):
        if string[i] in chars:
            if count > longest:
                longest = count
            count = 0
            chars = []
            chars.append(string[i])
            count = 1
        else:
            chars.append(string[i])
            count += 1
    return longest


def main():
    s = "hsthththththth"
    out = longest(s)
    print(out)


if __name__ == "__main__":
    main()