import base64

def anhTostring():
    with open("bachnhut2.jpg", "rb") as original_file:
        encoded_string = base64.b64encode(original_file.read())
        print(encoded_string)
    f2 = open("myfile.txt", "w")
    f2.write(encoded_string.decode('utf-8'))
    f2.close()

    f3=open("myfile.txt", "r")
    data=f3.read()
    f3.close()
    #print(encoded_string)
    # xmzWowsfJbpGwCe0DTveqwvos7Mf0lcVNe/Q+G1hO/p+UNPd/stUse8AhP/3fDixf8HI3No67nvhlYAAAAASUVORK5CYII='

    #print(type(encoded_string))
    with open("new_image2.jpeg", "wb") as new_file:
        #new_file.write(base64.decodebytes(data))
        new_file.write(base64.b64decode(data))
    return  new_file

anhTostring()


