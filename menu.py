
def configure():
	print("Enter loc 1 cordinates:",end = '')
	lo1 = list(map(float , input().strip().split()))
	print("Enter loc 2 cordinates:",end = '')
	lo2 = list(map(float , input().strip().split()))
	print("Enter loc 3 cordinates:",end = '')
	lo3 = list(map(float , input().strip().split()))
	print(lo1,lo2,lo3)
	return lo1,lo2,lo3


lo1 = [0,0,0]
lo2 = [0,0,0]
lo3 = [0,0,0]

while(True):
	print("""
    main menu
    ---------
      
        1) config
        2) goto l1
        3) goto l2
        4) goto l3
        5) pick up
        6) collect
        7) deposit
        8) adjust angles
        9) exit
              """)
	print(":",end = "")
        
	inp = input()
	if inp == "1":
		lo1,lo2,lo3 = configure()
	elif inp == "2":
		pass
	elif inp == "3":
		pass
	elif inp == "4":
		pass
	elif inp == "5":
		pass
	elif inp == "6":
		pass
	elif inp == "7":
		pass
	elif inp == "8":
		pass
	elif inp == "9":
		break

print("exiting menu...")
