#Yusef Bayyat
#8/28/20
#option 1
import math

def main():
    name = input("What's your name?")
    print("Hello " +name+ ", today we are going to be shopping at one of my favorite clothing stores, Nike!")
    print("Let's look at some clothing items and you can pick how many of each item you wanna buy.")
    print("Oh wow look at all these nice Nike shirts!")
    totalNikeShirts = (int(input("How many would you like to buy?")))
    print("Nice I think getting " +str(totalNikeShirts)+ " shirt(s) was a great idea")
    print("")
    print("This store has a massive selection of pants, lets go take a look at some pants.")
    print("Oh wow look at these super nice Nike pants!")
    totalNikePants = (int(input("How many would you like to buy")))
    print("Nice getting " +str(totalNikePants)+ " pant(s) was super smart.")
    print("")
    print("To complete your outfit I think we should get you some shoes, lets go take a look at their selection.")
    print("Hey look, they have aisles of aisles of shoes here.")
    totalNikeShoes = (int(input("How many would you like to buy?")))
    print("Congrats on the " +str(totalNikeShirts)+ " shirts(s)," +str(totalNikePants)+ " pant(s), " +str(totalNikeShoes)+" shoe(s). ")
    #calculations
    costNikeShirts = totalNikeShirts*19.99
    costnikepants = totalNikePants*24.99
    costnikeshoes = totalNikeShoes*59.99
    subtotal = costNikeShirts + costnikepants + costnikeshoes
    tax = subtotal*.065
    shipping =5.99
    orderTotal = float(tax + shipping + subtotal)
    #Printed Order
    print("")
    print("------------------------------------------------")
    print("Item               Cost")
    print("Nike Shirts        $19.99")
    print("Nike Pants         $24,99")
    print("Nike Shoes         $59.99")
    print("Subtotal           $"      +str(subtotal))
    print("------------------------------------------------")
    print("Tax                $"      +str(tax))
    print("Shipping           $"      +str(shipping))
    print("Order Total        $"      +str(orderTotal))
    print("------------------------------------------------")










main()
