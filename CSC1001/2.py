minutes=eval(input('Enter the number of minutes:'))#interact with users
all_days=minutes // (60*24)
years= all_days //365
days= all_days % 365 #calculate
print('That minutes will equal to',years, days)