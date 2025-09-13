# Format large numbers with underscores for better readability

billion:int = 1_000_000_000
print(billion)

my_number = 1_000_000
print(f"{my_number:,}")

#1,000,000

print(f"{my_number=}")
#my_number=1000000

pi = 3.14159_26535_89793
places:int = 3
print(f"{pi:.{places}f}")
print(f"{pi:.2f}")

#No error if the key does not exist

users: dict[int,str] = {0:'Bob', 1:'Alice'}

print(users.get(2, 'Not found'))
