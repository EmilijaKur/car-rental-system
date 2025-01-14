1
from datetime import datetime, date
def list_cars():
    file=open("vehicles.txt", 'r')
    print("The following cars are available:")
    lines=file.readlines()
    file.close()
    data=[]
    reg_num_list=[]
    for line in lines:
        row=line.strip().split(',')
        data.append(row)
    for i in range(len(data)):
        reg_nr=data[i][0]
        model=data[i][1]
        price=data[i][2]
        properties=[]
        for j in range(3, len(data[i])):
                properties.append(data[i][j].strip())
        properties_str=""
        for k in range(len(properties)):
            properties_str=properties_str+properties[k]
            if k<len(properties)-k:
                properties_str=properties_str+", "
        print(f"* Reg nr: {reg_nr}, Model: {model}, Price per day:{price}\nProperties: {properties_str}")
        reg_num_list.append(reg_nr)
    print("")
    
    
def rent():
    filer=open("vehicles.txt", 'r')
    lines=filer.readlines()
    filer.close()
    data=[]
    reg_num_list=[]
    for line in lines:
        row=line.strip().split(',')
        data.append(row)
    for i in range(len(data)):
        reg_nr=data[i][0]
        reg_num_list.append(reg_nr)
##    print(reg_num_list)
    file=open("rentedVehicles.txt", 'r')
    lines=file.readlines()
    file.close()
    data=[]
    for line in lines:
        row=line.strip().split(',')
        data.append(row)
    rented_regnr=[]
    for i in range(len(data)):
        reg_nr=data[i][0]
        rented_regnr.append(reg_nr)
##    print(rented_regnr)
    filecust=open("customers.txt", 'r')
    customers=filecust.readlines()
    filecust.close()
    allcust=[]
    for customer in customers:
        customer1=customer.strip().split(',')
        allcust.append(customer1)
    custbirthdays=[]
    custname=[]
    for i in range(len(allcust)):
        if len(allcust[i])>=2:
            cust1birthday=allcust[i][0]
            custbirthdays.append(cust1birthday)
            cust1name=allcust[i][1]
            custname.append(cust1name)
##    print(custbirthdays)
##    print(custname)        
    given_regnr=input("Give the register number of the car you want to rent:\n")
    check=0
    returningcustomer=0
    if given_regnr in reg_num_list and given_regnr not in rented_regnr:
        while True:
            birthday=input("Please enter your birthday in the form DD/MM/YYYY:\n")
            try:
                
                birthday_date=datetime.strptime(birthday, "%d/%m/%Y")
                break
            except:
                print("There is not such date. Try again!")
        
        today=date.today()
        age = today.year - birthday_date.year
        if today.month<birthday_date.month or (today.month==birthday_date.month and today.day<birthday_date.day):
            age=age-1
        if age<18:
            print("You are too young to rent a car, sorry!")
            print("")
        elif age>75:
            print("You are too old to rent a car, sorry!")
            print("")
        else:
            print("Age OK")
            for j in range(len(custbirthdays)):
                if birthday==custbirthdays[j]:
                    print(f"Hello {custname[j]}")
                    print(f"You rented the car {given_regnr}")
                    print("")
                    returningcustomer=1
                
            while True and returningcustomer==0:
                print("Names contain only letters and start with capital letters.")
                fname=input("Enter the first name of the customer:\n")
                lname=input("Enter the last name of the customer:\n")
                if ('A'<=fname[0]<='Z') and ('A'<=lname[0]<='Z'):
                    valid_fname=True
                    for char in fname[1:]:
                        if not ('a' <= char <= 'z'):
                            valid_fname = False
                    valid_lname = True
                    for char in lname[1:]:
                        if not ('a' <= char <= 'z'):
                            valid_lname = False
                    if valid_fname and valid_lname:
                        break
                    else:
                        continue            
            
            while True and returningcustomer==0:
                email=input("Give your email:\n")
                check_at=False
                check_dot=False
                for i in range(len(email)):
                    if email[i]=='@':
                        check_at=True
                    elif email[i]=='.' and check_at==True:
                        check_dot=True
                if check_at==True and check_dot==True:
                    print(f"Hello {fname}")
                    print(f"You rented the car {given_regnr}")
                    print("")
                    break
                else:
                    print("Give a valid email address")
                    continue
            customfile=open("customers.txt", 'a')
            if returningcustomer==0:
                customfile.write(f"{birthday},{fname},{lname},{email}\n")        
            customfile.close()
            rentedcars=open("rentedVehicles.txt", 'a')
            rentedcars.write(f"{given_regnr},{birthday},{today.day}/{today.month}/{today.year} {datetime.now().hour}:{datetime.now().minute}\n")
            rentedcars.close()
    elif given_regnr in rented_regnr:
        print(f"{given_regnr} already rented")
        print("")
    else:
        print("Car does not exist")
        print("")
           
def return_car():
    file=open("rentedVehicles.txt", 'r')
    lines=file.readlines()
    file.close()
    data=[]
    for line in lines:
        row=line.strip().split(',')
        data.append(row)
    rented_regnr=[]
    dates_list=[]
##    print(data)
    for i in range(len(data)):
        if len(data[i])>=3:
            reg_nr=data[i][0]
            rented_regnr.append(reg_nr)
            renteddate=data[i][2]
            dates_list.append(renteddate)
##    print(rented_regnr, dates_list)
    file=open("vehicles.txt", 'r')
    cars=file.readlines()
    file.close()
    cardata=[]
    reg_num_list=[]
    price_list=[]
    birthday=""
    for car in cars:
        row=car.strip().split(',')
        cardata.append(row)
    for i in range(len(cardata)):
        reg_nr=cardata[i][0]
        price=cardata[i][2]
        reg_num_list.append(reg_nr)
        price_list.append(price)
##    print(reg_num_list, price_list)
    return_car=input("Give the register number of the car you want to return:\n")
    if return_car in rented_regnr:
        now=datetime.now()
        formatteddate=now.strftime("%d/%m/%Y %H:%M")
        for i in range(len(rented_regnr)):
            if return_car==rented_regnr[i]:
                rent_date=datetime.strptime(dates_list[i],"%d/%m/%Y %H:%M")
                difference=(now-rent_date).days+1
                price_per_day=0
                for j in range(len(reg_num_list)):
                    if rented_regnr[i]==reg_num_list[j]:
                        price_per_day=int(price_list[j])
                print(f"The rent lasted {difference} days and the cost is {difference*price_per_day:.2f} euros")
                print("")
                birthday=data[i][1]
                formattedrentdate=rent_date.strftime("%d/%m/%Y %H:%M")
                data.remove(data[i])                
##        print(data)        
        newrentfile=open("rentedVehicles.txt", 'w')
        for line in data:
            line_str=""
            for i in range(len(line)):
                if i!=len(line)-1:
                    line_str=line_str+str(line[i])+","
                else:
                    line_str=line_str+str(line[i])
            newrentfile.write(line_str+"\n")
        newrentfile.close()
        transactions=open("transActions.txt", "a")
        transactions.write(f"{return_car},{birthday},{formattedrentdate},{formatteddate},{difference},{difference*price_per_day:.2f}")
        transactions.close()
        
    elif return_car not in rented_regnr and return_car in reg_num_list:
        print("Car is not rented")
        print("")
    else:
        print("Car does not exist")
        print("")
def count_sum():
    file=open("transActions.txt", 'r')
    lines=file.readlines()
    file.close()
    data=[]
    for line in lines:
        row=line.strip().split(',')
        data.append(row)
    money=[]
    for i in range(len(data)):
        amount=data[i][5]
        money.append(float(amount))
    total_sum=0
    for i in range(len(money)):
        total_sum=total_sum+money[i]
    print(f"The total amount of money is {total_sum:.2f} euros")
    print("")

def main():
    while True:
        print("""You may select one of the following:
1) List available cars
2) Rent a car
3) Return a car
4) Count the money
0) Exit """)
        choice=input("What is your selection?\n")
        if choice=="1":
            list_cars()
        elif choice=="2":   
            rent()      
        elif choice=="3":
            return_car()
        elif choice=="4":
            count_sum()
        elif choice=="0":
            print("Bye!")
            break            
        else:
            print("")
            continue
    
main()
