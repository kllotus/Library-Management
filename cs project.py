import mysql.connector
from datetime import date
from tabulate import tabulate
con=mysql.connector.connect(host='localhost',user='root',password='mykanwal.sql30',database='library')
if con.is_connected():
    cur=con.cursor()


def display():
    print('*'*90)
    print('*'*90)
    print('\t\t\tWelcome')
    print('*'*90)
    print('*'*90)

def add_bk():
    display()
    from tabulate import tabulate
    print('\t\t\tGiven book is the latest book ID')
    lastbk='select max(bookID) from books'
    cur.execute(lastbk)
    for i in cur:
        print('\t\t\t',i)
    bookid=input('\t\t\tEnter Book ID:\t\t\t\t')
    title=input('\t\t\tEnter title of the book:\t\t')
    author=input('\t\t\tName of the author:\t\t\t')
    category=input('\t\t\tEnter the genre of the book:\t\t')
    pub=input('\t\t\tEnter name of the publisher:\t\t')
    copies=int(input('\t\t\tEnter number of copies:\t\t\t'))
    status=input('\t\t\tEnter available/not available:\t\t')
    query="insert into books values(%s,%s,%s,%s,%s,%s,%s)"
    data=(bookid,title,author,category,pub,copies,status)
    cur.execute(query,data)
    con.commit()
    print('\t\t\tRECORD HAS BEEN ADDED..')
    query="select * from books where bookID='{}'".format(bookid)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(result,headers=['bookID','title','author','category','publisher','copies','status'],tablefmt='fancy_grid'))


def searchtitle():
    from tabulate import tabulate
    booktitle=input('\t\t\tEnter title to serach:\t')
    query="select * from books where title='{}'".format(booktitle)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(result,headers=['bookID','title','author','category','publisher','copies','status'],tablefmt='fancy_grid'))
    else:
        print('\t\t\tNO MATCH FOUND')

def searchauthor():
    from tabulate import tabulate
    bookauthor=input('\t\t\tEnter author to be searched:\t')
    query="select * from books where author='{}'".format(bookauthor)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(result,headers=['bookID','title','author','category','publisher','copies','status'],tablefmt='fancy_grid'))
    else:
        print('\t\t\tNO MATCH FOUND')
def searchbook_():
    while True:
        display()
        print('\t\t\t1.SEARCH BY TITLE')
        print('\t\t\t2.SEARCH BY AUTHOR')
        print('\t\t\t3.RETURN')
        ch=int(input('\t\t\tENter choice:\t'))
        if ch==1:
            searchtitle()
        elif ch==2:
            searchauthor()
        else:
            break

def updatebid():
    from tabulate import tabulate
    bookid=input('\t\t\tEnter book ID to update:\t\t')
    query="select * from books where bookID='{}'".format(bookid)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:print(tabulate(result,headers=['bookID','title','athor','category','publisher','copies','status'],tablefmt='fancy_grid'))
    ch=input('\t\t\tDo you want to update yes/no:\t\t')
    if ch=='yes' or ch=='Yes':
        bookidnew=input('\t\t\tEnter new book ID:\t\t\t')
        query="update books set bookID='{}' where bookID='{}'".format(bookidnew,bookid)
        cur.execute(query)
        con.commit()
        print('\t\t\tRECORD IS UPDATED')
        query="select * from books where bookID='{}'".format(bookidnew)
        cur.execute(query)
        result=cur.fetchall()
        if cur.rowcount>0:
            print(tabulate(result,headers=['bookID','title','author','category','publisher','copies','status'],tablefmt='fancy_grid'))
        elif ch=='no' or ch=='No':
            print()
        else:
            print('\t\t\tNO MATCHING RECORD FOUND')
def updatepublisher():
    from tabulate import tabulate
    title=input('\t\t\tEnter the title whose publisher is to be updated:\t')
    query="select * from books where title='{}'".format(title)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(result,headers=['bookID','title','author','category','publisher','copies','status'],tablefmt='fancy_grid'))
        ch=input('\t\t\tDo you want to update yes/no:\t\t\t')
        if ch=='yes' or ch=='Yes':
            new_publisher=input('\t\t\tENter new publisher:\t\t\t\t')
            query="update books set publisher='{}' where title='{}'".format(new_publisher,title)
            cur.execute(query)
            con.commit()
            print('\t\t\tRECORD IS UPDATED')
            query="select * from books where title='{}'".format(title)
            cur.execute(query)
            result=cur.fetchall()
            if cur.rowcount>0:
                print(tabulate(result,headers=['bookID','title','author','category','publisher','copies','status'],tablefmt='fancy_grid'))
            elif ch=='no' or ch=='NO':
                print()
            else:
                print('\t\t\tNO MATCHING RECORD FOUND')

def updatebook():
    while True:
        display()
        print('\t\t\t1.UPDATE BY BOOKID')
        print('\t\t\t2.UPDATE PUBLISHER')
        print('\t\t\t3.RETURN')
        ch=int(input('\t\t\t Enter choice:\t'))
        if ch==1:
            updatebid()
        elif ch==2:
            updatepublisher()
        else:
            break

def deletebid():
    from tabulate import tabulate
    bookid=input('\t\t\tEnter book ID to delete:\t\t')
    query="select * from books where bookid='{}'".format(bookid)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(result,headers=['bookID','title','author','category','publisher','copies','status'],tablefmt='fancy_grid'))
    ch=input('\t\t\tDo you want to delete yes/no:\t\t')
    if ch=='yes' or ch=='Yes':
        query="delete from books where bookid='{}'".format(bookid)
        cur.execute(query)
        con.commit()
        print('\t\t\tRECORD IS DELETED')
    elif ch=='no' or ch=='No':
        print()
    else:
        print('\t\t\tNO MATCHING RECORD FOUND')
def deletetitle():
    from tabulate import tabulate
    title=input('\t\t\tEnter book title to delete:\t\t')
    query="select * from books where title='{}'".format(title)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(result,headers=['bookID','title','author','category','publisher','copies','status'],tablefmt='fancy_grid'))
        ch=input('\t\t\tDo you want to delete yes/no:\t\t')
        if ch=='yes' or ch=='Yes':
            query="delete from books where title='{}'".format(title)
            cur.execute(query)
            con.commit()
            print('\t\t\tRECORD IS DELETED')
        elif ch=='no' or ch=='No':
            print()
        else:
            print('\t\t\tNO MATCHING RECORD FOUND')
def delete_book():
    while True:
        display()
        print('\t\t\t1.DELETE BY BOOK ID')
        print('\t\t\t2.DELETE BY TITLE')
        print('\t\t\t3.RETURN')
        ch=int(input('\t\t\tEnter choice:\t'))
        if ch==1:
            deletebid()
        elif ch==2:
            deletetitle()
        else:
            break


def add_mem():
    display()
    print('\t\t\tGiven below is the latest memberID')
    lastID='select max(memID) from members'
    cur.execute(lastID)
    for i in cur:
        print('\t\t\t',i)
        memid=input('\t\t\tEnter memberID:\t\t\t')
        name=input('\t\t\tEnter name:\t\t\t')
        gender=input('\t\t\tEnter gender:\t\t\t')
        ad=input('\t\t\tEnter the address:\t\t\t')
        city=input('\t\t\tEnter city:\t\t\t')
        phoneno=int(input('\t\t\tEnter phone number:\t\t\t'))
        emailid=input('\t\t\tEnter email ID:\t\t\t')
        query="insert into members values(%s,%s,%s,%s,%s,%s,%s)"
        data=(memid,name,gender,ad,city,phoneno,emailid)
        cur.execute(query,data)
        con.commit()
        print('\t\t\tRECORD HAS BEEN ADDED')
        query="select * from members where memID='{}'".format(memid)
        cur.execute(query)
        result=cur.fetchall()
        if cur.rowcount>0:
            print(tabulate(result,headers=['memID','Name','Gender','Address','City','PhoneNo','emailID'],tablefmt='fancy_grid'))

def searchmemid():
    memberid=input('\t\t\tEnter member id to serach:\t')
    query="select * from members where memID='{}'".format(memberid)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(result,headers=['memID','Name','Gender','Address','City','PhoneNo','emailID'],tablefmt='fancy_grid'))
    else:
        print('\t\t\tNO MATCH FOUND')

def searchmem_name():
    membername=input('\t\t\tEnter member name to search:\t')
    query="select * from members where Name='{}'".format(membername)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(result,headers=['memID','Name','Gender','Address','City','PhoneNo','emailID'],tablefmt='fancy_grid'))
    else:
        print('\t\t\tNO MATCH FOUND')
def search_mem():
    while True:
        display()
        print('\t\t\t1.SEARCH BY MEMBER ID')
        print('\t\t\t2.SEARCH BY MEMBER NAME')
        print('\t\t\t3.RETURN')
        ch=int(input('\t\t\tEnter choice:\t'))
        if ch==1:
            searchmemid()
        elif ch==2:
            searchmem_name()
        else:
            break

def updatephone():
    memid=input('\t\t\tEnter member ID to update:\t\t')
    query="select * from members where memID='{}'".format(memid)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(result,headers=['memID','Name','Gender','Address','City','PhoneNO','emailID'],tablefmt='fancy_grid'))
        ch=input('\t\t\tDo you want to update yes/no:\t\t')
        if ch=='yes' or ch=='Yes':
            newphone=input('\t\t\tDo you want to update yes/no:\t\t')
            query="update members set PhoneNo='{}' where memID='{}'".format(newphone,memid)
            cur.execute(query)
            con.commit()
            print('\t\t\tRECORD IS UPDATED')
            query="select * from members where memID='{}'".format(memid)
            cur.execute(query)
            result=cur.fetchall()
            if cur.rowcount>0:
                print(tabulate(result,headers=['memID','Name','Gender','Address','City','PhoneNO','emailID'],tablefmt='fancy_grid'))
            elif ch=='no' or ch=='No':
                print()
            else:
                print('\t\t\tNO MATCHING RECORD FOUND')
def updatemem_address():
    memid=input('\t\t\tEnter member ID to update:\t\t')
    query="select * from members where memid='{}'".format(memid)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(result,headers=['memID','Name','Gender','Address','City','PhoneNO','emailID'],tablefmt='fancy_grid'))
        ch=input('\t\t\tDo you want to update yes/no:\t\t')
        if ch=='yes' or ch=='Yes':
            addressnew=input('\t\t\tEnter new address:\t\t\t')
            query="update members set address='{}' where memid='{}'".format(addressnew,memid)
            cur.execute(query)
            con.commit()
            print('\t\t\tRECORD IS UPDATED')
            query="select * from members where memID='{}'".format(memid)
            cur.execute(query)
            result=cur.fetchall()
            if cur.rowcount>0:
                print(tabulate(result,headers=['memID','Name','Gender','Address','City','PhoneNO','emailID'],tablefmt='fancy_grid'))
            elif ch=='no' or ch=='No':
                print()
            else:
                print('\t\t\tNO MATCHING RECORD FOUND')
def update_mem():
    while True:
        display()
        print('\t\t\t1.UPDATE MEMBER PHONE NUMBER')
        print('\t\t\t2.UPDATE MEMBER ADDRESS')
        print('\t\t\t3.RETURN')
        ch=int(input('\t\t\tEnter choice:\t'))
        if ch==1:
            updatephone()
        elif ch==2:
            updatemem_address()
        else:
            break


def deletememid():
    memid=input('\t\t\tEnter member ID to delete:\t\t')
    query="select * from members where memID='{}'".format(memid)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(result,headers=['memID','Name','Gender','Address','City','PhoneNO','emailID'],tablefmt='fancy_grid'))
        ch=input('\t\t\tDo you want to delete yes/no:\t\t')
        if ch=='yes' or ch=='Yes':
            query="delete from members where memID='{}'".format(memid)
            cur.execute(query)
            con.commit()
            print('\t\t\tRECORD IS DELETED')
        elif ch=='no' or ch--'No':
            print()
    else:
        print('\t\t\tNO MATCHING RECORD FOUND')


def add_issues(bkid):
    from tablulate import tabulate
    from datetime import date
    mem=input('\t\t\tEnter the member ID:\t\t\t')
    query="select memID from members where memID='{}'".format(mem)
    cur.execute(query)
    result=cur.fetchall()
    memberid=mem
    query="select memID,Name,Bookissued,max(returndate),duefines,status from issues_return where memID='{}'".format(memberid)
    cur.execute(query)
    res=cur.fetchall()
    if cur.rowcount>0:
        print()
        print('\t\t\tTERMS AND CONDITIONS')
        print('\t\t\t1.if due fine 0 and pending book can be issued')
        print('\t\t\t2.if due fine is there and pending book cannot be issued until previous one returned')
        print('\t\t\t3.if status returned the book can be issued')
        print()
        print('\t\t\tDo you want continue issuing')
        ch=input('\t\t\tenter yes or no:t\t\t')
        if ch=='yes' or ch=='Yes':
            chkbook(bkid)
            query="select Name from members where memID='{}'".format(mem)
            cur.execute(query)
            result1=cur.fetchall()
            query="select title from books where bID='{}'".format(bkid)
            cur.execute(query)
            result2=cur.fetchall()
            valid=result+result1+result2
            L=[]
            for i in valid:
                for j in i:
                    L.append(j)
                print('\t\t\tEnter the issue date')
                y=int(input('\t\t\tEnter the year:\t\t\t\t'))
                m=int(input('\t\t\tEnter the month:\t\t\t'))
                d=int(input('\t\t\tEnter the date:\t\t\t\t'))
                doi=date(y,m,d)
                print('\t\t\tEnter the return date')
                yr=int(input('\t\t\tEnter the year:\t\t\t\t'))
                mr=int(input('\t\t\tEnter the month:\t\t\t'))
                dr=int(input('\t\t\tEnter the date:\t\t\t\t'))
                dor=date(yr,mr,dr)
                duefines=input('\t\t\tEnter the duefines:\t\t\t')
                status=input('\t\t\tEnter the status:\t\t\t')
                for i in range(len(L)):
                    if i==0:
                        g=L[0]
                    elif i==1:
                        h=L[1]
                    elif i==2:
                        j=L[2]
                query="insert into issues_return values(%s,%s,%s,%s,%s,%s,%s)"
                data=(g,h,j,doi,dor,duefines,status)
                cur.execute(query,data)
                con.commit()
                print('\t\t\tBOOK HAS BEEN ISSUED')
                if ch=='no' or ch=='No':
                        print()
def chkbook(bkid):
    query="select status from books where bID='{}'".format(bkid)
    cur.execute(query)
    d=cur.fetchall()#available
    for i in d:
        for k in i:
            if k=='available':
                query ="update books set copies=copies-1where bID='{}'".format(bkid)
                cur.execute(query)
                con.commit()
            elif k=='not available':
                print('\t\t\tBOOK IS NOT AVAILABLE')
                break
        query="select copies from books where bID='{}'".format(bkid)
        cur.execute(query)
        v=cur.fetchall()
        for i in v:
            for k in i:
                if k==0:
                    query="update books set staus='not available'where bID='{}'".format(bkid)
                    cur.execute(query)
                    con.commit()
                elif k!=0:
                    query="update books set status='available' where bID='{}'".format(bkid)
                    cur.execute(query)
                    con.commit()
        
 


def add_issues(bkid):
    from tabulate import tabulate
    from datetime import date
    mem=input('\t\t\tEnter the member ID:\t\t\t')
    query="select memID from members where memID='{}'".format(mem)
    cur.execute(query)
    result=cur.fetchall()
    memberid=mem
    query="select memID,Name,Bookissued,max(returndate),duefines,status from issues_return where memID='{}'".format(memberid)
    cur.execute(query)
    res=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(res,headers=['memID','Name','issued book','return date','duefine','status'],tablefmt='fancy_grid'))
    print()
    print('\t\t\tTERMS AND CONDITIONS')
    print('\t\t\t1.if due fine 0 and pending book can be issued')
    print('\t\t\t2.if due fine is there and pending book cannot be issued until previous one returned')
    print('\t\t\t3.if status returned the book can be issued')
    print()
    print('\t\t\tDo you want continue issuing')
    ch=input('\t\t\tenter yes or no:\t\t\t')
    if ch=='yes' or ch=='Yes':
        chkbook(bkid)
        query="select Name from members where memID='{}'".format(mem)
        cur.execute(query)
        result1=cur.fetchall()
        query="select Title from books where bookID='{}'".format(bkid)
        cur.execute(query)
        result2=cur.fetchall()
        valid=result+result1+result2
        L=[]
        for i in valid:
            for j in i:
                L.append(j)
            print('\t\t\tEnter the issue date')
            y=int(input('\t\t\tEnter the year:\t\t\t\t'))
            m=int(input('\t\t\tEnter the month:\t\t\t'))
            d=int(input('\t\t\tEnter the date:\t\t\t\t'))
            doi=date(y,m,d)
            print('\t\t\tEnter the return date')
            yr=int(input('\t\t\tEnter the year:\t\t\t\t'))
            mr=int(input('\t\t\tEnter the month:\t\t\t'))
            dr=int(input('\t\t\tEnter the date:\t\t\t\t'))
            dor=date(yr,mr,dr)
            duefines=input('\t\t\tEnter the duefines:\t\t\t')
            status=input('\t\t\tEnter the status:\t\t\t')
            for i in range(len(L)):
                if i==0:
                    g=L[0]
                if i==1:
                    h=L[1]
                if i==2:
                    j=L[2]
            query="insert into issues_return values(%s,%s,%s,%s,%s,%s,%s)"
            data=(g,h,j,doi,dor,duefines,status)
            cur.execute(query,data)
            con.commit()
            print('\t\t\tBOOK HAS BEEN ISSUED')
    if ch=='no' or ch=='No':
        print()




def chkbook(bkid):
    query="select status from books where bookID='{}'".format(bkid)
    cur.execute(query)
    d=cur.fetchall()
    for i in d:
        for k in i:
            if k=='available':
                query ="update books set copies=copies-1 where bookID='{}'".format(bkid)
                cur.execute(query)
                con.commit()
            elif k=='not available':
                print('\t\t\tBOOK IS NOT AVAILABLE')
                break
        query="select copies from books where bookID='{}'".format(bkid)
        cur.execute(query)
        v=cur.fetchall()
        for i in v:
            for k in i:
                if k==0:
                    query="update books set staus='not available' where bookID='{}'".format(bkid)
                    cur.execute(query)
                    con.commit()
                elif k!=0:
                    query="update books set status='available' where bookID='{}'".format(bkid)
                    cur.execute(query)
                    con.commit()



def search_isid():
    from tabulate import tabulate
    memid=input('\t\t\tEnter memid to search:\t')
    query="select * from issues_return where memID='{}'".format(memid)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(result,headers=['memID','Name','book issued','issue date','return date','duefines','status'],tablefmt='fancy_grid'))
    else:
        print('\t\t\tNO MATCH FOUND')

        
def search_isstatus():
    from tabulate import tabulate
    stat=input('\t\t\tEnter status to search:\t')
    query="select * from issues_return where status='{}'".format(stat)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(result,headers=['memlD','Name','book issued','issue date','return date','duefines','status'],tablefmt='fancy_grid'))
    else:
        print('\t\t\tNO MATCH FOUND')



def search_issues():
    while True:
        display()
        print('\t\t\tl.SEARCH BY MEMBER ID')
        print('\t\t\t2.SEARCH BY STATUS')
        print('\t\t\t3.RETURN')
        ch=int(input('\t\t\t Enter choice:\t'))
        if ch==1:
            search_isid()
        elif ch==2:
            search_isstatus()
        else:
            break
                


def chkbookreturn(enter_book):
    memid=input('\t\t\tEnter memeber id:\t\t')
    query="select status from issues_return where bookissued='{}'and memid='{}'".format(enter_book,memid)
    cur.execute(query)
    q=cur.fetchall()
    for i in q:
        for k in i:
            if k=='returned':
                query="update books set copies=copies+1 where title='{}'".format(enter_book)
                cur.execute(query)
                con.commit()
            elif k=='pending':
                break




def update_status():
    from tabulate import tabulate
    memid=input('\t\t\tEnter member id whose status to update:\t\t')
    enter_book=input('\t\t\tEnter the book title:\t\t\t\t')
    query="select * from issues_return where memID='{}'and bookissued='{}'".format(memid,enter_book)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(result,headers=['memID','Name','book issued','issue date','return date','duefines','status'],tablefmt='fancy_grid'))
        ch=input('\t\t\tDo you want to update yes/no:\t\t\t')
        if ch=='yes' or ch=='Yes':
            new_status=input('\t\t\tEnter new status:\t\t\t\t')
            query="update issues_return set status='{}' where memID='{}' and Bookissued='{}'".format(new_status,memid,enter_book)
            cur.execute(query)
            con.commit()
            print('\t\t\tRECORD IS UPDATED')
            query="select * from issues_return where memID='{}'and bookissued='{}'".format(memid,enter_book)
            cur.execute(query)
            result=cur.fetchall()
            if cur.rowcount>0:
                print(tabulate(result,headers=['memID','Name','book issued','issue date','return date','duefines','status'],tablefmt='fancy_grid'))
            elif ch=='no' or ch=='No':
                print()
            else:
                print('\t\t\tNO MATCHING RECORD FOUND')




def update_duefine():
    from tabulate import tabulate
    memid=input('\t\t\tEnter member id whose duefines to update:\t\t')
    enter_book=input('\t\t\tEnter the book title:\t\t\t\t')
    query="select * from issues_return where memID='{}'and bookissued='{}'".format(memid,enter_book)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount>0:
        print(tabulate(result,headers=['memID','Name','book issued','issue date','return date','duefines','status'],tablefmt='fancy_grid'))
        ch=input('\t\t\tDo you want to update yes/no:\t\t\t')
        if ch=='yes' or ch=='Yes':
            new_duefine=input('\t\t\tEnter new duefine:\t\t\t\t')
        query="update issues_return set duefines='{}' where memID='{}'and Bookissued='{}'".format(new_duefine,memid,enter_book)
        cur.execute(query)
        con.commit()
        print('\t\t\tRECORD IS UPDATED')
        query="select * from issues_return where memID='{}'and bookissued='{}'".format(memid,enter_book)
        cur.execute(query)
        result=cur.fetchall()
        if cur.rowcount>0:
            print(tabulate(result,headers=['memID','Name','book issued','issue date','return date','duefines','status'],tablefmt='fancy_grid'))
        elif ch=='no' or ch=='No':
            print()
    else:
        print('\t\t\tNO MATCHING RECORD FOUND')


        
def update_issues():
    while True:
        display()
        print('\t\t\t1.UPDATE BY STATUS')
        print('\t\t\t2.UPDATE BY DUEFINES')
        print("\t\t\t3.RETURN")
        ch=int(input('\t\t\t Enter choice:\t'))
        if ch==1:
            update_status()
        elif ch==2:
            update_duefine()
        else:
            break

def reportbk():
    from tabulate import tabulate
    query="select * from books"
    cur.execute(query)
    result=cur.fetchall()
    print(tabulate(result,headers=['bID','title','author','category','publisher','copies','statues'],tablefmt='fancy_grid'))

def reportmem():
    from tabulate import tabulate
    query="select * from members"
    cur.execute(query)
    result=cur.fetchall()
    print(tabulate(result,headers=['memID','Name','gender','gender','address','city','phoneno','EmailID'],tablefmt='fancy_grid'))

def reportsis():
    from tabulate import tabulate
    query="select * from issues_return"
    cur.execute(query)
    result=cur.fetchall()
    print(tabulate(result,headers=['memID','Book issued','issue date','return date','duefines','Status'],tablefmt='fancy_grid'))



def booksmenu():
    while True:
        display()
        print('\t\t\t1.ADD BOOK')
        print('\t\t\t2.SEARCH BOOK')
        print('\t\t\t3.UPDATE BOOK')
        print('\t\t\t4.DELETE BOOK')
        print('\t\t\t5.EXIT')
        ch=int(input('\t\t\t\Enter Choice:\t'))
        print('='*90)
        if ch==1:
              add_bk()
        elif ch==2:
              searchbook_()
        elif ch==3:
              updatebook()
        elif ch==4:
              delete_book()
        elif ch==5:
              break


def membermenu():
    while True:
        display()
        print('\t\t\t1.ADD MEMBER')
        print('\t\t\t2.SEARCH MEMBER')
        print('\t\t\t3.UPDATE MEMBER')
        print('\t\t\t4.DELETE MEMBER')
        print('\t\t\t5.EXIT')
        ch=int(input('\t\t\t\Enter Choice:\t'))
        print('='*90)
        if ch==1:
              add_mem()
        elif ch==2:
              search_mem()
        elif ch==3:
              update_mem()
        elif ch==4:
              deletememid()
        elif ch==5:
              break



def issuemenu():
     while True:
        display()
        print('\t\t\t1.ADD ISSUES/RETURN')
        print('\t\t\t2.SEARCH ISSUES/RETURN')
        print('\t\t\t3.UPDATE ISSUES/RETURN')
        print('\t\t\t4.EXIT')
        ch=int(input('\t\t\t\Enter Choice:\t'))
        print('='*90)
        if ch==1:
            bkid=input('\t\t\tEnter the book id:\t\t\t')
            add_issues(bkid)
        if ch==2:
            search_issues()
        if ch==3:
            update_issues()
        if ch==4:
            break



def reportmenu():
     while True:
        display()
        print('\t\t\t1.BOOKS')
        print('\t\t\t2.MEMBERS')
        print('\t\t\t3.ISSUE RETURN')
        print('\t\t\t4.RETURN')
        ch=int(input('\t\t\t\Enter Choice:\t'))
        if ch==1:
              reportbk()
        elif ch==2:
              reportmem()
        elif ch==3:
              reportsis()
        else:
              break

def mainmenu():
    #this is the main menu
    while True:
        display()
        print('\t\t\t1.BOOKS MENU')
        print('\t\t\t2.MEMBERSHIP MENU')
        print('\t\t\t3.LOANED BOOKS MENU')
        print('\t\t\t4.REPORT MENU')
        print('\t\t\t5.EXIT')
        ch=int(input('\t\t\t\Enter Choice:\t'))
        if ch==1:
            booksmenu()
        elif ch==2:
            membermenu()
        elif ch==3:
            issuemenu()
        elif ch==4:
            reportmenu()
        elif ch==5:
            break
        
mainmenu()




    
