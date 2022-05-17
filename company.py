from timeit import repeat
from turtle import clear
from window import Window
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from child_window import Child_window
from client import Client


class Company:
    def __init__(self) -> None:
        self.name = "Creditime"
        self.window = Window(self.name, 500, 500, 800, 250, "icon/creditime.ico", (True, True))
        self.clientt = Client()

    def main_win_vidgets(self):
        top_frame = Frame(self.window.root)
        bottom_frame = Frame(self.window.root)
        top_frame.pack()
        bottom_frame.pack()
        Label(top_frame, text="Компания CREDITIME", relief=RAISED, bd=3, font=("", 18), padx=10).pack(side=LEFT, pady=(100, 20))
        font_size = 12
        Button(bottom_frame, text="Войти в аккаунт", command="Входим в аккаунт", font=("", font_size)).pack(side=LEFT, padx=(0, 10))
        Button(bottom_frame, text="Регистарция", command=self.registration, font=("", font_size)).pack(side=LEFT)

    # def menu(self):
    # Label(self.window.root, text="Компания CREDITIME", relief=RAISED, bd=3, font=("JetBrains Mono", 16)).
    # font_size = 12
    # Button(self.window.root, text="Войти в аккаунт", command="Входим в аккаунт", font=("", font_size)).pack()
    # Button(self.window.root, text="Регистарция", command=self.registration, font=("", font_size)).pack()

    def registration(self):
        self.window.root.withdraw()
        regis = Child_window(self.window.root, "Регистрация", 500, 500, 800, 250, "icon/registration.ico")
        regis.root.protocol(
            "WM_DELETE_WINDOW",
            lambda this_window=regis: self.exit(this_window, "Выйти?"),
        )
        # Вернуться в меню
        Label(regis.root, text=f"Создание аккаунта в {self.name}", relief=RAISED, bd=3, font=("", 18), padx=10).place(
            relx=0.5,
            rely=0.1,
            anchor=CENTER,
        )  # Заголовок

        Label(regis.root, text="Имя").place(relx=0.337, rely=0.2, anchor=CENTER)
        first_name = Entry(regis.root)
        first_name.place(relx=0.5, rely=0.2, anchor=CENTER)  # first name
        Label(regis.root, text="Фамилия").place(relx=0.31, rely=0.25, anchor=CENTER)
        last_name = Entry(regis.root)
        last_name.place(relx=0.5, rely=0.25, anchor=CENTER)  # last name
        Label(regis.root, text="email").place(relx=0.33, rely=0.30, anchor=CENTER)
        email = Entry(regis.root)
        email.place(relx=0.5, rely=0.30, anchor=CENTER)  # email
        Label(regis.root, text="Пароль").place(relx=0.32, rely=0.35, anchor=CENTER)
        password = Entry(regis.root, show="*")
        password.place(relx=0.5, rely=0.35, anchor=CENTER)  # password
        Label(regis.root, text="Повторите пароль").place(relx=0.26, rely=0.40, anchor=CENTER)
        repeat_password = Entry(regis.root, show="*")
        repeat_password.place(relx=0.5, rely=0.40, anchor=CENTER)  # repeat_pass
        Label(regis.root, text="Телефон: +380").place(relx=0.282, rely=0.45, anchor=CENTER)
        phone = Entry(regis.root)
        phone.place(relx=0.5, rely=0.45, anchor=CENTER)  # phone
        Label(regis.root, text="Возраст").place(relx=0.315, rely=0.50, anchor=CENTER)
        age = Spinbox(regis.root, from_=18, to=60, width=4)
        age.place(relx=0.414, rely=0.50, anchor=CENTER)
        Button(regis.root, text="Очистить поля", command=lambda: self.clear(first_name, last_name, email, password, repeat_password, phone, age)).place(
            relx=0.55, rely=0.50, anchor=CENTER
        )
        Button(regis.root, text="Зарегистрироваться", command=lambda: self.get_info(first_name, last_name, email, password, repeat_password, phone, age)).place(
            relx=0.33, rely=0.58, anchor=CENTER
        )
        question = "Отменить регистрацию и вернуться в меню?"
        Button(
            regis.root,
            text="Вернуться в меню",
            command=lambda this_window=regis: self.close_window(this_window, question),
        ).place(relx=0.63, rely=0.58, anchor=CENTER)
        

    def clear(self, fname=Entry, lname=Entry, email=Entry, password=Entry, repeat_password=Entry, phone=Entry, age=Spinbox):
        fname.delete(0, END)
        lname.delete(0, END)
        email.delete(0, END)
        password.delete(0, END)
        repeat_password.delete(0, END)
        phone.delete(0, END)
        age.delete(0, END)

    def get_info(self, fname=Entry, lname=Entry, email=Entry, password=Entry, repeat_password=Entry, phone=Entry, age=Spinbox):
        if fname.get() != "" and lname.get() != "" and email.get() != "" and password.get() != "" and repeat_password.get() != "" and phone.get() != "" and age.get() != "":
            # check email========================
            # TODO: Сделать проверку на повторение почты в базе
            email_str = str(email.get())
            correct_email = False
            unValidSumbol = "-+!@#$%^&*()|\?/<>~\"'"
            for i in range(len(email_str)):
                if email_str[0] == "@":
                    correct_email = False
                    break
                else:
                    if email_str[i] == "@":
                        symbol = email_str[:i]
                        if self.check_email(symbol, unValidSumbol) == True:
                            messagebox.showwarning("Символы", "Могут использоваться символы (a-z), цифры (0-9) и точку.")
                            return
                        if len(symbol) < 6:
                            print(symbol)
                            break
                        elif len(symbol) >= 8:
                            alphaValid = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                            alphaValid += alphaValid.lower()
                            if self.check_email(symbol, alphaValid) == False:
                                break
                        if email_str[i + 1 :] == "gmail.com" or email_str[i + 1 :] == "mail.ru" or email_str[i + 1 :] == "yandex.ru":
                            correct_email = True
                            break
                    else:
                        correct_email = False
            if correct_email == False:
                messagebox.showerror("Не корректные данные", "Не правильная почта!")
                return
            # ===================================
            # Check password
            if len(password.get()) < 4:
                messagebox.showwarning("Пароль", "Пароль должен содержать минимум 4 символа")
                return
            if password.get() != repeat_password.get():
                messagebox.showwarning("Предупреждение", "Пароли не совпадают!")
                return
            # ====================================
            # check phone
            validSymbols = "1234567890"
            if not self.check_phone(phone.get(), validSymbols):
                messagebox.showwarning("Телефон", "Не корректный номер телефона")
                return
            # =====================================
            # check age
            str_age = age.get()
            print("age type", type(str_age))
            for val in str_age:
                if not (val in validSymbols):
                    messagebox.showerror("Ошибка", "Введены не корректные данные!")
                    return
            if int(str_age) < 18 or int(str_age) > 60:
                messagebox.showwarning("Возрастные ограничения", "Наша компанию обслуживает людей возрастом от 18 до 60 лет включительно!")
                return
            # =====================================
            messagebox.showinfo("Успех", "Поздравляю вы зарегистрировались!")
        else:
            messagebox.showwarning("Данные", "Не все данные заполнены!")

    def exit(self, this_window, question):
        if messagebox.askokcancel("Потвердите закрытие окна", question):
            self.window.root.deiconify()
            this_window.root.destroy()
            self.window.root.destroy()  # Потом убрать возможно!

    def close_window(self, this_window, question):
        if messagebox.askyesno("Закрыть окно регистрации", question):
            self.window.root.deiconify()
            this_window.root.destroy()

    def run(self):
        self.main_win_vidgets()
        self.window.run()

    def check_phone(self, testS=str, validSymbols=str()):
        flag = True
        if len(testS) < 9:
            return False
        for val in testS:
            if not (val in validSymbols):
                flag = False
                break
        if flag == True:
            return True
        else:
            return False

    def check_email(self, testS=str, validSymbols=str()):
        flag = False
        for val in testS:
            if val in validSymbols:
                flag = True
                break
        if flag == True:
            return True
        else:
            return False
