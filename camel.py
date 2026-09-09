""" Camelcase program """

def camelcase(sentence):
    #convert sentence to camelCase
    title_case = sentence.title()#uppercase first letter of each word
    upper_camel_cased = title_case.replace(' ','') # remove spaces
    #lowercase first letter, join with rest of string
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def banner():
    """ Display program name """
    message = 'Awesome camelcase program!'
    stars = '*' * len(message)
    print(f'n{stars}\n{message}\n{stars}\n')

def instructions():
    """ Display instructions to user """
    print('Enter a sentence and I will convert it to camelCase for you!')

          


def main():
    banner()
    instructions()
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()