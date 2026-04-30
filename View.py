import pandas as pd
from Config import DECIMALS, CURRENCY


class Display:

    def show_menu(self):
        """Affiche le menu principal et retourne le choix de l'utilisateur."""

        print()
        print("1. Acheter")
        print("2. Vendre")
        print("3. Voir portefeuille")
        print("4. Quitter")

        return input("Choix : ")

    def ask_buy(self):
        """Demande à l'utilisateur les informations d'un achat et les retourne."""

        date = input("Date (YYYY-MM-DD) : ")
        name = input("Name : ")
        ticker = input("Ticker : ")
        quantity = float(input("Quantité : "))
        price = float(input(f"Prix (en {CURRENCY}) : "))
        fees = float(input(f"Fees (en {CURRENCY}) : "))

        return date, name, ticker, quantity, price, fees

    def ask_sell(self):
        """Demande à l'utilisateur les informations d'une vente et les retourne."""

        date = input("Date (YYYY-MM-DD) : ")
        name = input("Name : ")
        ticker = input("Ticker : ")
        quantity = float(input("Quantité : "))
        price = float(input(f"Prix (en {CURRENCY}) : "))
        fees = float(input(f"Prix (en {CURRENCY}) : "))

        return date, name, ticker, quantity, price, fees

    def display_situation(self, situation):
        """Affiche le portefeuille sous forme de dataframe et fournit d'autres informations."""

        rows = []

        for position in situation.positions:

            rows.append(
                {
                    "Ticker": position.ticker,
                    "Nom": position.name,
                    "Quantité": float(position.quantity),
                    "PRU": round(position.average_cost, DECIMALS),
                    "PnL réalisé": round(position.realized_pnl, DECIMALS)
                })

        dataframe = pd.DataFrame(rows)
        dataframe = dataframe.set_index("Ticker")

        print()
        print("-" * 55)
        print("Portefeuille :")
        print(dataframe)

        print()
        print(f"Positions: {situation.total_positions}")

        print(f"Montant investi: {round(situation.total_invested, 2)}{CURRENCY}")
        print("-" * 55)