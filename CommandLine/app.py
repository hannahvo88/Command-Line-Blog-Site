import dbcreds
import mariadb

conn = None
cursor = None

print("Username: ")
username= input()

print("Password: ")
user_password= input()

print ("Would you like to write a new post. Please enter 1")
print ("Would you like to see all other posts. Please enter 2")

user_action = input ("Please select your option: ")

while True:
    try:
        conn=mariadb.connect(
                        user=dbcreds.user,
                        password=dbcreds.password,
                        host=dbcreds.host,
                        port=dbcreds.port,
                        database=dbcreds.database
                        )
        cursor = conn.cursor()

        if user_action == "1":
            print("Please write your new post: ")
            post = input()
            cursor.execute("INSERT INTO blog_post (username, content) VALUES (?,?)",[username, post])
            conn.commit()
            print("This is your new post: ")
            print(post)
        elif user_action == "2":
            cursor.execute("SELECT username, content FROM blog_post")
            posts = cursor.fetchall()
            for post in posts:
                print(post)
        else:
            print ("Sorry! Please select your option again")
            print ("Would you like to write a new post. Please enter 1")
            print ("Would you like to see all other posts. Please enter 2")
                
    except mariadb.OperationalError:
        print("There seems to be a connection issue!")
    except mariadb.ProgrammingError:
        print("Apparently you do not know how to code")
    except mariadb.IntergrityError:
        print("Error with DB integrity, most likely consraint failure")
    except:
        print("Opps! Somthing went wrong")

    finally:
        if (cursor != None):
            cursor.close()
        else:
            print("No cursor to begin with.")
        
        if (conn != None):
            conn.rollback()
            conn.close()
        else:
            print("No connection!")
        
    print("Would you like continue?")
    print("Yes = y")
    print("No = n")
    select_option= input()
    if select_option == "y":
        continue
    elif select_option == "n":
        break
    else:
        continue
