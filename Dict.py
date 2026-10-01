countrydb={}
while True:
  print("1 Insert")
  print("2 Display all countries")
  print("3 Display all Capitals")
  print("4 Get Capital")
  print("5 Delete")
  choice=int(input("Enter your choice from 1-5"))
  if choice == 1:
    country=input("Enter a country's name").upper()
    capital=input("Enter the country's Capital").upper()
    countrydb[country]=capital
    print(countrydb)
  elif choice == 2:
    print(list(countrydb.keys()))
  elif choice == 3:
    print(list(countrydb.values()))
  elif choice == 4:
    country=input("Enter the capital  name")
    print(countrydb.get(country)) 
  elif choice == 5:
    country=input("Enter the country name").upper()
    print(countrydb)
    del countrydb[country]
