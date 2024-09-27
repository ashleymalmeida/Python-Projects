#Scratch Coding:

string1 = input("Choose a name : ")
string2 = input("Insert your close friend's name : ")
string3 = input("A word to decribe your friend : ")
string4 = input("What bad thing did your ex-friend did to affect you?: ")

story = """There was a little girl whose name was {} , She was like no other girl,
She is brilliant, beautiful, amazing, and smart. Nobody knew her well enough nor
ever see her. She lost many people on her way of her journey until suddenly she
met someone named {} . He/She was like any original person but {} never knew that
person was going to show her the reality of a friendship like no other. Little by
little she was knowing the person that at one point that person became someone
{}. After all she went through she finally had someone who would be there
for her every moment and step motivating her to be the best version of herself
not like those who never were there for her because they {} and it affected her
deeply"""


print(story.format(string1, string2, string3, string4))
      
