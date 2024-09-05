import sys
import requests


def main():
    if len(sys.argv) == 2:
        try:
            qnt = float(sys.argv[1])
            print(f"${btcPrice(qnt):,.4f}")
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")


def btcPrice(num):
    try:
        result = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json").json()
        price = result["bpi"]["USD"]["rate_float"]
        return price * num
    except requests.RequestException:
        return None


if __name__ == "__main__":
    main()
