"""
Personal Finance Calculator
Student: [Your Name]
Date: [Today's Date]
Purpose: Calculate monthly budget and savings
"""
monthly_income = float(input("Enter your monthly income in THB: ")) #รับค่ารายต่อได้ต่อเดือน
rent_cost = float(input("Enter your Monthly rent/housing cost: ")) #รับค่าค่าเช่าต่อเดือน
food_budget = int(input("Enter your Monthly food budget in THB: ")) #รับค่ากินต่อเดือน
transportation_cost =float(input("Enter your Monthly transportation expenses: ")) #รับค่าเดินทางต่อเดือน
entertainment_budget = int(input("Enter your Monthly entertainment budget: ")) #รับค่าค่าเที่ยวต่อเดือน
emergency_fund_percent = float(input("Enter your Percentage to save for emergency: ")) #รับค่าเปอร์เซ็นต์ที่ต้องการสำรองเงิน
investment_percent = float(input("Enter your Percentage to invest: ")) #รับค่าเปอร์เซ็นต์ที่ต้องการลงทุน

total_fixed_expenses = rent_cost + transportation_cost 
total_variable_expenses = food_budget + entertainment_budget 
total_expenses = total_fixed_expenses + total_variable_expenses #คำนวณค่าใช้จ่ายทั้งหมด
remaining_income = monthly_income - total_expenses  #คำนวณเงินคงเหลือ
emergency_fund_amount = monthly_income * (emergency_fund_percent / 100) #คำนวณเงินสำรอง
investment_amount = monthly_income * (investment_percent / 100) #คำนวณเงินลงทุน
available_for_savings = remaining_income - emergency_fund_amount - investment_amount #คำนวณเงินสำหรับออม
expense_ratio = (total_expenses / monthly_income) * 100 #คำนวณเปอร์เซ็นต์ค่าใช้จ่ายเทียบกับรายได้ทั้งหมด

#แสดงผลค่าใช้จ่ายและเงินคงเหลือ
print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {total_fixed_expenses:.2f} THB")
print(f"Variable Expenses: {total_variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")
#แสดงผลเงินสำรอง เงินออม เงินลงทุน
print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent:.0f}%): {emergency_fund_amount:.2f} THB")
print(f"Investment ({investment_percent:.0f}%): {investment_amount:.2f} THB")
print(f"Available for Savings: {available_for_savings:.2f} THB")

#แสดงผลสัดเปอร์เซ็นต์ค่าใช้จ่ายเทียบกับรายได้ทั้งหมด
print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")