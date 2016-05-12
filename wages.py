def hoursinput(hours):
	while True:
		try:
			hours = float(hours)
			break
		except ValueError:
			print ("Please use a valid number")	

def wageinput(wage):
	while True:
		try:
			wage = float(wage)
			break
		except ValueError:
			print ("Please use a valid number")	

def OvertimePay(hoursinput):
	if hours > 20:
		OT = hours - 20
		TP = wage * 1.5
		OTpay = float(OT) * float(TP)
		hours = float(hours) - float(OT)
		pay = float(wage) * float(hours) + OTpay
		print(pay, " dollars total")

	else:
		pay = float(wage) * float(hours)
		print(pay, " dollars total")

def main()
	hours = input("enter your hours: ")
	hoursinput(hours)
	wage = input("enter your hourly wage: ")
	wageinput(wage)

main()


if _name_== "_main_":
	main()