#!/usr/bin/env python3
import random


def lotto_ziehung():
   """
      do lotto Ziehung ;-)

      @parameters: nothing
      @returns: liste with lotto numbers
   """
   lottoz = []   
   random.seed() 
   while len(lottoz) < 6: 
       lz = random.randint(1,49)
       if lz not in lottoz:
         lottoz.append(lz)
   lottoz.sort(key=int)    
   return(lottoz)    

def tipp_eingabe_check(lotto_eingabe):
   """
      Check Numbers if they are valid

      @parameters: list of lotto number
      @returns: boolean 
   """
   if(len(lotto_eingabe) > 6 ):
      return(False)
   elif len(set(lotto_eingabe)) != len(lotto_eingabe):
      return(False)
   

   for lotto_tipp_single in lotto_eingabe:
      if lotto_tipp_single in range (1,50):
         return(True)
      else:
         return(False)     

def tipp_auswertung(tipp, ziehung):
    """
      looks for common numbers in 2 list with lotto numbers 

      @parameters: 2 list of lotto number
      @returns: integer
    """
    s1 = set(tipp)
    s2 = set(ziehung)
    return(len(s1.intersection(s2)))

    #found = []
    #for was_found in s3:
     #  found.append(match)





if __name__ == "__main__":
   eing = [7, 16, 23, 33,  44, 49 ] 
   
   if tipp_eingabe_check(eing) == True:
      lz = lotto_ziehung()
      print ("Ihre Zahlen: " + str(eing))
      print ("Gezogen    : " + str(lz))
      print (f"{tipp_auswertung(eing,lz)} Zahlen stimmen ueberein")
   else:
      print ("lottozahlen check fehlgeschlagen")   
  

    

