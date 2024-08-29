string1 = input("Choose a noun :")
string2 = input("Choose a plural noun :")
string3 = input("Choose a noun :")
string4 = input("Choose a place :")
string5 = input("Choose an adjective (Describing word):")


sentence = """Did you know I have a pet {} ?
He likes to run around and play with all of the {}
One morning, I woke up and he was wearing a {} for a hat!
I especially like to take him to the {}
because he shows off his {} side."""



print(sentence.format(string1, string2, string3, string4, string5))
