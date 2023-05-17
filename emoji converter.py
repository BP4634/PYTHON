def convert_emoji(message):
    
    words = message.split(' ')
    emojis = {":)":"😃", ":(":"😔","%":"😭"}

    output = ""

    for item in words:
        output += emojis.get(item, item) + " "


    return (output)


message = input(">")

print(convert_emoji(message))


