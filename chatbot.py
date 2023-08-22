import re

class Chatbot:
    def __init__(self):
        self.responses = {
            "services": self.services,
            "product_quality": self.product_quality,
            "online_sale": self.online_sale,
            "factory": self.factory,
            "brands": self.brands,
            "prices": self.prices
        }

    def services(self):
        return "We provide an broad range of services from all over the india.Anyone can be able to buy the product from anywhere we help customers for their problems."

    def product_quality(self):
        return "We are committed to delivering high-quality products that meet industry standards."

    def online_sale(self):
        return "We frequently offer online sales and discounts. Please visit our website for more details."

    def factory(self):
        return "Our products are manufactured in our state-of-the-art factory with advanced technology."

    def brands(self):
        return "We offer products from multiple renowned brands to ensure a diverse selection."

    def prices(self):
        return "For information on prices, please check our website or contact our customer support."

    def get_response(self, question):
        for keyword, response in self.responses.items():
            if re.search(keyword, question, re.IGNORECASE):
                return response()
            if question=="hi":
                return "Hi! How may i assit you"
        return "I'm sorry, I don't have information on that topic."

def main():
    chatbot = Chatbot()
    print("Hi! It is an system generated chatbot for food factory")
    print("press exit to end the conversaation")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Thankyou ! Have a nice day!")
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
