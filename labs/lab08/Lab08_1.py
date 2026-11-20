# Starting file for LAB 8-1
# CS31 Course
# Carlos Farias
# Date 11/19/2026

#============================================
#        The Invoice program
#============================================

from decimal import Decimal 
from decimal import ROUND_HALF_UP

def get_discount_percent(order_total):
    if order_total <= 0:
        return Decimal("0")
    elif order_total < 100:
        return Decimal("0")
    elif order_total < 250:
        return Decimal("0.10")
    else:
        return Decimal("0.20")


def main():
    print("=" * 44)
    print("            The Invoice program")
    print("=" * 44)

    choice = "y"

    while choice == "y":
        # Get and round the order total.
        order_total = Decimal(input("Enter order total: "))
        order_total = order_total.quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        print()

        # Reject zero or negative totals before calculating an invoice.
        if order_total <= 0:
            print("Order total must be greater than zero.")
            print()
            continue

        # Determine the discount percentage.
        discount_percent = get_discount_percent(order_total)

        # Calculate the discount and subtotal.
        discount = (order_total * discount_percent).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        subtotal = order_total - discount

        # Calculate shipping on the discounted subtotal.
        shipping_percent = Decimal("0.085")
        shipping_cost = (subtotal * shipping_percent).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

        # Calculate sales tax on the discounted subtotal.
        tax_percent = Decimal("0.05")
        sales_tax = (subtotal * tax_percent).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

        invoice_total = subtotal + shipping_cost + sales_tax

        # Display each amount with a dollar sign and two decimal places.
        amounts = [
            ("Order total:", order_total),
            ("Discount amount:", discount),
            ("Subtotal:", subtotal),
            ("Shipping cost:", shipping_cost),
            ("Sales tax:", sales_tax),
            ("Invoice total:", invoice_total),
        ]

        for label, amount in amounts:
            formatted_amount = f"${amount:,.2f}"
            print(f"{label:<20}{formatted_amount:>12}")

        print()
        choice = input("Continue? (y/n): ").strip().lower()
        print()

    print("Bye!")


if __name__ == "__main__":
    main()