#Modules used in Program(Hotel Management System)
import pickle
import random
import datetime


back=('Y')
while(back=='Y'):
    #Structure of Main Menu
    print('','',"THE SAVOY",sep='\t')
    print('',''," WELCOME",sep='\t')
    print('','',"MAIN MENU",sep='\t')
    print("1. ROOM FILE")
    print("2. CUSTOMER FILE")
    print("3. BILL GENERATION")
    print("4. REPORT FILE")
    print("5. SEARCH BY NAME")
    print("6. QUIT")
    print()




    choice1=eval(input("Enter your choice from the above list: "))
    
    if(choice1==1):
        bck=("Y")
        while(bck=='Y'):
            #Structure of Room File Menu
            print()
            print('','',"THE SAVOY",sep='\t')
            print('','',"ROOM FILE",sep='\t')
            print('','',"   MENU",sep='\t')
            print("1. ADDITION OF A RECORD")
            print("2. MODIFICATION OF A RECORD")
            print("3. REMOVAL OF A RECORD")
            print("4. BACK TO MAIN MENU")
            print("5. QUIT")
            print()
            
            
            choice2=str(input("Enter your choice from the above list: "))

            if(choice2=='1'):
                again=('Y')
                while(again=='Y'):
                    #Structure of Addition Of Record in Room File 
                    print()
                    print('','',"THE SAVOY",sep='\t')
                    print('','',"ROOM FILE",sep='\t')
                    print('',"   ADDITION OF A RECORD",sep='\t')
                    
                    #To check whether the room exists
                    rno=str(input("1. Room No.: "))
                    f=open("Room.dat","rb")
                    vl=[]
                    try:
                        while True:
                            d1=pickle.load(f)
                            vl.append(d1)
                    except EOFError:
                        pass
                    f.close()
                    vl2=[]
                    for c in vl:
                        vl2=vl2+c
                    v=rno in vl2
                    
                    while(v==True):
                        print('NOTE: Room Number Already Exist')
                        rno=str(input("1. Room No.: "))
                        v=rno in vl2

                    #To assign floor no. as per room no.
                    v=len(rno)
                    if(v==3):
                        flr=rno[0]
                        print("2. Floor No.: ",rno[0],sep='')
                    elif(v==4):
                        flr=rno[0]+rno[1]
                        print("2. Floor No.: ",rno[0],rno[1],sep='')

                    #Taking other informations about room
                    typ=str(input("3. Single/Double: "))
                    cond=str(input("4. Regular/Luxury/Super Luxury: "))
                    serv=str(input("5. AC/Without AC: "))
                    view=str(input("6. Mountains/Park/Lake: "))
                    chrg=str(input("7. Charges Per Day(IN RUPEES): "))
                    status='A'
                    print("status: ",status)
                    f=open("Room.dat",'ab+')
                    
                    #Code to add records in Room File
                    list1=[rno,flr,typ,cond,serv,view,chrg,status]
                    pickle.dump(list1,f)
                    f.close()

                    print()
                    print("Record added successfully to the room file")
                    print()

                    #asking to add another record or other repeating functions
                    again=str(input("Add another record(Yes/No): "))
                    again=again.upper()
                    if(again=='Y'):
                        pass
                    else:
                        bck=str(input("Back to room file menu(Yes/No): "))
                        bck=bck.upper()
                        if(bck=='Y'):
                            pass
                        else:
                            back=str(input("Back to main menu(Yes/No): "))
                            back=back.upper()
                            if(back=='Y'):
                                pass
                            else:
                                quit()

            elif(choice2=="2"):
                again=('Y')
                while(again=='Y'):
                    #Structure of Modification Of Record in Room File 
                    print()
                    print('','',"THE SAVOY",sep='\t')
                    print('','',"ROOM FILE",sep='\t')
                    print('',"MODIFICATION OF A RECORD",sep='\t')
                    rno=str(input("Enter the number of room whose data has to be modified: "))

                    #Code to display old records from Room File and to load data from room file into a list
                    f=open("Room.dat",'rb+')
                    vl=[]
                    try:
                        while True:
                            d1=pickle.load(f)
                            if (d1[0]==rno):
                                print("1. Room No.: ",d1[0])
                                print("2. Floor No.: ",d1[1])
                                print("3. Single/Double: ",d1[2])
                                print("4. Regular/Luxury/Super Luxury: ",d1[3])
                                print("5. AC/Without AC: ",d1[4])
                                print("6. Mountains/Park/Lake: ",d1[5])
                                print("7. Charges Per Day(IN RUPEES): ",d1[6])
                                print("8. Available/Under Maintainence: ",d1[7])
                                
                                #To check whether the room is vacant
                                upd1=eval(input("Enter 3 to 8 To Update Records: "))
                                if(d1[7]=="B"):
                                    print("Can't Modify Room While Customer Is Using It")
                                    vl.append(d1)
                                else:
                                    if(upd1==1):
                                        print("Can't Modify Room Number")
                                    elif(upd1==2):
                                        print("Can't Modify Floor Number")
                                    elif(upd1==8):
                                        new_value=str(input("Enter New Value: "))
                                        if(new_value=='B'):
                                            
                                            #To restrict status of room as booked
                                            print("Can't Modify Status Of Room As Booked")
                                        else:
                                            d1[(upd1-1)]=new_value
                                    else:
                                        #Code to display new records from Room File
                                        
                                        d1[(upd1-1)]=str(input("Enter New Value: "))
                                        print()
                                        print("Record modified successfully in the room file")
                                        print()
                                        print("1. Room No.: ",d1[0])
                                        print("2. Floor No.: ",d1[1])
                                        print("3. Single/Double: ",d1[2])
                                        print("4. Regular/Luxury/Super Luxury: ",d1[3])
                                        print("5. AC/Without AC: ",d1[4])
                                        print("6. Mountains/Park/Lake: ",d1[5])
                                        print("7. Charges Per Day(IN RUPEES): ",d1[6])
                                        print("8. Booked/Available/Under Maintainence: ",d1[7])
                                    vl.append(d1)
                            else:
                                vl.append(d1)
                    except EOFError:
                        pass
                    f.close()

                    #Code to modify records in Room File
                    f=open("Room.dat",'wb')
                    for c in vl:
                        pickle.dump(c,f)
                    f.close()

                    print()

                    #asking to modify another record or other repeating functions
                    again=str(input("Modify another record(Yes/No): "))
                    again=again.upper()
                    if(again=='Y'):
                        pass
                    else:
                        bck=str(input("Back to room file menu(Yes/No): "))
                        bck=bck.upper()
                        if(bck=='Y'):
                            pass
                        else:
                            back=str(input("Back to main menu(Yes/No): "))
                            back=back.upper()
                            if(back=='Y'):
                                pass
                            else:
                                quit()

            elif(choice2=='3'):
                again=('Y')
                while(again=='Y'):
                    #Structure of Removal Of Record from Room File 
                    print()
                    print('','',"THE SAVOY",sep='\t')
                    print('','',"ROOM FILE",sep='\t')
                    print('',"REMOVAL OF A RECORD",sep='\t')
                    rno=str(input("Enter the number of room whose data has to be removed: "))

                    #To load data from room file into a list
                    f=open("Room.dat",'rb+')
                    vl=[]
                    try:
                        while True:
                            d1=pickle.load(f)
                            if (d1[0]==rno):
                                pass                            
                            else:
                                vl.append(d1)
                    except EOFError:
                        pass
                    f.close()

                    #Code to modify records in Room File
                    f=open("Room.dat",'wb')
                    for c in vl:
                        pickle.dump(c,f)
                    f.close()

                    print()
                    print("Record removed successfully from the room file")
                    print()

                    #asking to delete another record or other repeating functions
                    again=str(input("Delete another record(Yes/No): "))
                    again=again.upper()
                    if(again=='Y'):
                        pass
                    else:
                        bck=str(input("Back to room file menu(Yes/No): "))
                        bck=bck.upper()
                        if(bck=='Y'):
                            pass
                        else:
                            back=str(input("Back to main menu(Yes/No): "))
                            back=back.upper()
                            if(back=='Y'):
                                pass
                            else:
                                quit()

            elif(choice2=="4"):
                break
            else:
                quit()
    elif(choice1==2):
        bck=("Y")
        while(bck=='Y'):
            #Structure of Customer File Menu
            print()
            print('','',"THE SAVOY",sep='\t')
            print('',"      CUSTOMER FILE",sep='\t')
            print('','',"   MENU",sep='\t')
            print("1. BOOKING OF ROOM")
            print("2. MODIFICATION OF A RECORD")
            print("3. REMOVAL OF A RECORD")
            print("4. BACK TO MAIN MENU")
            print("5. QUIT")

            choice2=str(input("Enter your choice from the above list: "))

            if(choice2=='1'):
                again=('Y')
                while(again=='Y'):
                    #Structure of Booking Of Room in Hotel and entry of data in Customer File
                    print()
                    print('','',"THE SAVOY",sep='\t')
                    print('',"      CUSTOMER FILE",sep='\t')
                    print('',"     BOOKING OF ROOM",sep='\t')

                    #Code to generate a unique id for each entry of customer
                    csno1=str(random.randint(1000,9999))
                    lst1=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                    lst2=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                    lst3=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                    lst=lst1+lst2+lst3
                    csno2=str(random.randint(10,99))
                    csno3=str(random.randint(0,9))
                    csno=csno1+lst+csno2+lst1+csno3
                    
                    f=open("Customer.dat","rb")
                    vl=[]
                    try:
                        while True:
                            d1=pickle.load(f)
                            vl.append(d1)
                    except EOFError:
                        pass
                    f.close()
                    vl2=[]
                    for c in vl:
                        vl2=vl2+c
                    v=csno in vl2
                    
                    while(v==True):
                        csno1=str(random.randint(1000,9999))
                        lst1=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                        lst2=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                        lst3=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                        lst=lst1+lst2+lst3
                        csno2=str(random.randint(10,99))
                        csno3=str(random.randint(0,9))
                        csno=csno1+lst+csno2+lst1+csno3
                        v=csno in vl2
                        
                    print("1. Customer No.: ",csno,sep='')

                    #Taking other informations from customer
                    cnam=str(input("2. Customer Name: "))
                    cno=str(input("3. Contact No.: "))
                    adrs=str(input("4. Address: "))
                    cid=str(input("5. Check In Date: "))
                    day,month,year=map(int,cid.split('-'))
                    cid=datetime.date(year,month,day)

                    cod=str(input("6. Check Out Date: "))
                    day,month,year=map(int,cod.split('-'))
                    cod=datetime.date(year,month,day)
                    
                    nod=(cod-cid).days
                    print('7. No. Of Days: ',nod,sep='')

                    #Code to take preference of room from customer and to check whether the room is available
                    agn='Y'
                    while(agn=='Y'):
                        print()
                        print('','',"THE SAVOY",sep='\t')
                        print('',"      CUSTOMER FILE",sep='\t')
                        print('',"     BOOKING OF ROOM",sep='\t')
                        print("Please Select The Feautures Of The Room:")
                        flr=str(input("1. Floor No.: "))
                        typ=str(input("2. Single/Double: "))
                        cond=str(input("3. Regular/Luxury/Super Luxury: "))
                        serv=str(input("4. AC/Without AC: "))
                        view=str(input("5. Mountains/Park/Lake: "))
                        f=open("Room.dat",'rb')
                        try:
                            while True:
                                d1=pickle.load(f)
                                if(d1[1]==flr and d1[2]==typ and d1[3]==cond and d1[4]==serv and d1[5]==view and d1[7]=='A'):
                                    print()
                                    print("Room No.: ",d1[0])
                                    print("Charges Per Day(IN RUPEES): ",d1[6])
                                    rr=int(d1[6])
                                    print("Total(IN RUPEES): ",nod*int(d1[6]))
                                    print()
                                    cont=str(input("Do You Want To Proceed: "))
                                    cont=cont.upper()
                                    if(cont=='Y'):
                                        rno=d1[0]
                                        agn='N'
                                        break
                                    else:
                                        agn=str(input("Want To Look For Rooms With Other Features?(Yes/No): "))
                                        if(agn=='Y'):
                                            break
                                        else:
                                            quit()
                                else:
                                    agn='NY'
                                    pass
                        except EOFError:
                            pass
                        f.close()
                        if(agn=='NY'):
                            print("No Rooms Are Available With Current Selection Of Features")
                            agn=str(input("Want To Look For Rooms With Other Features?(Yes/No): "))
                            if(agn=='Y'):
                                pass
                            else:
                                quit()
                        else:
                            pass


                    #Code to change the status of room as booked
                    f=open('Room.dat','rb')
                    vl=[]
                    try:
                        while True:
                            d1=pickle.load(f)
                            if(rno==d1[0]):
                                d1[7]='B'
                                vl.append(d1)
                            else:
                                vl.append(d1)
                    except EOFError:
                        pass
                    f.close()

                    f=open("Room.dat",'wb')
                    for c in vl:
                        pickle.dump(c,f)
                    f.close()
                    
                    #Code to enter the records of customer in customer file 
                    f=open("Customer.dat",'ab+')
                    list2=[csno,cnam,cno,adrs,cid,cod,rno,rr]
                    pickle.dump(list2,f)
                    f.close()
                    
                    print()
                    print("Room Booked Successfully")
                    print()

                    #asking to book another record or other repeating functions
                    again=str(input("Book another room(Yes/No): "))
                    again=again.upper()
                    if(again=='Y'):
                        pass
                    else:
                        bck=str(input("Back to customer file menu(Yes/No): "))
                        bck=bck.upper()
                        if(bck=='Y'):
                            pass
                        else:
                            back=str(input("Back to main menu(Yes/No): "))
                            back=back.upper()
                            if(back=='Y'):
                                pass
                            else:
                                quit()
            elif(choice2=='2'):
                again=('Y')
                while(again=='Y'):
                    #Structure of Modification Of Record in Customer File
                    print()
                    print('','',"THE SAVOY",sep='\t')
                    print('',"      CUSTOMER FILE",sep='\t')
                    print(''," MODIFICATION OF A RECORD",sep='\t')

                    csno=str(input("Enter the customer id of customer whose data has to be modified: "))

                    #Code to check whether the customer is in hotel and modifying their records
                    file=open("History.dat",'rb')
                    hist=[]
                    try:
                        while True:
                            d1=pickle.load(file)
                            hist.append(d1[0])
                    except EOFError:
                        pass
                    if(csno in hist):
                        print("Can't Modify The Record Of This Customer")
                    else:
                        f=open("Customer.dat",'rb+')
                        vl=[]
                        try:
                            while True:
                                d1=pickle.load(f)
                                if (d1[0]==csno):
                                    print("1. Customer No.: ",d1[0])
                                    print("2. Customer Name: ",d1[1])
                                    print("3. Contact No.: ",d1[2])
                                    print("4. Address: ",d1[3])
                                    print("5. Check In Date: ",d1[4])
                                    print("6. Check Out Date: ",d1[5])
                                    print("7. Room No.: ",d1[6])
                                    upd1=eval(input("Enter 3 to 7 To Update: "))
                                    if(upd1==2):
                                        print("Can't Modify Customer Name")
                                        scrt=str(input(":"))
                                        if(scrt=='*'):
                                            d1[(upd1-1)]=str(input("Enter New Name: "))
                                            print()
                                            print("Customer Name Updated")
                                            print()
                                        else:
                                            pass
                                    elif(upd1==5 or upd1==6):
                                        d1[(upd1-1)]=str(input("Enter New Value: "))
                                        day,month,year=map(int,d1[(upd1-1)].split('-'))
                                        d1[(upd1-1)]=datetime.date(year,month,day)
                                    elif(upd1==7):
                                        i=d1[upd1-1]
                                        f1=open("Room.dat",'rb+')
                                        v=[]
                                        try:
                                            while True:
                                                d2=pickle.load(f1)
                                                if (d2[0]==i):
                                                    d2[7]='A'
                                                    v.append(d2)
                                                else:
                                                    v.append(d2)
                                        except EOFError:
                                            pass
                                        f1.close()

                                        f1=open("Room.dat",'wb')
                                        for c in v:
                                            pickle.dump(c,f1)
                                        f1.close()
                                        d1[(upd1-1)]=str(input("Enter New Value: "))
                                        f1=open("Room.dat",'rb+')
                                        v=[]
                                        try:
                                            while True:
                                                d2=pickle.load(f1)
                                                if (d2[0]==d1[(upd1-1)]):
                                                    d2[7]='B'
                                                    d1[7]=d2[6]
                                                    v.append(d2)
                                                else:
                                                    v.append(d2)
                                        except EOFError:
                                            pass
                                        f1.close()

                                        f1=open("Room.dat",'wb')
                                        for c in v:
                                            pickle.dump(c,f1)
                                        f1.close()
                                        f1=open("Room.dat",'rb+')
                                        try:
                                            while True:
                                                d2=pickle.load(f1)
                                                print(d2)
                                        except EOFError:
                                            pass
                                        f1.close()
                                    else:
                                        d1[(upd1-1)]=str(input("Enter New Value: "))
                                        print()
                                        print("Record modified successfully in the customer file")
                                        print()
                                        print("1. Customer No.: ",d1[0])
                                        print("2. Customer Name: ",d1[1])
                                        print("3. Contact No.: ",d1[2])
                                        print("4. Address: ",d1[3])
                                        print("5. Check In Date: ",d1[4])
                                        print("6. Check Out Date: ",d1[5])
                                        print("7. Room No.: ",d1[6])
                                    vl.append(d1)
                                else:
                                    vl.append(d1)
                        except EOFError:
                            pass
                        f.close()

                        f=open("Customer.dat",'wb')
                        for c in vl:
                            pickle.dump(c,f)
                        f.close()

                        print()

                    #asking to modify another record or other repeating functions
                    again=str(input("Modify another record(Yes/No): "))
                    again=again.upper()
                    if(again=='Y'):
                        pass
                    else:
                        bck=str(input("Back to customer file menu(Yes/No): "))
                        bck=bck.upper()
                        if(bck=='Y'):
                            pass
                        else:
                            back=str(input("Back to main menu(Yes/No): "))
                            back=back.upper()
                            if(back=='Y'):
                                pass
                            else:
                                quit()
            elif(choice2=='3'):
                again=('Y')
                while(again=='Y'):
                    #Structure of Removal Of Record in Customer File
                    print()
                    print('','',"THE SAVOY",sep='\t')
                    print('',"      CUSTOMER FILE",sep='\t')
                    print('',"   REMOVAL OF A RECORD",sep='\t')
                    
                    csno=str(input("Enter the customer id of customer whose data has to be removed: "))

                    #Code to remove records of customer from the history and customer file as per situation 
                    file=open("History.dat",'rb')
                    hist=[]
                    try:
                        while True:
                            d1=pickle.load(file)
                            hist.append(d1[0])
                    except EOFError:
                        pass
                    if(csno in hist):
                        f=open("History.dat",'rb+')
                        vl=[]
                        try:
                            while True:
                                d1=pickle.load(f)
                                if (d1[0]==csno):
                                    pass                            
                                else:
                                    vl.append(d1)
                        except EOFError:
                            pass
                        f.close()

                        f=open("History.dat",'wb')
                        for c in vl:
                            pickle.dump(c,f)
                        f.close()
                    else:
                        f=open("Customer.dat",'rb')
                        vl=[]
                        try:
                            while True:
                                d1=pickle.load(f)
                                if (d1[0]==csno):
                                    rno=d1[6]
                                else:
                                    pass
                        except EOFError:
                            pass
                        f.close()
                        f=open("Room.dat",'rb+')
                        vl=[]
                        try:
                            while True:
                                d1=pickle.load(f)
                                if(d1[0]==rno):
                                    d1[7]='A'
                                    vl.append(d1)
                                else:
                                    vl.append(d1)
                        except EOFError:
                            pass
                        f=open("Room.dat",'wb')
                        for c in vl:
                            pickle.dump(c,f)
                        f.close()
                    
                    f=open("Customer.dat",'rb+')
                    vl=[]
                    try:
                        while True:
                            d1=pickle.load(f)
                            if (d1[0]==csno):
                                pass                            
                            else:
                                vl.append(d1)
                    except EOFError:
                        pass
                    f.close()

                    f=open("Customer.dat",'wb')
                    for c in vl:
                        pickle.dump(c,f)
                    f.close()

                    

                    print()
                    print("Record removed successfully from the Customer file")
                    print()

                    #asking to delete another record or other repeating functions
                    again=str(input("Delete another record(Yes/No): "))
                    again=again.upper()
                    if(again=='Y'):
                        pass
                    else:
                        bck=str(input("Back to customer file menu(Yes/No): "))
                        bck=bck.upper()
                        if(bck=='Y'):
                            pass
                        else:
                            back=str(input("Back to main menu(Yes/No): "))
                            back=back.upper()
                            if(back=='Y'):
                                pass
                            else:
                                quit()
            elif(choice2=="4"):
                break
            else:
                quit()
    elif(choice1==3):
        again=('Y')
        while(again=='Y'):
            #Structure of Bill Generation
            print('','',"THE SAVOY",sep='\t')
            print('',"     BILL GENERATION",sep='\t')
            
            csno=str(input("Enter the customer id of customer whose bill has to be generated: "))

            #Code to generate the bill of the customer and confirming the check out date
            f=open("Customer.dat",'rb+')
            try:
                while True:
                    d1=pickle.load(f)
                    if (d1[0]==csno):
                        print("Check Out Date: ",d1[5])
                        check=str(input("Continue With Same Check Out Date(Yes/No): "))
                        if(check=="Y"):
                            cod=d1[5]
                            print(cod)
                        else:
                            cod=str(input("New Check Out Date: "))
                            day,month,year=map(int,cod.split('-'))
                            cod=datetime.date(year,month,day)
                            d1[5]=cod
                        print("Customer No.: ",d1[0])
                        print("Room No: ",d1[6])
                        print("Customer Name: ",d1[1])
                        print("Check In Date: ",d1[4])
                        print("Check Out Date: ",d1[5])
                        nod=(d1[5]-d1[4]).days
                        print("5. No. Of Days: ",nod,sep='')
                        fwd=str(input("Do You Want To Proceed: "))
                        fwd=fwd.upper()
                        if(fwd=='Y' or fwd=='YES'):
                            print()
                            print('-'*45)
                            print()
                            print('','',"THE SAVOY",sep='\t')
                            print('',"      CUSTOMER BILL",sep='\t')
                            print("1. Customer No.: ",d1[0])
                            print("2. Room No: ",d1[6])
                            print("2. Customer Name: ",d1[1])
                            print("3. Check In Date: ",d1[4])
                            print("4. Check Out Date: ",d1[5])
                            nod=(d1[5]-d1[4]).days
                            print("5. No. Of Days: ",nod,sep='')
                            amnt=int(d1[7])*nod
                            print("6. Amount(Without Taxes)[INR}: ",amnt)
                            if(1000<=int(d1[7])<=2499):
                                gst=(12*amnt)/100
                                ddt=(2*amnt)/100
                                print("Tax(GST): 12% Of Amount: ",gst)
                                print("Deduction: 2% Of Amount: ",ddt)
                            elif(2500<=int(d1[7])<=7499):
                                gst=(18*amnt)/100
                                ddt=(5*amnt)/100
                                print("Tax(GST): 18% Of Amount: ",gst)
                                print("Deduction: 5% Of Amount: ",ddt)
                            else:
                                gst=(28*amnt)/100
                                ddt=(10*amnt)/100
                                print("Tax(GST): 28% Of Amount: ",gst)
                                print("Deduction: 10% Of Amount: ",ddt)
                            print("Total Amount[INR]: ",amnt+gst-ddt)
                            print()
                            print('',"HOPE YOU ENJOYED OUR SERVICES",sep='\t')
                            print()
                            print('-'*45)
                            print()
                            rno=d1[6]

                            #Code to add data in history file
                            f1=open("History.dat",'ab')
                            pickle.dump(d1,f1)
                            f1.close()
                        else:
                            rno=0
                            pass
                    else:
                        pass
            except EOFError:
                pass
            f.close()
            print()

            #Code to modify data in customer file
            f=open("Customer.dat",'rb+')
            vl=[]
            try:
                while True:
                    d1=pickle.load(f)
                    if (d1[0]==csno):
                        d1[5]=cod
                        vl.append(d1)
                    else:
                        vl.append(d1)
            except EOFError:
                pass
            f.close()
            f=open("Customer.dat",'wb')
            for c in vl:
                pickle.dump(c,f)
            f.close()

            #Code to update status of room after billing
            f=open("Room.dat",'rb+')
            vl=[]
            try:
                while True:
                    d1=pickle.load(f)
                    if (d1[0]==rno):
                        d1[7]='A'
                        vl.append(d1)
                    else:
                        vl.append(d1)
            except EOFError:
                pass
            f.close()

            f=open("Room.dat",'wb')
            for c in vl:
                pickle.dump(c,f)
            f.close()

            #asking for another bill generation or other repeating functions
            again=str(input("Generate another bill(Yes/No): "))
            again=again.upper()
            if(again=='Y'):
                pass
            else:
                back=str(input("Back to main menu(Yes/No): "))
                back=back.upper()
                if(back=='Y'):
                    pass
                else:
                    quit()    
    elif(choice1==4):
        bck=("Y")
        while(bck=='Y'):
            #Structure of Report Menu
            print()
            print('','',"THE SAVOY",sep='\t')
            print('',''," REPORT",sep='\t')
            print('','',"   MENU",sep='\t')
            print("1. LIST OF ALL ROOMS")
            print("2. LIST OF ALL THE CUSTOMERS")
            print("3. LIST OF ALL AVAILABLE ROOMS")
            print("4. LIST OF OLD CUSTOMERS")
            print("5. LIST OF CURRENT CUSTOMERS")
            print("6. BACK TO MAIN MENU")
            print("7. QUIT")


            choice2=str(input("Enter your choice from the above list: "))


            if(choice2=='1'):
                #structure of list of all rooms from report menu
                print()
                print('','',"THE SAVOY",sep='\t')
                print('',''," REPORT",sep='\t')
                print('',"    LIST OF ALL ROOMS",sep='\t')

                #Code to display list of all rooms in a tabular form
                print('-'*116)
                print("| ",end="")
                print("ROOM NO.","FLOOR NO.","SINGLE/DOUBLE","REGULAR/LUXURY/SUPER-LUXURY","AC/WITHOUT AC","Mountains/Park/Lake","RENT","STATUS",sep='| ',end="|")
                print()
                lst=["ROOM NO.","FLOOR NO.","SINGLE/DOUBLE","REGULAR/LUXURY/SUPER-LUXURY","AC/WITHOUT AC","Mountains/Park/Lake","RENT","STATUS"]
                f=open("Room.dat",'rb+')
                vl=[]
                try:
                    while True:
                        d1=pickle.load(f)
                        vl.append(d1)
                except EOFError:
                    pass
                f.close()
                for c1 in vl:
                    i=0
                    for c2 in range(0,len(c1)):
                        print("| ",c1[c2],sep='',end='')
                        r=len(lst[i])
                        i+=1
                        for c3 in range(0,(r-len(c1[c2]))):
                            print(" ",end='')
                    print("|")
                print('-'*116)

                #Code for repeating functions
                bck=str(input("Back To Report Menu(Yes/No): "))
                bck=bck.upper()
                if(bck=='Y'):
                    pass
                else:
                    back=str(input("Back to main menu(Yes/No): "))
                    back=back.upper()
                    if(back=='Y'):
                        pass
                    else:
                        quit()
            
            elif(choice2=='2'):
                #structure of list of all customers from report menu
                print()
                print('','',"THE SAVOY",sep='\t')
                print('',''," REPORT",sep='\t')
                print('',"  LIST OF ALL CUSTOMERS",sep='\t')
                
                #Code to display list of all customers in a tabular form
                print('-'*105)
                print("| ",end='')
                print("CUSTOMER NO.","CUSTOMER NAME","CONTACT NO.","ADDRESS OF CUSTOMER","CHECK IN DATE","CHECK OUT DATE","ROOM NO.",sep='| ',end="|")
                print()
                lst=["CUSTOMER NO.","CUSTOMER NAME","CONTACT NO.","ADDRESS OF CUSTOMER","CHECK IN DATE","CHECK OUT DATE","ROOM NO."]
                f=open("Customer.dat",'rb+')
                vl=[]
                try:
                    while True:
                        d1=pickle.load(f)
                        vl.append(d1)
                except EOFError:
                    pass
                f.close()
                for c1 in vl:
                    i=0
                    for c2 in range(0,len(c1)):
                        if(c2==7):
                            pass
                        elif(c2==4):
                            print("| ",c1[c2]," ",end='')
                            i+=1
                        elif(c2==5):
                            print("| ",c1[c2]," ",end=' ')
                            i+=1
                        else:
                            print("| ",c1[c2],sep='',end='')
                            r=len(lst[i])
                            i+=1
                            for c3 in range(0,(r-len(c1[c2]))):
                                print(" ",end='')
                    print("|")
                print('-'*105)

                #Code for repeating functions
                bck=str(input("Back To Report Menu(Yes/No): "))
                bck=bck.upper()
                if(bck=='Y'):
                    pass
                else:
                    back=str(input("Back to main menu(Yes/No): "))
                    back=back.upper()
                    if(back=='Y'):
                        pass
                    else:
                        quit()
                print()
            elif(choice2=='3'):
                #structure of list of all available rooms from report menu
                print()
                print('','',"THE SAVOY",sep='\t')
                print('',''," REPORT",sep='\t')
                print('',"LIST OF ALL AVAILABLE ROOMS",sep='\t')

                #Code to display list of all available rooms in a tabular form
                print('-'*116)
                print("| ",end="")
                print("ROOM NO.","FLOOR NO.","SINGLE/DOUBLE","REGULAR/LUXURY/SUPER-LUXURY","AC/WITHOUT AC","Mountains/Park/Lake","RENT","STATUS",sep='| ',end="|")
                print()
                lst=["ROOM NO.","FLOOR NO.","SINGLE/DOUBLE","REGULAR/LUXURY/SUPER-LUXURY","AC/WITHOUT AC","Mountains/Park/Lake","RENT","STATUS"]
                f=open("Room.dat",'rb+')
                vl=[]
                try:
                    while True:
                        d1=pickle.load(f)
                        if(d1[7]=='A'):
                            vl.append(d1)
                        else:
                            pass
                except EOFError:
                    pass
                f.close()
                for c1 in vl:
                    i=0
                    for c2 in range(0,len(c1)):
                         print("| ",c1[c2],sep='',end='')
                         r=len(lst[i])
                         i+=1
                         for c3 in range(0,(r-len(c1[c2]))):
                              print(" ",end='')
                    print("|")
                print('-'*116)

                #Code for repeating functions
                bck=str(input("Back To Report Menu(Yes/No): "))
                bck=bck.upper()
                if(bck=='Y'):
                    pass
                else:
                    back=str(input("Back to main menu(Yes/No): "))
                    back=back.upper()
                    if(back=='Y'):
                        pass
                    else:
                        quit()
            elif(choice2=='4'):
                #structure of list of old customers from report menu
                print()
                print('','',"THE SAVOY",sep='\t')
                print('',''," REPORT",sep='\t')
                print('',"  LIST OF OLD CUSTOMERS",sep='\t')

                #Code to display list of old customers in a tabular form
                print('-'*105)
                print("| ",end='')
                print("CUSTOMER NO.","CUSTOMER NAME","CONTACT NO.","ADDRESS OF CUSTOMER","CHECK IN DATE","CHECK OUT DATE","ROOM NO.",sep='| ',end="|")
                print()
                lst=["CUSTOMER NO.","CUSTOMER NAME","CONTACT NO.","ADDRESS OF CUSTOMER","CHECK IN DATE","CHECK OUT DATE","ROOM NO."]
                f=open("History.dat",'rb+')
                vl=[]
                try:
                    while True:
                        d1=pickle.load(f)
                        vl.append(d1)
                except EOFError:
                    pass
                f.close()
                for c1 in vl:
                    i=0
                    for c2 in range(0,len(c1)):
                        if(c2==7):
                            pass
                        elif(c2==4):
                            print("| ",c1[c2]," ",end='')
                            i+=1
                        elif(c2==5):
                            print("| ",c1[c2]," ",end=' ')
                            i+=1
                        else:
                            print("| ",c1[c2],sep='',end='')
                            r=len(lst[i])
                            i+=1
                            for c3 in range(0,(r-len(c1[c2]))):
                                print(" ",end='')
                    print("|")
                print('-'*105)

                #Code for repeating functions
                bck=str(input("Back To Report Menu(Yes/No): "))
                bck=bck.upper()
                if(bck=='Y'):
                    pass
                else:
                    back=str(input("Back to main menu(Yes/No): "))
                    back=back.upper()
                    if(back=='Y'):
                        pass
                    else:
                        quit()
                        
            elif(choice2=='5'):
                #structure of list of current customers from report menu
                print()
                print('','',"THE SAVOY",sep='\t')
                print('',''," REPORT",sep='\t')
                print('',"LIST OF CURRENT CUSTOMERS",sep='\t')

                #Code to display list of current customers in a tabular form
                print('-'*116)
                print("| ",end='')
                print("CUSTOMER NO.","CUSTOMER NAME","CONTACT NO.","ADDRESS OF CUSTOMER","CHECK IN DATE","CHECK OUT DATE(Tentative)","ROOM NO.",sep='| ',end="|")
                print()
                lst=["CUSTOMER NO.","CUSTOMER NAME","CONTACT NO.","ADDRESS OF CUSTOMER","CHECK IN DATE","CHECK OUT DATE(Tentative)","ROOM NO."]
                f=open("History.dat",'rb+')
                hist=[]
                try:
                    while True:
                        d1=pickle.load(f)
                        hist.append(d1)
                except EOFError:
                    pass
                f.close()
                f=open("Customer.dat",'rb+')
                vl=[]
                try:
                    while True:
                        d1=pickle.load(f)
                        if(d1 in hist):
                            None
                        else:
                            vl.append(d1)
                except EOFError:
                    pass
                f.close()
                for c1 in vl:
                    i=0
                    for c2 in range(0,len(c1)):
                        if(c2==7):
                            pass
                        elif(c2==4):
                            print("| ",c1[c2]," ",end='')
                            i+=1
                        elif(c2==5):
                            print("| ",c1[c2],"            ",end=' ')
                            i+=1
                        else:
                            print("| ",c1[c2],sep='',end='')
                            r=len(lst[i])
                            i+=1
                            for c3 in range(0,(r-len(c1[c2]))):
                                print(" ",end='')
                    print("|")
                print('-'*116)

                #Code for repeating functions
                bck=str(input("Back To Report Menu(Yes/No): "))
                bck=bck.upper()
                if(bck=='Y'):
                    pass
                else:
                    back=str(input("Back to main menu(Yes/No): "))
                    back=back.upper()
                    if(back=='Y'):
                        pass
                    else:
                        quit()
                        
            elif(choice2=='6'):
                back='Y'
                break
            else:
                quit()
    elif(choice1==5):
        bck=("Y")
        while(bck=='Y'):
            #Structure of Search By Name Menu
            print()
            print('','',"THE SAVOY",sep='\t')
            print('',"      SEARCH BY NAME",sep='\t')
            print('','',"   MENU",sep='\t')
            print("1. CURRENT CUSTOMERS")
            print("2. OLD CUSTOMERS")
            print("3. BACK TO MAIN MENU")
            print("4. QUIT")

            choice2=str(input("Enter your choice from the above list: "))


            if(choice2=='1'):
                print()
                print('','',"THE SAVOY",sep='\t')
                print('',"      SEARCH BY NAME",sep='\t')
                print('',"    CURRENT  CUSTOMERS",sep='\t')
                cnam=str(input("Enter The Name: "))

                #Code to show data of the customer searched
                print('-'*89)
                print("| ",end='')
                print("CUSTOMER NO.","CUSTOMER NAME","CONTACT NO.","ADDRESS OF CUSTOMER","CHECK IN DATE","ROOM NO.",sep='| ',end="|")
                print()
                lst=["CUSTOMER NO.","CUSTOMER NAME","CONTACT NO.","ADDRESS OF CUSTOMER","CHECK IN DATE","ROOM NO."]
                f=open("History.dat",'rb+')
                hist=[]
                try:
                    while True:
                        d1=pickle.load(f)
                        hist.append(d1)
                except EOFError:
                    pass
                f.close()
                f=open("Customer.dat",'rb+')
                v=[]
                try:
                    while True:
                        d1=pickle.load(f)
                        if(d1 in hist):
                            None
                        else:
                            v.append(d1)
                except EOFError:
                    pass
                f.close()
                vl=[]
                for c in v:
                    if(c[1]==cnam):
                        vl.append(c)
                    else:
                        pass
                for c1 in vl:
                    i=0
                    for c2 in range(0,len(c1)):
                        if(c2==5 or c2==7):
                            pass
                        elif(c2==4):
                            print("| ",c1[c2]," ",end='')
                            i+=1
                        else:
                            print("| ",c1[c2],sep='',end='')
                            r=len(lst[i])
                            i+=1
                            for c3 in range(0,(r-len(c1[c2]))):
                                print(" ",end='')
                    print("|")
                print('-'*89)

                #Code for repeating functions
                bck=str(input("Back To Search By Name Menu(Yes/No): "))
                bck=bck.upper()
                if(bck=='Y'):
                    pass
                else:
                    back=str(input("Back to main menu(Yes/No): "))
                    back=back.upper()
                    if(back=='Y'):
                        pass
                    else:
                        quit()
            elif(choice2=='2'):
                print()
                print('','',"THE SAVOY",sep='\t')
                print('',"      SEARCH BY NAME",sep='\t')
                print('',"      OLD  CUSTOMERS",sep='\t')
                cnam=str(input("Enter The Name: "))

                #Code to show data of the customer searched
                print('-'*90)
                print("| ",end='')
                print("CUSTOMER NO.","CUSTOMER NAME","CONTACT NO.","ADDRESS OF CUSTOMER","CHECK OUT DATE","ROOM NO.",sep='| ',end="|")
                print()
                lst=["CUSTOMER NO.","CUSTOMER NAME","CONTACT NO.","ADDRESS OF CUSTOMER","CHECK OUT DATE","ROOM NO."]
                f=open("History.dat",'rb+')
                v=[]
                try:
                    while True:
                        d1=pickle.load(f)
                        v.append(d1)
                except EOFError:
                    pass
                f.close()
                vl=[]
                for c in v:
                    if(c[1]==cnam):
                        vl.append(c)
                    else:
                        pass
                for c1 in vl:
                    i=0
                    for c2 in range(0,len(c1)):
                        if(c2==4 or c2==7):
                            pass
                        elif(c2==5):
                            print("| ",c1[c2]," ",end=' ')
                            i+=1
                        else:
                            print("| ",c1[c2],sep='',end='')
                            r=len(lst[i])
                            i+=1
                            for c3 in range(0,(r-len(c1[c2]))):
                                print(" ",end='')
                    print("|")
                print('-'*90)

                #Code for repeating functions
                bck=str(input("Back To Search By Name Menu(Yes/No): "))
                bck=bck.upper()
                if(bck=='Y'):
                    pass
                else:
                    back=str(input("Back to main menu(Yes/No): "))
                    back=back.upper()
                    if(back=='Y'):
                        pass
                    else:
                        quit()  
            elif(choice2=='3'):
                back='Y'
                break
            else:
                quit()
    else:
        exit()
