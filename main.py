import csv
import os
from tabulate import tabulate
from datetime import datetime
def clear():
      os.system('cls' if os.name == 'nt' else 'clear')

while True:
 print("\n\t-------- Main Menu --------\t\n\n")
 print("1. Add Expanses")
 print("2. View Expanses")
 print("3. Edit Expanses")
 print("4. Delete Expanses")
 print("5. Format Expanses")
 print("6. Summary")
 print("7. Exit")
 file_path="data.csv"
 if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
     with open(file_path, "w", newline="") as f:
         writer = csv.writer(f)
         writer.writerow(["Time", "Category", "Amount", "Description"])
         

 def add_expanse():
     try:
       expanses=int(input("How many expanses you want to add : "))
       clear()
     except ValueError:
        
          clear()
          print("-- Invalid Amount -- ")
          input("Try again! ") 
          clear()
          expanses=int(input("How many expanses you want to add : "))
          clear()
             
     j=1
     while(j<=expanses):
        category=input("Enter Category : ").lower()
        i=1
        k=10
        while(i<=k):
         try:
           amount=int(input("Enter Amount : "))
           break
         except ValueError:
             print("\n\n\t\tInvalid Amount:")
             input(f"\t\tTry again! {k} tries remaining\n ")  
             clear()
             i=i+1
             
             
        description=input("Enter description : ")
        clear()
        time= datetime.now().strftime("%d-%b-%Y %I:%M %p")
        
        
        
        with open(file_path,"a",newline="") as f:
            writer=csv.writer(f)
            writer.writerow([time,category,amount,description])
        print(f"Expense added successfully!")
        
        
        
        if j==expanses:
            break
        else:
            input("Enter any key to to perceed! ")
            clear()
               
        j=j+1
        
     input("Enter any key to exit! ")
     clear()

 
 
 
 




 def view_expanse():
     
     if os.path.getsize(file_path) == 0:
             print("No Expanses found.")
             return
     else:
      with open(file_path,"r") as f:
         reader=csv.reader(f)
         data=list(reader)
         print(tabulate(data, headers="firstrow", tablefmt="pretty"))
         input("Enter any key to exit! ")
         clear()
         





 def load_expanse(): 
      expanse_tracker=[]
      with open(file_path,"r") as f:
              reader=csv.reader(f)
              header=next(reader)
              for row in reader:
                  expanse_tracker.append(row)
              return header, expanse_tracker








 def edit_expanse(): 
     header,expanse_tracker=load_expanse()
     if len(expanse_tracker)==0:
         print("Expanse list is empty!")
         input("Enter any key to exit ")
         clear()
     else:    
       for i,row in enumerate(expanse_tracker,start = 1):
           print(f"{i}. {row}")
  
       repeat="y"
       while(repeat=="y") :   
        
        Choice=int(input("\nEnter a number to edit : "))
        clear()
        if Choice >=1 and Choice <=len(expanse_tracker):
             row=expanse_tracker[Choice-1]
             print("NOTE: Leave blank to keep old values ")
             print("==>> Enter new values\n")
             
             for i, head in enumerate(header):
                new_value=input(f"\t{head} ({row[i]}):\t  ")
             
                
                
                if new_value.strip():
                    row[i]=new_value
              
                 
             with open(file_path,"w",newline="") as f:
                      writer=csv.writer(f)
                      writer.writerow(header)
                      writer.writerows(expanse_tracker)
                      print("\nExpanse added successfully! ")
             input("\nEnter any key to perceed! ")
             clear()
             for i,row in enumerate(expanse_tracker,start = 1):
               print(f"{i}. {row}")
             repeat=input("\nDo you want to edit more(y/n): ").lower()
             if repeat=="n":
                 break       
        else:
                print("\nError: Invalid number")     
                
       input("\nEnter any key to exit! ")         
       clear()






 def format_data():
     
     with open("data.csv", "w", newline="") as f:
         writer = csv.writer(f)
         writer.writerow(["Time", "Category", "Amount", "Description"])
     print("CSV data cleared successfully!")
     input("Enter any key to exit! ")
     clear()








 def delete_expanse():
   
     header,expanse_tracker=load_expanse()
     if len(expanse_tracker)==0:
         print("Expanse list is empty!")
         input("Enter any key to exit! ")
         clear()
     else:   
       for i,row in enumerate(expanse_tracker,start = 1):
           print(f"{i}. {row}")
       iteration=1
       while(True):    
        try:
          n_of_deletion=int(input("\nHow many expanses you want to delete :"))

          clear()
          break
        except ValueError:
            print("Invalid Entry! ")
            input("Try Again! ")  
            clear()
            iteration+=1
       j=1
       while(j<=n_of_deletion):
         for i,row in enumerate(expanse_tracker,start = 1):
           print(f"{i}. {row}")    
   
         Choice=int(input("\nEnter a number to delete an expanse : "))
         clear()
         try:
          if Choice >=1 and Choice <=len(expanse_tracker):
           
            expanse_tracker.pop(Choice-1)
   
            with open(file_path,"w",newline="") as f:
                       writer=csv.writer(f)
                       writer.writerow(header)
                       writer.writerows(expanse_tracker)
            print("\nExpanse deleted successfully! ") 
            input("Enter any key to exit!") 
            clear()
            
  
         except ValueError:
                 print("Error: Invalid number")
                 input("Enter any key to exit! ")
                 clear()
         j=j+1 
         





  
 def summary_expanse():
    header,expanse_tracker=load_expanse()
    if len(expanse_tracker)==0:
         print("Expanse list is empty!")
         input("\nEnter any key to exit! ")
         clear()
    else: 
      for i,row in enumerate(expanse_tracker,start = 1):
           print(f"{i}. {row}")
      search=int(input("\n1. Category\n2. Total\n\nSelect for summary: ")) 
      clear()
      if(search==1):
                    search_no=int(input("How many times: "))
                    clear()
                    for i in range(search_no):
                       for i,row in enumerate(expanse_tracker,start = 1):
                           print(f"{i}. {row}")
                       print("\n(Note: Enter for total expanse)")    
                       user_category=(input("Enter Category: "))
                       clear()
                       amount=[]
      
                       for expanse in expanse_tracker:
                           ctg=expanse[1].strip().lower()
                           if user_category == ctg or  ctg.startswith(user_category)   :
                               
                               amount.append(int(expanse[2])) 
                       if not amount:
                               print("No matches!")   
                               input("Enter any key to perceed! ") 
                               clear() 
                       else:    
                        for i,row in enumerate(expanse_tracker,start = 1):
                           print(f"{i}. {row}")

                        Total_amount=sum(amount)  
                            
                        print(f"\nThe List of Total Expanses used by Category {user_category}: {amount}")  
                        print(f"Total Expanse of Category {user_category}: {Total_amount}") 
                        input("\nEnter any key to exit! ")  
                        clear()  
                       
      elif(search==2):
               Total_amount=0
               list_amount=[]
               for i,row in enumerate(expanse_tracker,start = 1):
                        print(f"{i}. {row}")
                        list_amount.append(int(row[2]))   
               
               Total_amount=sum(list_amount)
               print(f"\nThe List of Total Expanses till now are: {list_amount}")  
               print(f"Total Expanse till now are : {Total_amount}") 
               input("\nEnter any key to exit! ")  
               clear()
      
      else:
          print("Invalid Entry!")
          input("Try Again! ")  
          clear()
          summary_expanse()  
                  



            
                                  
                     
 choice=int(input("\n\nEnter your choice : "))
 clear()
 if(choice==1):
     add_expanse()
 elif choice==2:
     view_expanse() 
 elif choice==3:       
 
     edit_expanse()
 elif choice==4:
     
     delete_expanse()     
 elif choice==5:       
 
     format_data()
 elif choice==6:       
 
     summary_expanse()
 elif choice==7:
       break
 else:
     print("\nInvalid Entry! ")
     input("Enter any key to perceed: ") 
     clear()
     continue       
 

 
 
   
 
 
 
             
 
 
 
     
 


