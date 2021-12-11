
link = input("Enter the Site Link : ")
url = link.replace("http://", "")
url = url[:url.index(".")]
password = url[:3] + str(len(url)) + str(url.count("e")) + "!"

print(password)