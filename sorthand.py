# Arithmetic operators

weekly_allowance = 2000
spend = 400
found = 100
snacks = 250
print(f"my weekly allowance is {weekly_allowance}")
print("i spend 400 for book")
balance_ = float(weekly_allowance) - float(spend)
print(f"new balance is {balance_}")
print("i found 100 under my bed and added to my balance")
new_balance = float(balance_) + float(found)
print(f"my new balance turn {new_balance}")
print("i bought snacks worth 250")
new_balance_ = float(new_balance) - float(snacks)
print(f"my current balance is {new_balance_}")
print("i gave 25% of my balance to my sibling")
_new_balance_ = float(new_balance_) - float(362.5)
print("my balance is now {_new_balance_}")
new_Balance = _new_balance_ - 362.5 
print(f"my new balance is {new_Balance}")
split = new_Balance // 2
print(f"i split the balance into two now balance is {split}")
split %= 100
print(split)






