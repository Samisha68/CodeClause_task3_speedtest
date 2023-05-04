import time

sentance="Rome was not build in a day. We need to practice more!"
print("\t WELCOME TO THE TYPING TEST \n")
print(sentance)

print("Start typing the above sentence \n")


input("Press Enter to Start The typing test \n")

start_time=time.time()
user_input=input()
end_time=time.time()
time_taken=end_time - start_time
print("You took",time_taken,"seconds to type the above sentence \n")