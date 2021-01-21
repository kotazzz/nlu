from prompt_toolkit import prompt

if __name__ == '__main__':

    text = prompt('Give me some input: ')
    print('You said: %s' % text)