# collect the user input and store it in a variable
input("What's the weather like today ? (sunny/rainy/cold):")

# use the input to give the recommendations
if input == "sunny":
    print("Wear a t-shirt and sunglasses."),
    elif input =="rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif input == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, i don't have the recommendations for this weather.")   