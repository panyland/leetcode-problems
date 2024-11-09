def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
    

def longest_subs_palindrome(string):
    longest = ""
    for j in range(len(string)):
        for i in range(len(string)):
            current = string[j:i+2]
            is_pal = is_palindrome(current)
            if is_pal and len(current) > len(longest):
                longest = current
    return longest


def main():
    s = "regergsaippuakivikauppiasaetrgagtarada"
    out = longest_subs_palindrome(s)
    print(out)


if __name__ == "__main__":
    main()