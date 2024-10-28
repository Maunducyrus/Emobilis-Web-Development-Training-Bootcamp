# if.....elif...if

# votes = 0
# if votes > 10000:
#     print("You've been voted in")
# else:
#     print("You've not voted in")
#
#     marks = 1
#     if marks > 80 and marks <= 100:
#         print("Grade A")
#     elif marks>70 and marks <= 80:
#         print("Grade B")
#     elif marks>60 and marks <= 70:
#         print("Grade C")
#     elif marks>50 and marks <= 60:
#         print("Grade D")
#     elif marks>40 and marks <= 50:
#         print("Grade E")
#     elif marks > 0:
#         print("You have failed")
#     else:
#         print("Enter a value between 0 and 100")

withdrawal_amount = float(input("Enter your withdrawal amount: "))

additional_amount = 0

if withdrawal_amount > 10000:
    additional_amount = withdrawal_amount * 0.1

elif withdrawal_amount > 5000:
    additional_amount = withdrawal_amount * 0.05

    # total amount to be given out
    total_amount = withdrawal_amount + additional_amount

    # Displaying total amount
    print("Total amount given out is ", total_amount)




