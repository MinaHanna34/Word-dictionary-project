import string

WORD_LENGTH = 5


in_secret_word_correct_spot = [] ## replace the right-hand side with the correct instructions, use indentation if needed
in_secret_word_somewhere = []## replace the right-hand side with the correct instructions, use indentation if needed
not_in_secret_word = []## replace the right-hand side with the correct instructions, use indentation if needed
words_list = [] ## replace the right-hand side with the correct instructions, use indentation if needed
N = 0 ## replace the right-hand side with the correct instructions, use indentation if needed
attempts = 0 ## replace the right-hand side with the correct instructions, use indentation if needed




def read_dictionary (file_name):
    my_project=open(file_name)
    new_dictionary_list = []
    new_dictionary_list= my_project.readlines()
    for i in range(len(new_dictionary_list)):
        temp= new_dictionary_list[i]
        new_temp=temp.lower()

        new_dictionary_list[i] = new_temp[0:-1]
    my_project.close()
    return new_dictionary_list

    return new_dictionary_list

    return new_dictionary_list

def enter_a_word (word_type, num_letters):
    a_word = input("Enter the secret "+ str(num_letters)+"-letter "+word_type+" word: ")
    
    a_word = a_word.lower()
    
    return a_word 

def is_it_a_word (input_word, dictionary_list):
    is_word = True ## replace the right-hand side with the correct instructions, use indentation if needed
    if input_word in dictionary_list and len(input_word) == 5:
        is_word= True
    else:
         is_word= False

    return is_word #Boolean variable

def enter_and_check(word_type, dictionary_list):
    in_word = '' ## replace the right-hand side with the correct instructions, use indentation if needed
    in_dict = 0## replace the right-hand side with the correct instructions, use indentation if needed
    length = len (word_type)-1 ## replace the right-hand side with the correct instructions, use indentation if needed
    checking = False
    while checking  is False:
        enter_word = enter_a_word (word_type, length)
        is_word= is_it_a_word (enter_word  , dictionary_list)


        if is_word and length == 5:
                  in_word= enter_word
                  checking = True
        elif enter_word in dictionary_list:
            print(f'You entered a {len(enter_word)}-letter word that is in the dictionary. Please try again!')
        else:
                   print(f'You entered a {len(enter_word)}-letter word that is not in the dictionary. Please try again!')
                   checking = False
                   
    return in_word 
        
#    if word_type in dictionary_list and word_type len(5):


def compare_words (player, secret):
    global remaining_alphabet
    global in_secret_word_correct_spot 
    global in_secret_word_somewhere
    global not_in_secret_word
    letter_count = 0
    index =0
    final = '' ## replace the right-hand side with the correct instructions, use indentation if needed
    in_correct_spot = 0 ## replace the right-hand side with the correct instructions, use indentation if needed
    temp = list(secret)
    replace = secret
    for i in range(len(player)):
      index =  replace.find(player[i])
      letter_count = replace.count(player[i])
      if letter_count > 1:
          temp[i] = "_"
          replace = replace.join(temp)
      if index == i:
              in_correct_spot +=1
              final = final+player[i]
              if in_secret_word_correct_spot.count(player[i]) == 0 :
                  in_secret_word_correct_spot.append(player[i])
      elif index == -1:
              final= final +"_"
              if not_in_secret_word.count(player[i]) == 0 :
                  not_in_secret_word.append(player[i])
      else:
              final= final + "("+ player[i] + ")"
              if in_secret_word_somewhere.count(player[i]) == 0 :
                  in_secret_word_somewhere.append(player[i])
      if remaining_alphabet.count(player[i]) != 0:
          remaining_alphabet.remove(player[i])
    return final, in_correct_spot # returns a string and an integer

# program code
print('Welcome to new and improved Wordle - CECS 174 edition!')
dictionary_list= read_dictionary ('project4_dictionary.txt')
words_list = read_dictionary('project4_dictionary.txt')
##print(words_list)
##print(enter_a_word ('skill', 5))
##print(is_it_a_word ('apple', ['apple', 'banana']))

##print(is_word)
##enter_a_word(word_type, 5 )
alphabet_string = string.ascii_lowercase #Create a string of all lowercase letters
remaining_alphabet = list(alphabet_string) #Create a list of all lowercase letters
alphabet_string = string.ascii_lowercase #Create a string of
remaining_alphabet = list(alphabet_string) #Create a list of
in_secret_word_correct_spot = [] # a list of all characters
in_secret_word_somewhere = [] # a list of all characters that
not_in_secret_word = [] # a list of all characters that have
words_list = [] # a list of strings that contains all words
secret_word =' ' # a sting containing the secret word
player_word = ' ' # a sting containing the player word
N = 0 # the total allowed number of attempts (guesses)
attempts = 0 # the number of attempts the user has made so
letter_in_the_right_spot = 0 # the number of letters that are

secret_word= (enter_and_check ('secret', dictionary_list))

N = int(input('Input allowed number of attempts: '))    
while  N != attempts:
    print(f'Enter your attempt #{attempts+1}')
    attempts +=1
    player_word = (enter_and_check('player', dictionary_list))


    temp1, temp2 = compare_words (player_word, secret_word)
    print(f'letter in the right spot: {temp2}')
    print(f'You guessed letters of the secret_word: {temp1}')
    print('Previously attempted letters that are in the correct spot of secret_word: ')
    print(in_secret_word_correct_spot)
    print('Previously attempted letters that are in some spot of secret_word: ')
    print(in_secret_word_somewhere )
    print('Previously attempted letters that are not in the secret_word: ')
    print(not_in_secret_word)
    print('Remaining letters of the alphabet that have not been tried: ')
    print(remaining_alphabet)
    if secret_word == player_word:
        print(f'Congrats you won using {attempts} attempt(s)')
        break
if secret_word != player_word  and attempts != 0:
    print(f'You already used #{attempts} attempts. Better luck tomorrow!')





