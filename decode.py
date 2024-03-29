# a simple Python function to decode a message_file.txt 

# message file has format of:
# 3 love
# 6 computers
# 2 dogs
# 4 cats
# 1 I
# 5 you
#
# to decode: organize each line based on num associated, into a pyramid, ascending order, 1 at the top, each row is to have +1 values as the row before it


message1 = 'D:\Beginning\Coding\Projects\Python\MessingAround\message1.txt'
message2 = 'D:\Beginning\Coding\Projects\Python\MessingAround\message2.txt'
message3 = 'D:\Beginning\Coding\Projects\Python\MessingAround\message3.txt'


def decode(message_file):
    dict = {}
    answer_dict = {}
    return_string = ""

    # read file
    with open(message_file, 'r') as f:
        for _, line in enumerate(f, start=1):
            # clean data and insert into dict
            num, word = line.strip().split(' ', 1)
            dict[int(num)] = word

    # grab right side of pyramid
    x = 1
    nextLevel= x + 1
    while x <= len(dict):
        answer_dict[x] = dict[x] 
        x += nextLevel
        nextLevel+=1
    
    # encode dict answers into answer string
    for k in answer_dict:
        return_string += " " + answer_dict[k]
    return_string = return_string.lstrip()
    return return_string


# for testing purposes
# print("#####    Decoded MESSAGE1: ")
# print(decode(message1))
# print("#####    Decoded MESSAGE2: ")
# print(decode(message2))
# print("#####    Decoded MESSAGE3: ")
# print(decode(message3))
# print("#####    Optimized_Decoded MESSAGE1: ")
# print(decode2(message1))
# print("#####    Optimized_Decoded MESSAGE2: ")
# print(decode2(message2))
# print("#####    Optimized_Decoded MESSAGE3: ")
# print(decode2(message3))
print("##### end of script #####")