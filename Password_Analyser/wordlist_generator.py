import itertools

def generate_wordlist(keywords, years):
    wordlist = []
    # Combine keywords + years (e.g., "john" -> "john2025")
    for word in keywords:
        wordlist.append(word)
        for year in years:
            wordlist.append(f"{word}{year}")
            wordlist.append(f"{word.upper()}{year}")
    # Leet-speak substitutions (e.g., 'a' -> '@')
    leet_map = {'a': '@', 'e': '3', 'o': '0'}
    for word in wordlist.copy():
        for char, replacement in leet_map.items():
            if char in word:
                wordlist.append(word.replace(char, replacement))
    return wordlist

if __name__ == "__main__":
    keywords = input("Enter keywords (comma-separated): ").split(',')
    years = input("Enter years (comma-separated): ").split(',')
    wordlist = generate_wordlist(keywords, years)
    with open("wordlist.txt", "w") as f:
        f.write("\n".join(wordlist))
    print(f"Generated {len(wordlist)} passwords in 'wordlist.txt'.")