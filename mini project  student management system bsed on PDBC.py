import MySQLdb
conn=MySQLdb.connect('localhost','root','root','b46')
curs=conn.cursor()
while True:
    ch=int(input("\n\n enter choice:\n1.add student\t\t2.show all student\n3.update a student\t4.delete a student\n5.sort by student\t6.search by student\n7.exit"))
    match ch:
           case 1:
               print("add a student")
               r=int(input("enter rn:"))
               n=input("enter name:")
               m=float(input("enter marks:"))
               curs.execute(f"insert into student values({r},'{n}',{m})")
               conn.commit()
               print("student added")
           case 2:
               print("show all student")
               curs.execute("select * from student")
               print("rn\tname\tmarks")
               for row in curs:
                    print(row[0],'\t',row[1],'\t',row[2])
           case 3:
               print("update a student")
               
               c=int(input("1. update rn \n2.update  marks"))
               
               match c:
                   case 1:
                       print("update rn")
                       r=int(input("enter rn to update:"))
                       m=float(input("enter updated marks:"))
                       curs.execute(f"update student set rn={r} where marks={m}")
                       if curs.rowcount==0:
                        print("sorry! rn is not updated")
                       conn.commit()
                       print("rn updated")
                   case 2:
                       print("update marks")
                       r=int(input("enter rn to update:"))
                       m=float(input("enter updated marks:"))
                       curs.execute(f"update student set marks={m} where rn={r}")
                       if curs.rowcount==0:
                        print("sorry! marks is not available")
                       conn.commit()
                       print("marks updated")
              
           case 4:
               print("delete a student")
               r=int(input("enter rn to delete:"))
               curs.execute(f"delete from student where rn={r}")
               if curs.rowcount==0:
                        print("sorry! rn is not available")
               conn.commit()
               print("student deleted")
           case 5:
               print("sort by student")
               ch=int(input("1.sort by rn \t2.sort by desc rn\n3.sort by marks \t4.sort ny desc marks\n5.sort by name\t6.sort ny desc name"))
               match ch:
                       case 1:
                           print("sort by rn")
                           curs.execute("select * from student order by rn")
                           print("rn \tname \tmarks")
                           for row in curs:
                                print(row[0],'\t',row[1],'\t',row[2])
                       case 2:
                           print("sort by desc rn")
                           curs.execute("select * from student order by rn desc")
                           print("rn \tname\tmarks")
                           for row in curs:
                               print(row[0],'\t',row[1],'\t',row[2])
                       case 3:
                           print("sort by marks")
                           curs.execute("select * from student order by marks")
                           print("rn \tname \tmarks")
                           for row in curs:
                                print(row[0],'\t',row[1],'\t',row[2])
                       case 4:
                           print("sort by desc marks")
                           curs.execute("select * from student order by marks desc")
                           print("rn \tname\tmarks")
                           for row in curs:
                              print(row[0],'\t',row[1],'\t',row[2])
                       case 5:
                           print("sort by name")
                           curs.execute("select * from student order by name")
                           print("rn \tname \tmarks")
                           for row in curs:
                                print(row[0],'\t',row[1],'\t',row[2])
                       case 6:
                           print("sort by desc name")
                           curs.execute("select * from student order by name desc")
                           print("rn \tname \tmarks")
                           for row in curs:
                               print(row[0],'\t',row[1],'\t',row[2])
           case 6:
               print("search a student")
               ch3=int(input("1.search by rn \t2.search bye name\n3.search by marks"))
               match ch3:
                    
                case 1:
                    print("search by rn")
                    r=int(input("enter rn to search:"))
                    curs.execute(f"select * from student where rn={r}")
                    if curs.rowcount==0:
                        print("sorry! rn is not available")
                    print("rn \tname \ttmarks")
                    for row in curs:
                        print(row[0],'\t',row[1],'\t',row[2])
                case 2:
                    print("search by name")
                    n=input("enter name to search")
                    curs.execute(f"select * from student where name='{n}'")
                    if curs.rowcount==0:
                        print("sorry! name is not available")
                    print("rn \tname \tmarks")
                    for row in curs:
                        print(row[0],'\t',row[1],'\t',row[2])
                case 3:
                    print("search by marks")
                    m=float(input("enter marks to search"))
                    curs.execute(f"select * from student where marks={m}")
                    if curs.rowcount==0:
                        print("sorry! marks is not available")
                    print("rn \tname \tmarks")
                    for row in curs:
                        print(row[0],'\t',row[1],'\t',row[2])
           case 7:
               print("exingting...")
                   
                   
conn.close()

             
             
                
                        
            
                    
        
               
       
                     
               
           
                     
               
           
                     
           
    
