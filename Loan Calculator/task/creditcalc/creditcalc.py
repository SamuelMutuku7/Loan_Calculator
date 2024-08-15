import math
import argparse


def calculate_annuity_payment(principal, periods, interest):
    nominal_interest = interest / (12 * 100)
    payment = math.ceil(principal * ((nominal_interest * (1 + nominal_interest) ** periods) /
                                     ((1 + nominal_interest) ** periods - 1)))
    return payment


def calculate_differentiated_payment(principal, periods, interest):
    nominal_interest = interest / 1200
    payments = []
    for month in range(1, periods + 1):
        current_month = month
        unique_payment = (principal / periods) + (
                nominal_interest * (principal - ((principal * (current_month - 1)) / periods)))
        raised_payment = math.ceil(unique_payment)
        payments.append(raised_payment)
    return payments


def calculate_periods(principal, payment, interest):
    nominal_interest = interest / 1200
    periods = math.ceil(math.log(payment / (payment - nominal_interest * principal)) / math.log(1 + nominal_interest))
    return periods


def calculate_principal(payment, periods, interest):
    nominal_interest = interest / (12 * 100)
    principal = payment / ((nominal_interest * (1 + nominal_interest) ** periods) /
                           ((1 + nominal_interest) ** periods - 1))
    return round(principal)


def main():
    parser = argparse.ArgumentParser(description='Credit Calculator')
    parser.add_argument('--type', type=str, help='Type of payment: "annuity" or "diff" (differentiated)')
    parser.add_argument('--principal', type=float, help='Credit principal')
    parser.add_argument('--payment', type=float, help='Monthly payment')
    parser.add_argument('--periods', type=int, help='Number of periods (months)')
    parser.add_argument('--interest', type=float, help='Annual interest rate (as a percentage)')

    args = parser.parse_args()

    # Validate the Parsed Arguments
    if args.type is None:
        print("Incorrect parameters")
        return
    elif args.type not in ["annuity", "diff"]:
        print("Incorrect parameters")
        return
    elif args.type == "diff" and args.payment is not None:
        print("Incorrect parameters")
        return
    elif args.type == "diff" and (args.principal is None or args.periods is None):
        print("Incorrect parameters")
        return
    elif args.type == "annuity" and args.principal is None and args.periods is None and args.payment is None:
        print("Incorrect parameters")
        return
    elif args.interest is None or args.interest <= 0:
        print("Incorrect parameters")
        return
    elif any(param is not None and param <= 0 for param in [args.principal, args.payment, args.periods]):
        print("Incorrect parameters")
        return



    # Handle the Different Outputs for all the Scenarios
    if args.type == "diff":
        payments_list = calculate_differentiated_payment(args.principal, args.periods, args.interest)
        for index, value in enumerate(payments_list):
            print(f"Month {index + 1}: payment is {value}")
        overpayment = sum(payments_list) - args.principal
        print(f"Overpayment = {overpayment}")
        return
    elif args.type == "annuity":
        if args.principal is not None and args.periods is not None:
            annuity_payment = calculate_annuity_payment(args.principal, args.periods, args.interest)
            overpayment = (annuity_payment * args.periods) - args.principal
            print(f"Your annuity payment = {annuity_payment}!")
            print(f"Overpayment = {overpayment}")
            return
        elif args.principal is not None and args.payment is not None:
            periods = calculate_periods(args.principal, args.payment, args.interest)
            overpayment = (args.payment * periods) - args.principal
            years = periods // 12
            months = periods % 12
            if periods < 12:
                print(f"It will take {periods} months to repay this loan!")
            elif periods == 12:
                print(f"It will take 1 year to repay this loan!")
            else:
                if months == 0:
                    print(f"It will take {years} years to repay this loan!")
                else:
                    print(f"It will take {years} years and {months} months to repay this loan!")
            print(f"Overpayment = {overpayment}")
            return
        elif args.payment is not None and args.periods is not None:
            principal = calculate_principal(args.payment, args.periods, args.interest)
            overpayment = (args.payment * args.periods) - principal
            print(f"Your loan principal = {principal}!")
            print(f"Overpayment = {overpayment}")
            return


if __name__ == "__main__":
    main()