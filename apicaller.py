from tkinter import *
import urllib


HTTP_METHODS = ["GET", "POST", "PUT", "DELETE"]


class HttpGuiApplication(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("HTTP GUI Client")
        self.host_frame = Frame(self)
        self.host_label = Label(self.host_frame, text="Enter the name of the host: ")
        self.host_entry = Entry(self.host_frame, width=40)
        self.host_entry.insert(0, "http://")
        self.method_frame = Frame(self)
        self.method_label = Label(self.method_frame, text="Choose an HTTP method: ")
        self.method_variable = StringVar(self.method_frame)
        self.method_variable.set(HTTP_METHODS[0])
        self.method_menu = OptionMenu(self.method_frame, self.method_variable, *HTTP_METHODS)
        self.content_label = Label(self, text="Write the content of your request")
        self.content_text = Text(self, width=50, height=10)
        self.response_label = Label(self, text="Body of the response")
        self.response_text = Text(self, width=50, height=10)
        self.response_text.bind("<Key>", lambda _: "break")
        self.send_button = Button(self, text="Send request", command=self.send_request)
        self.grid_widgets()
        
    def grid_widgets(self):
        self.host_frame.grid(row=0, column=0, pady=5)
        self.host_label.grid(row=0, column=0, pady=5)
        self.host_entry.grid(row=0, column=1, pady=5)
        
        self.method_frame.grid(row=1, column=0, pady=5)
        self.method_label.grid(row=1, column=0, pady=5)
        self.method_menu.grid(row=1, column=1, pady=5)
        
        self.content_label.grid(row=2, column=0, pady=5)
        self.content_text.grid(row=3, column=0, padx=10)
        
        self.response_label.grid(row=4, column=0, pady=5)
        self.response_text.grid(row=5, column=0, padx=10)
        
        self.send_button.grid(row=6, column=0, pady=10)

    def send_request(self):
        try:
            self._send_request()
        except urllib.HTTPError:
            print("Something went wrong!")

    def _send_request(self):
        host = self.host_entry.get()
        method = self.method_variable.get()
        kwarg = {}
        if method != "GET":
            kwarg['data'] = self.content_text.get(1.0, "end")
        opener = urllib.build_opener(urllib.HTTPHandler)
        request = urllib.Request(host, **kwarg)
        request.get_method = lambda: method
        url = opener.open(request)
        self.response_text.delete(1.0, "end")
        self.response_text.insert("end", url.read())


if __name__ == "__main__":
    app = HttpGuiApplication()
    app.mainloop()