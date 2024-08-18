import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import requests, json
import tkinter
import urllib


HTTP_METHODS = ["GET", "POST", "PUT", "DELETE"]


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"ETL Formatter - {filepath}")  
  

# Define a function to retrieve the response
# and text attribute from the JSON response
def get_zen():

        hostEntry = entry.get()
        contentEntry = content_text.get()
        if method_variable.get() == 'GET':
                response = requests.get(hostEntry).text
                response_info = json.loads(response)
              #  Fact = response_info["fact"]
                txt_edit.delete('1.0',tk.END)
                txt_edit.insert(tk.END, response)
                print(response)
                
        elif method_variable.get() == 'POST':
                {
                "id": 56464,
                "name": "Apple AirPods",
                "data": {
                "generation": "3rd",
                "price": 120
                }
                }

                contentEntry = content_text.get()

                headers = {"content-type": "application/json"}
                print("The content is: ",contentEntry)
                r = requests.post(hostEntry, data=contentEntry, headers=headers).text
                response_info = json.loads(r)
                print(r)
                Fact = r
                txt_edit.delete('1.0',tk.END)
                txt_edit.insert(tk.END, Fact)
                print("THIS WAS A POST METHOD")

        elif method_variable.get() == 'PUT':
                {
                "id":56464,
                "name":"Apple AirPods 2",
                "data":{
                "generation": "4th",
                "price": 125
                }
                 }

                contentEntry = content_text.get()
                headers = {"content-type": "application/json"}
                r = requests.put(hostEntry, data=contentEntry, headers=headers).text
                response_info = json.loads(r)
                print(r)
                Fact = r
                txt_edit.delete('1.0',tk.END)
                txt_edit.insert(tk.END, Fact)
                print("You selected the PUT method")
        elif method_variable.get() == 'DELETE':
            print("You selected the DELETE method")
        else:
            print("Please select a method")
    


window = tk.Tk()
window.title("ETL Formatter")


host = tk.StringVar()


host_frame = tk.Frame()
host_label = tk.Label(host_frame, text="Enter the name of the host: ")
entry = tk.Entry(host_frame,width=30)
entry.config(font="Arial, 10")
entry.grid(row=0, column=1, pady=5, stick="nsew")
method_frame = tk.Frame()
method_label = tk.Label(method_frame, text="Choose an HTTP method: ")
method_variable = tk.StringVar(method_frame)
method_variable.set(HTTP_METHODS[0])
method_menu = tk.OptionMenu(method_frame, method_variable, *HTTP_METHODS)
content_label = tk.Label(text="Write the content of your request")
content_text = tk.Entry(width=90)
content_text.config(font="Arial, 10")
content_text.grid(row=3, column=0 ,pady=5)
response_label = tk.Label(text="Body of the response")
txt_edit = tk.Text(width=50, height=10)
txt_edit.bind("<Key>", lambda _: "break")
txt_edit.config(font="Arial, 12")
txt_edit.grid(row=0, column=1, sticky="nsew")
send_button = tk.Button(text="Send request", command=get_zen)
host_frame.grid(row=0, column=0, pady=5)
host_label.grid(row=0, column=0, pady=5)
method_frame.grid(row=1, column=0, pady=5)
method_label.grid(row=1, column=0, pady=5)
method_menu.grid(row=1, column=1, pady=5)
content_label.grid(row=2, column=0, pady=5)
response_label.grid(row=4, column=0, pady=5)
txt_edit.grid(row=5, column=0, padx=10)
send_button.grid(row=6, column=0, pady=10)


frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(frm_buttons, text="Save Request As...", command=save_file)

btn_open.grid(row=7, column=1)
btn_save.grid(row=8, column=1)

frm_buttons.grid(row=7, column=0)


window.mainloop()
