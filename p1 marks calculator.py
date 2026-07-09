while True:


 a=input("enter students name:-")
 b=int(input("enter marks of english:-"))
 c=int(input("enter marks of physical education:-"))
 d=int(input("enter marks of chemistry:-"))
 e=int(input("enter marks of maths:-"))
 f=int(input("enter marks of physics:-"))


 total=b+c+d+e+f
 percentage=(total/500)*100


 print("#"*70)
 print("     STUDENTS MARKS CALCULATION AND STREAM PREDICTION       ")
 print(f"TOTAL MARKS OBTAINED BY STUDENT ARE {total} out of 500 ")
 print("PERCENTAGE:-",percentage)
 if percentage<=60:
    print("low marks ,so you are not selected ")
 elif percentage<=70:
    print("you can get IT branch")
 elif percentage<=80:
    print("good marks ,so you are selected for core cs branch cs branch")
 elif percentage<=90:
    print("you are not selected for cs in AI ML ")
 else:
    ("invalid percentage")
 print()
 print("#"*70)





