
def driver_age_check():
  age= int(input("how old are you"))
  if age>18:
    print("Powering ON.")
  elif age == 18:
    print("Powering on. Enjoy the first year of driving.")
  else:
     print("Powering Off. You are to young")

driver_age_check()