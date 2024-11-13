my_list = [1, 2, 3]
my_tuple = (4, 5)
a, b, c = my_list
d, e = my_tuple
print(a, b, c, d, e)
my_list_2 = [1, 2, 3, 4, 5, 6]
print(my_list_2[0:5])
print(my_list_2[3:])
print(my_list_2[:5:2])
print(my_list_2[::])
print(my_list_2[::-1])
print(my_list_2[-2:-6:-1])

text = "rly long text"
print(text[5])
print(len(text))
print(text.index("long"))
print("long" in text)
print(text.count("l"))
print(text.find("o"))
print(text[:7])
print(text.startswith("rl"))
print(text.endswith("xt"))

text_2 = "rly lOng teXt AgaIn"
print(text_2.capitalize()) # Делает первую букве предложения заглавной
print(text_2.title()) # Делает каждую первую букву заглавной
print(text_2.upper()) # Делает все буквы большими
print(text_2.lower()) # Делает все буквы маленькмим

mssg = "Hell o Wor"
print(mssg)
mssg = mssg.replace("Hell o", "Hello")
print(mssg)

text_3 = "'text'"
print(text_3)
text_3 = text_3.strip("'")
print(text_3)

my_string = "some little text"
my_string_2 = "some,little,text"

list_my_string = my_string.split()
list_my_string_2 = my_string_2.split(",")
print(list_my_string)
print(list_my_string_2)

lang = ["Pyt", "Java", "Go"]
print(lang)
lang = ",".join(lang)
print(lang)

my_text = "First {} or Second {}"
first_num = "1"
second_num = "2"
print(my_text.format(first_num, second_num))