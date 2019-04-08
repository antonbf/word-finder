

#look into the text
def check_word(txt):
  txt= txt.lower()
  with open("eng_words.txt","r") as my_text:
    for linenum, line in enumerate(my_text, 1):
      if txt+'\n' in line :
        return ("%s is the %sth most common word in English")\
        % (txt,str(linenum))
    return ("I couldn't find that word")
    my_text.close()

  #get the sentence we want to evaluate
def intro() :
  sentence = input("Enter your word, or type EXIT! to exit: ")
  if sentence == "EXIT!":
    return "EXIT!"
  elif len(sentence)>0 :
    print ("You entered '{}'".format(sentence))
    return sentence

#make sure they can continue to enter words
running = True
print ("Welcome to the frequency word finder!")
while(running == True):
  s = intro()
  if s== "EXIT!":
    print ("Thank you! Goodbye!")
    running = False
  else:
    print (check_word(s) + '\n')
