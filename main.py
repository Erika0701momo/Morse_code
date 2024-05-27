from morse import morse_dict

print(r"""
   _____                                                .___
  /     \   ___________  ______ ____     ____  ____   __| _/____
 /  \ /  \ /  _ \_  __ \/  ___// __ \  _/ ___\/  _ \ / __ |/ __ \
/    Y    (  <_> )  | \/\___ \\  ___/  \  \__(  <_> ) /_/ \  ___/
\____|__  /\____/|__|  /____  >\___  >  \___  >____/\____ |\___  >
        \/                  \/     \/       \/           \/    \/
""")
flag = 0
while flag == 0:
    string = input("Please enter a sentence. >>").lower()
    new_string = string.replace(" ", "")
    print("Here's your morse code:")
    for letter in new_string:
        print(morse_dict[letter])
    answer = input('Would you like to continue? Type y or n >>')
    if answer == 'n':
        flag = 1
