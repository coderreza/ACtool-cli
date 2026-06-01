print('''
Welcome to the Ac toolbar  :)
to use type __   
              |
              |
              |
        1.    |---------------->  text to voice tool
              |
              |
              |
        2.    |----------------> calculator
              |
              |
              |
        3.    |---------------word counting tool
              |
              |
        4.    |---------------> exit to exit''')
              
while True:
    operation = input("what do you want to do? ")
    if operation == "exit":
        break
    elif operation == "1":
        import tkinter as tk
        import pyttsx3
        from tkinter import messagebox

        engine = pyttsx3.init()
        def get_input():
            # گرفتن متن از اینپوت
            text = entry.get()
                
            if text:  # اگر متن خالی نبود
                engine.say(text)
                engine.runAndWait()  # ⬅️ این خط ضروری است تا صدا پخش شود
            else:
                print("متنی وارد نشده است!")

        # ایجاد پنجره اصلی
        root = tk.Tk()
        root.title("Text to Speech")
        root.geometry("300x200")

        # ایجاد برچسب (Label) برای راهنما
        label = tk.Label(root, text="inter the text: ")
        label.pack(pady=10)

        # ایجاد فیلد ورودی (Entry)
        entry = tk.Entry(root, width=30)
        entry.pack(pady=5)

        # ایجاد دکمه برای ثبت ورودی
        button = tk.Button(root, text="Say",bg="green", command=get_input)
        button.pack(pady=10)
        root.mainloop()
    elif operation == "2":
        import tkinter as tk
        from tkinter import Button
        from tkinter import messagebox
        win = tk.Tk()
        """Open the calculator window."""
        # Use Toplevel instead of Tk for a secondary window
        calc_win = tk.Toplevel(win)
        calc_win.title("ماشین حساب هوشمند")
        calc_win.geometry("300x450")
        calc_win.resizable(False, False)
        calc_win.configure(bg='black')
        
        # Variable to store the expression
        expression = tk.StringVar()

        def press(num):
            """Append number to expression."""
            current = expression.get()
            expression.set(current + str(num))

        def equalpress():
            """Calculate the result."""
            try:
                # Evaluate the expression safely
                # Note: eval() can be dangerous with untrusted input, 
                # but for a simple calculator it's acceptable.
                total = str(eval(expression.get()))
                expression.set(total)
            except ZeroDivisionError:
                messagebox.showerror("خطا", "تقسیم بر صفر مجاز نیست!")
                expression.set("")
            except Exception:
                messagebox.showerror("خطا", "ورودی نامعتبر است!")
                expression.set("")

        def clear():
            """Clear the expression."""
            expression.set("")

        # Display Entry
        display = tk.Entry(calc_win, textvariable=expression, font=('Arial', 24, 'bold'), 
                        justify='right', bd=10, insertbackground='black', bg='#EEE', fg='black')
        display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10, sticky="nsew")

        # Configure grid weights
        for i in range(4):
            calc_win.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            calc_win.grid_rowconfigure(i, weight=1)

        # Button Helper Function
        def create_button(row, col, text, bg_color, command):
            return tk.Button(calc_win, text=text, font=('Arial', 18), height=2, width=5, 
                            command=command, bg=bg_color, fg="white")

        # Row 1
        btn7 = create_button(1, 0, "7", "#333333", lambda: press(7))
        btn7.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        btn8 = create_button(1, 1, "8", "#333333", lambda: press(8))
        btn8.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        btn9 = create_button(1, 2, "9", "#333333", lambda: press(9))
        btn9.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        btn_div = create_button(1, 3, "/", "#FF9500", lambda: press('/'))
        btn_div.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

        # Row 2
        btn4 = create_button(2, 0, "4", "#333333", lambda: press(4))
        btn4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        btn5 = create_button(2, 1, "5", "#333333", lambda: press(5))
        btn5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
        btn6 = create_button(2, 2, "6", "#333333", lambda: press(6))
        btn6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
        btn_mul = create_button(2, 3, "*", "#FF9500", lambda: press('*'))
        btn_mul.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

        # Row 3
        btn1 = create_button(3, 0, "1", "#333333", lambda: press(1))
        btn1.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        btn2 = create_button(3, 1, "2", "#333333", lambda: press(2))
        btn2.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
        btn3 = create_button(3, 2, "3", "#333333", lambda: press(3))
        btn3.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
        btn_add = create_button(3, 3, "+", "#FF9500", lambda: press('+'))
        btn_add.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

        # Row 4
        btn0 = create_button(4, 0, "0", "#333333", lambda: press(0))
        btn0.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        btn_dot = create_button(4, 1, ".", "#333333", lambda: press('.'))
        btn_dot.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        btn_clear = create_button(4, 2, "C", "#AAAAAA", clear)
        btn_clear.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
        btn_sub = create_button(4, 3, "-", "#FF9500", lambda: press('-'))
        btn_sub.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

        # Row 5
        btn_equal = create_button(5, 0, "=", "#00C800", equalpress)
        btn_equal.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
    elif operation == "3":
        text = input("inter the text: ")
        words = text.split(" ")
        print(f"the text had {len(words)} words")
    elif operation == "help":
        print('''
to use type __   
              |
              |
              |
              |--------------->  textvoice for text to voice tool
              |
              |
              |
              |--------------->  calc for calculator
              |
              |
              |--------------->wordC for word count tool
              |
              |
              |---------------> exit to exit
              |
              |
              |---------------> help to help''')
    elif operation == "help --help":
        print("I have nothing to help you with (:")
