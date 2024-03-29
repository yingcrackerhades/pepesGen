import os
import re
import random

class pepesGen:
    def __init__(self, folderName, script):
        self.folderName = os.path.join(folderName, script)

    def script1(self, title, marq, message, auth, image, ytUrl, welMsg):
        with open(self.folderName, 'r') as file:
            content = file.read()

        content = content.replace('{title}', f'{title}')
        content = content.replace('{marquee}', f'{marq}')
        content = content.replace('{msg}', f'{message}')
        content = content.replace('{author}', f'{auth}')
        content = content.replace('{linkImg}', f'{image}')
        content = content.replace('{welcomMsg}', f'{welMsg}')

        id = youtubeId(ytUrl)
        if id:
            content = content.replace('{idYt}', f'{id}')
        else:
            print(f'No match found for YouTube URL: {ytUrl}')

        save = input("Output: ")
        with open(save, 'w') as file:
            file.write(content)

    def script2(self, title, name, grting, fb, email, github, ytUrl, ig):
        with open(self.folderName, 'r') as file:
            content = file.read()

        content = content.replace('HadesPwnme', f'{title}')
        content = content.replace('HADES', f'{name}')
        content = content.replace('["Surabaya Hacker Link", "XXXX", "Laztname", "Lawbyte", "YYYY", "Hades"]', f'{grting}')
        content = content.replace('{fb}', f'{fb}')
        content = content.replace('yingcrackerhades', f'{github}')
        content = content.replace('hadespwn0@gmail.com', f'{email}')
        content = content.replace('yinghades_', f'{ig}')

        id = youtubeId(ytUrl)
        if id:
            content = content.replace('{idYt}', f'{id}')
        else:
            print(f'No match found for YouTube URL: {ytUrl}')

        save = input("Output: ")
        with open(save, 'w') as file:
            file.write(content)

def youtubeId(url):
    pattern = r'^.*(?:(?:youtu\.be\/|v\/|vi\/|u\/\w\/|embed\/|shorts\/)|(?:(?:watch)?\?v(?:i)?=|\&v(?:i)?=))([^#\&\?]*).*'
    result = re.match(pattern, url)
    if result:
        return result.group(1)
    else:
        return None

if __name__ == "__main__":
    folderName = '.lib'
    script = ''
    ogol = ''
    
    chars = ['0', '1']
    colm = 26
    rows = 13
    
    for row in range(rows):
        ogol += ' ' * 10
        for col in range(colm):
            if (row < 5 or row > 7) and (col >= 8 and col <= 17):
                char = ' '
            else:
                char = random.choice(chars)
            ogol += char
        ogol += '\n'
        
    os.system('clear')
    print()
    print(ogol)
    print("[1] Script1")
    print("[2] Script2")
    print()    
    pil = input("root@hadespwnme# ")

    if pil == '1':
        script = 'script1.html'
        pepesGen = pepesGen(folderName, script)
        title = input("Title: ")
        marq = input("Marquee: ")
        message = input("Message: ")
        auth = input("Your name: ")
        image = input("Image: ")
        ytUrl = input("YouTube URL: ")
        welMsg = input("Welcome Message: ")

        pepesGen.script1(title, marq, message, auth, image, ytUrl, welMsg)
        print(f"Success make a Pepes file.")
    elif pil == '2':
        script = 'script2.html'
        pepesGen = pepesGen(folderName, script)
        title = input("Title: ")
        name = input("Name: ")
        grtingInput = input("Enter name(ex: hades, pwnme, lawbyte): ")
        grting = grtingInput.split(',')
        fb = input("Facebook: ")
        email = input("Email: ")
        ytUrl = input("YouTube URL: ")
        github = input("Github: ")
        ig = input("Instagram: ")

        pepesGen.script2(title, name, grting, fb, email, github, ytUrl, ig)
        print(f"Success make a Pepes file.")
    else:
        print("Invalid choosing.")
