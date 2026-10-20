# Staff Salary Calculator (Python)

A menu-driven command-line program for managing staff records and generating payslips with tax and National Insurance deductions.

> University coursework: *Computer Science Fundamentals*, BSc (Hons) Computing at Regent College London.

## Features

1. Add staff (name, hourly rate, hours worked), with input validation
2. View all staff
3. Search for a staff member and print their payslip
4. Delete staff
5. Compare the net pay of two staff members

## Example payslip

```
------ PAYSLIP ------
Name: Sam
Hours Worked: 160.0
Hourly Rate: £12.50
Gross Pay: £2000.00
Tax Deducted: £0.00
NI Deduction: £200.00
Net Pay: £1800.00
----------------------
```

## How to run

Requires Python 3 and no extra libraries.

```bash
python3 salary_management.py
```

## Concepts used

Functions · lists and dictionaries · loops and conditionals · `try/except` input validation · formatted output

## Possible improvements

- The tax model is simplified: it compares one period's pay with the annual £12,570 Personal Allowance. A real payroll would spread the allowance across pay periods and use the tax bands.
- Save staff records to a CSV file
- Add unit tests for `calculate_net_salary()`

## Author

**Gabriel Malini Rodrigues** · [LinkedIn](https://www.linkedin.com/in/gabriel-malini)
