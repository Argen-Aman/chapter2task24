print('Hello! Welcome to Google support and feedback service.')
print(input('My answer: ')) #You may also say hello.

file_name = 'google_' + str(input(
        'List of our branch offices given below:\n 1) Germany\n 2) Kazakhstan\n 3) KYRGYZSTAN\n 4) Moscow\n'
        ' 5) Paris\n 6) San-Francisco\n 7) Sweden\n 8) UAE\nTo which office do you want to apply: ')).lower() + '.txt'
comp = input('Your complain to this office: ')

def send_comp (file_name, comp):
    with open(file = file_name, mode = 'a') as f:
        f.write(comp)
send_comp (file_name, comp)

print('Thanks for the feedback. We care about every client and we will contact you as soon as possible.')
