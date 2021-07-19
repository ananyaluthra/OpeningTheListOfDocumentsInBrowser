import webbrowser, sys

f = open(r"C:\Users\luthr\Desktop\Internship\Url.xlsx")
tabs = 1
counter = 1

for url in f:
    counter += 1
    webbrowser.open_new_tab(url)
    if counter == tabs:
        input("Press any key to continue...")
        counter = 1 