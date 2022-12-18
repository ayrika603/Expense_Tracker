import matplotlib.pyplot as plt
import numpy as np

import pickle
def enter_expenses():
    f=open('expense.dat','wb')
    n=int(input('Enter no. of fields '))
    
    t=1
    while t>0:
        print('to continue enter 1 and to exit enter 0')
        r=int(input('enter option '))
        l=[]
        if r==1:
            month=input('enter month ')
            if month not in l:
                l.append(month)
                
                d={'month': month}
                for x in range(0,n):
                    y=input('enter name of field ')
                    e=int(input('enter expense '))
                    d1={y:e}
                    d.update(d1)
                pickle.dump(d,f)
            else:
                print('the fields for the month have already been entered')
        elif r==0:
            print('Thank you')
            break
        else:
            print('please enter a valid option')
        t=t+1
    f.close()

def display_expenses():
    f=open('expense.dat','rb')
    while True:
        try:
            rec=pickle.load(f)
            d=rec.keys()
            l=list(d)
            for x in range(0,len(l)):
                print(l[x],':',rec[l[x]])
            
        except EOFError:
            break
    f.close()

def graph_monthly_expenses():
    f=open('expense.dat','rb')
    m=input('enter month')
    print('Select one of the following options to obtain the graph of the expenditure in the selected month')
    print('1.bar graph')
    print('2.pie chart')
    n=int(input('enter option number '))
    
    while True:
        try:
            rec=pickle.load(f)
        
            d=rec.keys()
            t=rec['month']
            l=list(d)
            l2=[]
            for x in l:
                if x!='month':
                    
                    l2.append(rec[x])
        
            l.pop(0)
            
            
            if m==t:
                if n==1:
                    plt.bar(l,l2)
                    plt.ylabel('expenses')
                    plt.title('expenditure in the month of '+t)
                    plt.show()
                elif n==2:
                    plt.pie(l2, labels = l,autopct='%1.2f%%')
                    plt.show()
                else:
                    print('please enter valid option number')
                    break
        except EOFError:
            break
    f.close() 

def graph_yearly_expenditure():
    f=open('expense.dat','rb')
    print('enter 1 to obtain the graph of the net expenditure in each month or enter 2 to obtain the graph of the expenditure in a selected field for all the months')
    n=int(input('enter option '))
    if n==2:
        y=input('Enter the field ')
    l1=[]
    l2=[]
    while True:
        try:
            rec=pickle.load(f)
            d=rec.keys()
            l=list(d)
            t=rec['month']
            l2.append(t)
            if n==1:
                s=0
                for x in l:
                    if x!='month':
                        s=s+rec[x]
                l1.append(s)
            elif n==2:
                r=0
                for x in l:
                    if y==x:
                        l1.append(rec[x])
                        r=r+1
                if r==0:
                    print('No field found')
                    break
            else:
                print('please enter appropriate option number')
                break
        except EOFError:
            break
    f.close()
    print('select 1to obtain a line graph and 2 to obtain a pie chart')
    m=int(input('Enter option '))
    if m==1:
        x=np.array(l2)
        
        plt.plot(x,l1)
        plt.ylabel('expenses')
        plt.title('yearly expenditure')
        plt.show()
    elif m==2:
        plt.pie(l1, labels = l2,autopct='%1.2f%%')
        plt.show()
    else:
        print('please enter a valid option')
        
def edit_expenses():
    f=open('expense.dat','rb')
    f1=open('new_expense.dat','wb')
    m=input('enter month ')
    y=input('enter the field which you wish to edit ')
    
    while True:
        try:
            rec=pickle.load(f)
            d=rec.keys()
            l=list(d)
            d1={}
            for x in l:
                if m==rec['month']:
                    if x==y:
                        n=int(input('enter the value '))
                        d2={x:n}
                        d1.update(d2)
                    else:
                            d2={x:rec[x]}
                            d1.update(d2)
                else: 
                        d2={x:rec[x]}
                        d1.update(d2)
            pickle.dump(d1,f1)
        except:
            break
    f.close()
    f1.close()
    f=open('expense.dat','wb')
    f1=open('new_expense.dat','rb')
    while True:
        try:
            rec=pickle.load(f1)
            pickle.dump(rec,f)
        except:
            break
    f.close()
    f1.close()

def delete_expenses():
    f=open('expense.dat','rb')
    f1=open('new_expense2.dat','wb')
    y=input('Enter month whose record is to be deleted ')
    while True:
        try:
            rec=pickle.load(f)
            if rec['month']==y:
                continue
            else:
                pickle.dump(rec,f1)
        except:
            break
    f.close()
    f1.close()
    f=open('expense.dat','wb')
    f1=open('new_expense2.dat','rb')
    while True:
        try:
            rec=pickle.load(f1)
            pickle.dump(rec,f)
        except:
            break
    f.close()
    f1.close()

def max_min_expenditure():
    f=open('expense.dat','rb')
    maximum=0
    minimum=0
    d2={}
    while True:
        try:
            rec=pickle.load(f)
            s=0
            d=rec.keys()
            l=list(d)
            t=rec['month']
            for x in l:
                if x!='month':
                    s=s+rec[x]
            d1={t:s}
            d2.update(d1)
        except:
            break
    d3=sorted(d2)
    print('maximum expenditure is',d2[d3[0]],'in the month of',d3[0])
    print('minimum expenditure is',d2[d3[len(d3)-1]],'in the month of',d3[len(d3)-1])

print('select the option number to execute a function')
print('1. enter fields for expenditure in various months')
print('2. display the records')
print('3. obtain the graph for monthly expenses')
print('4. obtain the graph for yearly expenditure')
print('5. edit the expenses of a selected month')
print('6. delete the records of the selected month')
print('7. display the maximum and minimum expenditure in a year')
print('8. Exit')

x=1
while x>0:
    n=int(input('Enter option number'))

    if n==1:
        enter_expenses()
    elif n==2:
        display_expenses()
    elif n==3:
        graph_monthly_expenses()
    elif n==4:
        graph_yearly_expenditure()
    elif n==5:
        edit_expenses()
    elif n==6:
        delete_expenses()
    elif n==7:
        max_min_expenditure()
    elif n==8:
        print('Thank you')
        break
    else:
        print('please enter appropriate option number')
    
