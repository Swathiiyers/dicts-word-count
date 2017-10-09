def word_count(file_path):
    """Given a file, counts the number of times a space-separated word occurs in
    that file.

    """

    # Create empty dictionary.
    word_count = {}

    # Open file. Create file object.
    with open(file_path) as text_file:

        # Iterate line-by-line over file object.
        for line in text_file:
            # Strip all trailing white space.
            line = line.rstrip()
            # Split line on "space character" to generate a list of words.
            words = line.split(" ")

            # Iterate word-by-word over list of words.
            for word in words:
                # If word (key) in dictionary, increment value by +1 for each
                # iteration. If word not in dictionary, add to dictionary and
                #set value to 0.
                word_count[word] = word_count.get(word, 0) + 1

        # Unpack the tuples that .iteritems() returns and bind to identifiers.
        for word, count in word_count.iteritems():
            # Print values for word and count
            print word, count


# Call function.
word_count('test.txt')
