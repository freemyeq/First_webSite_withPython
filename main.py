

def main():
    name = get_firstName_lastName()
    info = get_info_about_user()

    web_file = open("Web_str.html", "w")

    web_file.write("<html>\n")
    web_file.write("<head>\n")
    web_file.write("</head>\n")
    web_file.write("<body>\n")
    web_file.write("    <center>\n")
    web_file.write(f"   <hl>{name}</hl>\n")
    web_file.write("    </center>\n")
    web_file.write("    <hr />\n")
    web_file.write(f"    {info}\n")
    web_file.write("    <hr /> \n")
    web_file.write("</body> \n")
    web_file.write("<html>\n")

    web_file.close


def get_firstName_lastName():
    name = input("Введите 'Имя' 'Фамилия': ")
    return name


def get_info_about_user():
    info = input("Введите информацию о себе: ")
    return info


main()
