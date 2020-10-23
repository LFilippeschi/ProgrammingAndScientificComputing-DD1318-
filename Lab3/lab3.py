import text_encryption_function
import random
import json

# UPPGIFT 1


def copy_text_file(in_file, out_file):
    fr = open(in_file, 'r')
    txt = fr.read()
    fr.close()
    fw = open(out_file, 'w')
    fw.write(txt)
    fw.close()


copy_text_file("namn.csv", "my_copy.csv")

# UPPGIFT 2


def encrypt_file(in_file, out_file):
    fr = open(in_file, 'r')
    txt = fr.read()
    fr.close
    txt = text_encryption_function.encrypt(txt)
    fw = open(out_file, 'w')
    fw.write(txt)
    fw.close()
# encrypt_file("namn.csv", "secret_names.csv")

# UPPGIFT 3


def user_dialogue():
    out_file = input("Name of new encrypted file: ")
    while True:
        try:
            in_file = input("Name of file to be encrypted: ")
            encrypt_file(in_file, out_file)
            break
        except Exception as e:
            print('That resulted in an input/output error, please try again! ' + str(e))
            continue
    print("Encryption completed!")

user_dialogue()

# UPPGIFT 4


def get_int_input(prompt_string, low, max):
    while True:
        try:
            x = int(input(prompt_string))
            if x < low or x > max:
                print('Out of bound!')
                continue
            return x
        except Exception as e:
            print('Svara med ett heltal!')
            continue

# get_int_input('>')

# UPPGIFT 5


short_quiz_list_of_lists = [['Vad heter Norges huvudstad?', 'Oslo', 'Bergen', 'Köpenhamn'],
                            ['Vad står ABBA för?', 'Agneta Björn Benny Annefrid',
                                'Kalle och Lisa', 'Smarrig Sill'],
                            ['What ingredient is always in pizza?', 'flour', 'candies', 'soup']]


def run_quiz(quiz_list_of_lists):
    print('-'*50)
    print('Hello and welcome to the quiz!')
    print('-'*50)

    for x in quiz_list_of_lists:
        print(x[0])
        list = [1, 2, 3]
        answ = []
        y = 1
        while y < 4:
            pos = random.randint(0, len(list)-1)
            pick = x[list[pos]]
            answ.append(pick)
            list.remove(list[pos])
            print('Alternativ ' + str(y) + ': ' + pick)
            y = y+1
        answer = get_int_input('Vilket är ditt svar? (1,2,3): ', 1, 3)
        if answ[answer-1] == x[1]:
            print('Rätt, det är: ' + answ[answer-1])
            print('-'*50)
        else:
            print('Fel, det rätta svaret är: ' + x[1])
            print('-'*50)


# run_quiz(short_quiz_list_of_lists)


# UPPGIFT 6/7/8

def get_quiz_list_handle_exceptions():
    text = 0
    while True:
        name_file = input('Name of quiz file: ')
        if name_file[-4:] != '.csv':
            print('That resulted in an input/output error, please try again!')
            continue
        else:
            fr = open(name_file, 'r')
            text = fr.readlines()
            fr.close()
            count = 0
            wrong_format = False
            for x in text:
                count = 0
                for c in x:
                    if c == ';':
                        count += 1
                if count < 3:
                    print(
                        'The file is not of the proper format. There needs to be four strings, separated by ; in each line of the file.')
                    wrong_format = True
                    break
                else:
                    continue
            if wrong_format == False:
                break
            else:
                continue
    list=[]
    for x in text:
        tmp = x.strip('\n')
        tmp = tmp.split(';')
        list.append(tmp)
    return list

#run_quiz(get_quiz_list_handle_exceptions()) #run quiz by importing questions from .csv file and checking if the file is of the right format

ql = get_quiz_list_handle_exceptions()
json_string = json.dumps(ql, indent=2)
fo = open("quiz.json", "w")
fo.write(json_string)
fo.close()