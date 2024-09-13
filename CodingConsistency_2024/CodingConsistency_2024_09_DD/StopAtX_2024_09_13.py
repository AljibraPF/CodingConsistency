#Function to  stop at a specific letter
def stopAtX():
    BookShelf = "ABooCaaaa"
    for i in range(len(BookShelf)):
        if BookShelf[i] == "C":
            break
        else:
            print(BookShelf[i])

stopAtX()

