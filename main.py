import requests
import csv

class CoinRobot:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"

    def get_coin_price(self, coin_id):
        url = f"{self.base_url}/simple/price?ids={coin_id}&vs_currencies=usd"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if coin_id in data:
                return data[coin_id]["usd"]
            else:
                return "Moeda não encontrada."
        else:
            return "Erro ao recuperar cotação."

    def save_coin_price(self, coin_id, price):
        with open('coin_prices.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([coin_id, price])

if __name__ == "__main__":
    bot = CoinRobot()
    coin_id = input("Digite o ID da moeda que deseja obter a cotação: ").lower()
    price = bot.get_coin_price(coin_id)
    if isinstance(price, float):
        print(f"O preço do {coin_id} é: ${price}")
        bot.save_coin_price(coin_id, price)
    else:
        print(price)
