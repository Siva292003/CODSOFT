def pizza_bot(user_input):
    user_input = user_input.lower()

    rules = {
        'hello': 'Hi there! Welcome to our pizza delivery service. How can I assist you today?',
        'menu': 'Sure, we offer a variety of pizzas including pepperoni, margherita, and vegetarian. What would you like to order?',
        'delivery': 'Yes, we provide delivery services. May I have your address and contact number?',
        'bye': 'Thank you for considering us! Have a great day!'
        # More rules can be added for ordering, customization, etc.
    }

    for rule, response in rules.items():
        if rule in user_input:
            return response

    return "I'm sorry, I didn't catch that. Please ask about our menu, delivery, or place an order."

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Pizza Bot: Goodbye!")
        break

    bot_response = pizza_bot(user_input)
    print("Pizza Bot:", bot_response)
