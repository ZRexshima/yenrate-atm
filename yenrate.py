# Goal - Program outputs the amount of yen to withdraw
# Given - ATM only dispenses 5_000 Yen notes
import sys

max_usd_withdrawal = 500
yen_bill = 5_000
yen_rate = 160


def main():
    converted = convert(max_usd_withdrawal)
    print(f"You can withdraw up to {converted:,} Yen")


def convert(dollars, rate):
    try:
        dollars = int(dollars)
    except:
       sys.exit("Please enter a number")

    return (dollars * rate) - ((dollars * rate) % yen_bill)


if __name__ == "__main__":
    main()
