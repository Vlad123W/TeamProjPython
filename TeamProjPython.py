def Open(file_name, mode):

    try:
        file = open(file_name, mode)
    except:

        return None

    else:
        return file


file_name = "Questions.txt"

file_1_w = Open(file_name, "w")

if file_1_w is not None:

    file_1_w.write("Konoplenko - What data types are in Python?")

    print(f"Information was successfully added to {file_name}!")

    file_1_w.close()

else:
    print("Error occures while opening the file!")