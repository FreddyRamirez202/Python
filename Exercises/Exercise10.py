meter = 1
approved = 0
failed = 0

num_students = int(input("How many students do you have?: "))

while meter <= num_students:
    rating = int(input(f"What rating do you want to put in to student {meter}?: "))
    
    if rating >= 3:
        approved +=1
        
    else:
        failed +=1
        
    meter +=1
    
print (f"Students approved: {approved}") 
print (f"Students failed: {failed}")             
