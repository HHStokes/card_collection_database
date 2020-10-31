import sqlite3
connect =sqlite3.connect('card_collection.db')

c = connect.cursor()

#c.execute('CREATE TABLE cards(name, type, varient, year, count, id type unique)')
#c.execute('ALTER TABLE cards MODIFY "id" UNIQUE')

def addCard(totalCards):
    cardName =  input("Card name: ")
    cardType = input("Card energy type: ") 
    cardVariant = input("Card varient/rarity: ")
    cardYear = input("Year printed: ")
    cardCount = input("Number copies: ")
    newId = totalCards + 1;

    cardData = [cardName,cardType,cardVariant,cardYear,cardCount, newId]
    c.execute('INSERT INTO cards VALUES (?,?,?,?,?,?)',cardData)
    connect.commit()
    return newId

def editCard():
    print("What value do you need to edit?")
    print("\t1. Name")
    print("\t2. Type")
    print("\t3. Varient")
    print("\t4. Year")
    print("\t5. Number of Cards Owned")
    change = input(">")
    newValue = input("Change to: ")
    cardID = input("Card ID: ")
    if change in["1.", 1, "1"]:
        c.execute('UPDATE cards SET "name" = ? WHERE "id" = ?',(newValue, cardID))
        connect.commit()
    elif change in["2.",2,"2"]:
        c.execute('UPDATE cards SET "type" = ? WHERE "id" = ?',(newValue,cardID))
        connect.commit()
    elif change in["3.",3 ,"3"]:
        c.execute('UPDATE cards SET "varient" = ? WHERE "id" = ?',(newValue, cardID))
        connect.commit()
    elif change in["4.", 4, "4"]:
        c.execute('UPDATE cards SET "year" = ? WHERE "id" = ?',(newValue, cardID))
        connect.commit()
    elif change in["5.", 5 , "5"]:
        c.execute('UPDATE cards SET "count" = ? WHERE "id" = ?',(newValue, cardID))
        connect.commit()
    else:
        print("Invalid input")



def deleteCard():
    print("Each card has an id integer. Please type in the id.")
    search = input(">")

    print("The card you selected is: ")
    for row in c.execute('SELECT * FROM cards WHERE "id" = ?', (search,)):
        print(row)
        
    print("Are you sure you want to delete this card? Y/N?")
    choice = input(">")
    if choice in ["Yes", "YES", "yes","y","Y"]:
        c.execute('DELETE FROM cards WHERE id = ?',(search,))
    else:
        print("Deletion cancelled")

    

def searchCards():
    print("This searches by name, or type ALL to display all")
    selection = input("Seach for: ")
    if selection in ["ALL","all", "All", "a","A"]:
        for row in c.execute('SELECT * FROM cards ORDER BY name'):
            print(row)
    else:
        #c.execute('SELECT ? FROM cards Order BY name', [selection])
        for row in c.execute('SELECT * FROM cards WHERE name = ? ORDER BY name', [selection]):
            print(row)

def main():
    cardCount = 0;
    for row in c.execute('SELECT * FROM cards ORDER BY name'):
            cardCount = cardCount + 1
    
    print("SQLITE_VERSION: " + sqlite3.sqlite_version)
    loop = True
    while loop == True:
        print("Welcome to the card collection database interface")
        print("Select an option by typing a number or exit by typing 'QUIT'")
        print("\t1. Add a card")
        print("\t2. Edit existing card")
        print("\t3. Delete existing card")
        print("\t4. Search for a card/cards")
        responce = input(">")
        if responce in ["1.", 1, "1"]:
            cardCount = addCard(cardCount)

        elif responce in ["2.", 2 ,"2"]:
            editCard()
        
        elif responce in ["3.", 3 ,"3"]:
            deleteCard()
        
        elif responce in ["4.", 4 ,"4"]:
            searchCards()

        elif responce in ["QUIT", "quit","Quit","q","Q"]:
            print("Thank you for using this interface. See you again!")
            loop = False
            connect.close()
        else:
            print("Invalid input. Try Again.")
    
main()
