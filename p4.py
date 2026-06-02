import string

# ─────────────────────────────────────────
# Step 1: Read the text file
# ─────────────────────────────────────────
filename = input("Enter the text file name (e.g., sample.txt): ")

try:
    with open(filename, 'r') as file:
        text = file.read()

    # ─────────────────────────────────────────
    # Step 2: Clean the text
    # - Convert to lowercase
    # - Remove punctuation
    # ─────────────────────────────────────────
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    # ─────────────────────────────────────────
    # Step 3: Split text into words
    # ─────────────────────────────────────────
    words = text.split()

    # ─────────────────────────────────────────
    # Step 4: Build frequency dictionary
    # ─────────────────────────────────────────
    freq_dict = {}

    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    # ─────────────────────────────────────────
    # Step 5: Sort dictionary by frequency
    #         in reverse (descending) order
    # ─────────────────────────────────────────
    sorted_dict = dict(
        sorted(
            freq_dict.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )

    # ─────────────────────────────────────────
    # Step 6: Slice first 10 items
    # ─────────────────────────────────────────
    top_10 = dict(list(sorted_dict.items())[:10])

    # ─────────────────────────────────────────
    # Step 7: Display Results
    # ─────────────────────────────────────────
    print("\n" + "=" * 40)
    print("   TOP 10 MOST FREQUENTLY USED WORDS")
    print("=" * 40)
    print("{:<6} {:<20} {:<10}".format("Rank", "Word", "Frequency"))
    print("-" * 40)

    for rank, (word, freq) in enumerate(top_10.items(), start=1):
        print("{:<6} {:<20} {:<10}".format(rank, word, freq))

    print("=" * 40)
    print("Total unique words in file : {}".format(len(freq_dict)))
    print("Total words in file        : {}".format(len(words)))
    print("=" * 40)

except FileNotFoundError:
    print("\nError: File '{}' not found. Please check the filename.".format(filename))
