def main():
    # Input gathering
    name = input("Enter Employee Name: ")
    emp_type = int(input("Enter Employee Type (1 for Private, 2 for Government): "))
    gross_salary = float(input("Enter Monthly Gross Salary: "))

    # 1. SSS (Private) or GSIS (Government) Calculation
    if emp_type == 1:
        # SSS Employee Share: 4.5% capped at ₱1,350.00
        sss_gsis = min(gross_salary * 0.045, 1350.0)
    else:
        # GSIS Employee Share: 9.0%
        sss_gsis = gross_salary * 0.09

    # 2. Pag-IBIG Contribution (2% capped at ₱200.00)
    pag_ibig = min(gross_salary * 0.02, 200.0)

    # 3. PhilHealth Contribution (2.5% employee share)
    phil_health = gross_salary * 0.025

    # Taxable Income Calculation
    taxable_income = gross_salary - (sss_gsis + pag_ibig + phil_health)

    # 4. BIR Withholding Tax (TRAIN Law Monthly Schedule)
    bir_tax = 0.0
    if taxable_income > 83333:
        bir_tax = 11875 + (taxable_income - 83333) * 0.25
    elif taxable_income > 33333:
        bir_tax = 1875 + (taxable_income - 33333) * 0.20
    elif taxable_income > 20833:
        bir_tax = (taxable_income - 20833) * 0.15

    # Final Totals
    total_deductions = sss_gsis + pag_ibig + phil_health + bir_tax
    net_pay = gross_salary - total_deductions

    # Output Display
    print("\n----------------------------------------")
    print(f"PAYROLL SUMMARY FOR: {name}")
    print(f"Employee Type: {'Private' if emp_type == 1 else 'Government'}")
    print(f"Gross Salary: PHP {gross_salary:.2f}")
    print("----------------------------------------")
    print(f"{'SSS' if emp_type == 1 else 'GSIS'} Contribution: PHP {sss_gsis:.2f}")
    print(f"Pag-IBIG Contribution: PHP {pag_ibig:.2f}")
    print(f"PhilHealth Contribution: PHP {phil_health:.2f}")
    print(f"BIR Withholding Tax: PHP {bir_tax:.2f}")
    print("----------------------------------------")
    print(f"Total Deductions: PHP {total_deductions:.2f}")
    print(f"Net Monthly Pay: PHP {net_pay:.2f}")
    print("----------------------------------------")

if __name__ == "__main__":
    main()