pois = {"Parliament": "28°37'2\"N, 77°12'29\"E", 
        "Wankhede": "18°56'20.10\"N, 72°49'32.60\"E",
        "Nalanda": "25°8'12\"N, 85°26'38\"E",
        "Mahabalipuram": "12°37'21.817\"N, 80°11'38.080\"E"
        }
user_text = input("")
words = user_text.split()
output = ""
for word in words:
    if word in pois:
        output += pois[word]
    else:
        output += word
    output += " "
print(output)
