text = ("This is a sample text that contains the word 'sample' multiple times.\n"
        "The purpose of this text is to demonstrate how to find and replace the word "
        "'sample' with another word, such as 'example'.\nBy doing so, we can see how "
        "string manipulation works in Python.\nLet's replace 'sample' with 'example' "
        "and see the result.")


file = open("test.txt", "w")
file.write(text)
file.close()
