def words(input_string):
    string =input_string.lower()
    string= input_string.replace(".","")
    string = input_string.replace(",", "")
    string = input_string.replace(";", "")
    string = input_string.replace(":", "")
    string = input_string.replace(",;", "")
    new_list=[]
    string_dict={}
    if type(string)==type(str()):
        new_list=string.split()
    elif type(string)==type(dict()):
        new_list=string.keys()
    for word in new_list:
        if word.isdigit():
            word=int(word)
        if word in string_dict:
            string_dict[word]+=1
        else:
            string_dict[word]=1
    return string_dict
print words("Hello,; world.. HeLlo World")
