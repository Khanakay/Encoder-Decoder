import tkinter as tk
from main_encoder import encoder 
from main_decoder import decoder 

def encode_it():
    string_to_encode = input1.get(1.0, tk.END)
    encoded_text = encoder(string_to_encode) 
    output1.delete(1.0, tk.END) 
    output1.insert(tk.END, encoded_text)  
    
def decode_it():
    string_to_decode = input2.get(1.0, tk.END)
    decoded_text = decoder(string_to_decode)  
    output2.delete(1.0, tk.END) 
    output2.insert(tk.END, decoded_text)  

root = tk.Tk()
root.title("ENCODER AND DECODER")
root.configure(bg="black")
#root.geometry("1000x650")

frame1 = tk.Frame(root, bg='black',borderwidth=2, relief="solid", padx=10, pady=10)
frame2 = tk.Frame(root, bg='black',borderwidth=2, relief="solid", padx=10, pady=10)

frame1.grid(row=0, column=0, padx=10, pady=10)
frame2.grid(row=0, column=1, padx=10, pady=10)

label1 = tk.Label(frame1,fg='lime' ,bg='black',text="ENTER YOUR PASSWORD BELOW")
label2 = tk.Label(frame2,fg='lime' ,bg='black', text="ENTER ENCODED STRING BELOW")

label1.grid(row=0 ,column=0)
label2.grid(row=0 ,column=0)

input1 = tk.Text(frame1 ,fg='lime',highlightcolor='red' ,bg='black',height=3, width=65)
input2 = tk.Text(frame2 ,fg='lime',highlightcolor='red' ,bg='black',height=20 ,width=65)

input1.grid(row=1 ,column=0, padx=10, pady=10)
input2.grid(row=1 ,column=0, padx=10, pady=10)


button1 = tk.Button(frame1 ,fg='lime',highlightcolor='red' ,bg='black', text="ENCODE IT" ,command=encode_it)
button2 = tk.Button(frame2 ,fg='lime',highlightcolor='red' ,bg='black', text="DECODE IT" ,command=decode_it)

button1.grid(row=2 ,column=0, padx=10, pady=10)
button2.grid(row=2 ,column=0, padx=10, pady=10)

label3 = tk.Label(frame1,fg='lime',highlightcolor='red' ,bg='black', text="ENCODED STRING BELOW")
label4 = tk.Label(frame2,fg='lime',highlightcolor='red' ,bg='black', text="DECODED PASSWORD BELOW")

label3.grid(row=3 ,column=0)
label4.grid(row=3 ,column=0)

output1 = tk.Text(frame1 ,fg='lime',highlightcolor='red' ,bg='black',height=20,width=65)
output2 = tk.Text(frame2 ,fg='lime',highlightcolor='red' ,bg='black',height=3,width=65)

output1.grid(row=5 ,column=0, padx=10, pady=10)
output2.grid(row=5 ,column=0, padx=10, pady=10)

input1.config(insertbackground="red")
output1.config(insertbackground="red")
input2.config(insertbackground="red")
output2.config(insertbackground="red")

root.mainloop()
