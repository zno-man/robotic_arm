
def configure():
	print("Enter loc 1 cordinates:",end = '')
	t1 = list(map(float , input().strip().split()))
	print("Enter loc 2 cordinates:",end = '')
	t2 = list(map(float , input().strip().split()))
	print("Enter loc 3 cordinates:",end = '')
	t3 = list(map(float , input().strip().split()))
	print(t1,t2,t3)

while(True):
	print("""
    main menu
    ---------
      
        1) config
        2) goto l1
        3) goto l2
        4) goto l3
        5) exit
              """)
	print(":",end = "")
        
	inp = input()
	if inp == "1":
		configure()
	elif inp == "2":
		a = 1
	elif inp == "3":
		a = 1
	elif inp == "4":
		a = 1
	elif inp == "5":
		break

print("exiting menu...")
