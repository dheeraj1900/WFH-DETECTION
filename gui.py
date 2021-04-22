import tkinter as tk

def start():
       email=username.get()
       passwd=password.get()
       print(email,passwd)
  

if __name__ == '__main__':

   root = tk.Tk()
   root.title("wfh detection")
   root.geometry("400x400")
   username=tk.Entry()
   username.pack()
   password=tk.Entry()
   password.pack()


   btn=tk.Button(root,text="submit",command=start)
   btn.pack()
   
   root.mainloop()