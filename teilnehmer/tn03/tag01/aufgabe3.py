#!/usr/bin/env python3

"""This script will convert temperature between C, F and K """

units =  ["C", "K", "F"]

while True:
   grad = input("Gradzahl:")
   if grad == "stop":
     exit()
   # using float() 
   # Check for float string 
   try :  
      float(grad) 
      break
   except : 
      print("Gradzahl ist keine Floating Point Zahl -  nochmal versuchen oder 'stop'") 
    


while True:
   einheit_in = input("Eingabe Einheit:")
   if einheit_in == "stop":
     exit()
   elif einheit_in not in units:
      print(f"Einheit muss C, F oder K sein - nochmal versuchen oder 'stop' für ende")
   elif float(grad) < 0 and   einheit_in =="K":
      print(f"Einheit K is nicht möglich mit negativen Werten")  
   elif float(grad) < -273.15 and   einheit_in =="C":
         print(f"Einheit C erlaubt keine Werte < -273.15")  
   elif float(grad) < ((-273.15 * 1.800) + 32)  and   einheit_in =="C":
         print(f"Einheit F erlaubt keine Werte < { (-273.15 * 1.800) + 32}")  
      
   else:
      break
   

while True:
   einheit_out = input("Ausgabe Einheit:")
   if einheit_in == "stop":
     exit()
   if einheit_out not in units:
     print(f"Einheit muss C, F oder K sein - nochmal versuchen oder 'stop' für ende")
   else:
      break  
   
if einheit_in == einheit_out:
   print("Das war einfach ;-)")
   print(f"{grad} {einheit_in} sind {grad} {einheit_out}")   

grad_in = float(grad)
if einheit_in == "F":
    if einheit_out == "C":
       grad_out = (grad_in - 32) / 1.800
    if einheit_out == "K":
       grad_out= ((grad_in - 32) / 1.800) + 273.15


if einheit_in == "C":
    if einheit_out == "F":
       grad_out = (grad_in * 1.800 + 32)
    if einheit_out == "K":
       grad_out = (grad_in  - 273.15)

if einheit_in == "K":
    if einheit_out == "C":
      grad_out = (grad_in + 273.15)
    if einheit_out == "F":
       grad_out = ((grad_in  + 273.15) * 1.8) + 32

print(f"{grad_in} {einheit_in} = {grad_out} {einheit_out}")


