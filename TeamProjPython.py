def Open(file_name, mode):

    try:
        file = open(file_name, mode)
    except:

        return None

    else:
        return file


file_name = "Questions.txt"

file_w = Open(file_name, "w")

if file_w is not None:

    file_w.write("Konoplenko - What data types are in Python?\n")

    print(f"Information was successfully added to {file_name}!")

    file_w.close()

else:
    print("Error occures while opening the file!")

    #       ↑
#Vlad Konoplenko KN-33-1

file_w = Open(file_name, "a")

if file_w is not None:

    file_w.write("Duzhak - Python has the following data types: numbers(int, float, complex), lines(str), \nlists(list, tuple, range), dictionaries(dict), logical(bool), plural(set, frozeenset). \nHow can you read and write data to a file in Python?")

    print(f"Information was successfully added to {file_name}!")

    file_w.close()

else:
    print("Error occures while opening the file!")

        #       ↑
#Ivan Duzhak KN-33-1