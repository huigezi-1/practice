import sys

def main():
    words_list = []
    lines = sys.stdin.readlines()

    for line in lines:
        stripped_line = line.strip()
        if stripped_line: 
            words_in_line = stripped_line.split()
            words_list.extend(words_in_line)
    print(words_list)

if __name__ == "__main__":
    main()
