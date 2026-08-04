# # Os Modules


# # import os()
# # when you delete a file firts you write (import os) without it cause error
# os.remove("students.txt")#NameError: name 'os' is not defined



# # os.remove()
# #File ko permanently delete karna.agr file na ho error ay ga
# import os
# os.remove("students.txt")# pc mese student.txt file delete ho jay gi
# # error na ya isi lia hm pahle maloom karen gy k file exist krti he k nahi
# import os
# if os.path.exists("students.txt"):
#     os.remove("students.txt")
#     print("File deleted.")
# else:
#     print("File not found.")




# # os.rename()
# # Kisi file ya folder ka naam change karna.
# import os
# os.rename("stydent.txt", "student.py")
# # yaha pehla wala old name and bd wala new name raken gy





# # os.path.exists()
# # Check karna ke file ya folder exist karta hai ya nahi.return true or false
# import os
# print(os.path.exists("students.txt"))
# # if k sarh kese use hoga
# import os
# if os.path.exists("students.txt"):
#     print("File found.")
# else:
#     print("File not found.")




# # os.mkdir()
# # new folder create karna 
# import os
# os.mkdir("Day10")
# # if k sath use
# import os
# if not os.path.exists("Day3"):
#     os.mkdir("Day3")
#     print("Folder created.")
# else:
#     print("Folder already exists.")



# # os.rmdir()
# # use for delete folder
# import os
# os.rmdir("Projects")





# # os.listdir()
# # Kisi folder ke andar jitni files aur folders hain, unki list dena.
# import os
# print(os.listdir("Day1"))












































































































