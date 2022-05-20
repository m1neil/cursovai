from window import Window
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from child_window import Child_window
from client import Client
import sqlite3
import hashlib


class Company:
    def __init__(self) -> None:
        self.name = "Creditime"
        self.window = Window(self.name, 500, 500, 800, 250, "icon/creditime.ico", (True, True))
        self.clientt = Client()
        self.database = sqlite3.connect("clients.db")
        self.cursor = self.database.cursor()
        self.user = Client()
        # TODO: В будущем добавить баланс пользователя скорей всего это будет карта которую он сможет окрыть
        query = """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            email VARCHAR,
            password VARCHAR,
            phone VARCHAR(13),
            age INT,
            work_place VARCHAR,
            work_position VARCHAR,
            salary FLOAT NOT NULL DEFAULT 0,
            credit FLOAT NOT NULL DEFAULT 0,
            sum_use_credit FLOAT NOT NULL DEFAULT 0,
            credit_days INT NOT NULL DEFAULT 0,
            regular_client INT NOT NULL DEFAULT 0
            )"""
        self.database.execute(query)
        self.database.commit()
        self.cursor.close()
        self.database.close()

    def run(self):
        self.main_win_fidgets()
        self.window.run()

    def main_win_fidgets(self):
        top_frame = Frame(self.window.root)
        bottom_frame = Frame(self.window.root)
        top_frame.pack()
        bottom_frame.pack()
        Label(top_frame, text="Компания CREDITIME", relief=RAISED, bd=3, font=("", 18), padx=10).pack(side=LEFT, pady=(100, 20))
        font_size = 12
        Button(bottom_frame, text="Войти в аккаунт", command=self.comeInAccount, font=("", font_size)).pack(side=LEFT, padx=(0, 10))
        Button(bottom_frame, text="Регистарция", command=self.registration, font=("", font_size)).pack(side=LEFT)

    def comeInAccount(self):
        comeInAcc = Child_window(self.window.root, "Вход в аккаунт", 500, 500, 700, 250, "icon/comeToAcc.ico")
        title_frame = Frame(comeInAcc.root)
        title_frame.pack()
        Label(title_frame, text=f"Войти в {self.name}", relief=RAISED, bd=3, font=("", 18), padx=30).pack(side=LEFT, pady=(30, 35))

        label_phone_or_email = Frame(comeInAcc.root)
        label_phone_or_email.pack()
        Label(label_phone_or_email, text="Введите почту или телефон", font=("", 12), padx=10).pack(side=LEFT, pady=(0, 10))

        entry_phone_or_email_frame = Frame(comeInAcc.root)
        entry_phone_or_email_frame.pack()
        input_phone_or_email = Entry(entry_phone_or_email_frame, width=30, font=("", 10))
        input_phone_or_email.pack(side=LEFT, pady=(0, 10))

        label_password_frame = Frame(comeInAcc.root)
        label_password_frame.pack()
        Label(label_password_frame, text="Пароль", font=("", 12)).pack(side=LEFT, pady=(0, 10))

        entry_password_frame = Frame(comeInAcc.root)
        entry_password_frame.pack()
        input_password = Entry(entry_password_frame, width=30, font=("", 10), show="*")
        input_password.pack(side=LEFT, pady=(0, 10))

        btn_submit_frame = Frame(comeInAcc.root)
        btn_submit_frame.pack()
        Button(btn_submit_frame, text="Войти", font=("", 12), width=12, command=lambda: self.check_input_data(input_phone_or_email, input_password, comeInAcc)).pack(side=LEFT)
        comeInAcc.focus()

    def check_input_data(self, input_phone_or_email=Entry, input_password=Entry, child_window=Child_window):
        examination = False
        user_id = None
        if input_phone_or_email.get() != "":
            if input_password.get() != "":
                try:
                    self.database = sqlite3.connect("clients.db")
                    self.cursor = self.database.cursor()
                    self.database.create_function("md5", 1, self.md5sum)
                    email = ""
                    phone = ""
                    if input_phone_or_email.get()[0] == "+":
                        self.cursor.execute("SELECT phone FROM users WHERE phone = ?", [input_phone_or_email.get()])
                        phone = input_phone_or_email.get()
                    else:
                        self.cursor.execute("SELECT email FROM users WHERE email = ?", [input_phone_or_email.get()])
                        email = input_phone_or_email.get()
                    if self.cursor.fetchone() is None:
                        messagebox.showwarning("Логин", "Такого логина не существует")
                    else:
                        self.cursor.execute(
                            "SELECT password FROM users WHERE email = ? AND password = md5(?) OR phone = ? AND password = md5(?)",
                            [email, input_password.get(), phone, input_password.get()],
                        )
                        if self.cursor.fetchone() is None:
                            messagebox.showwarning("Пароль", "Не верный пароль!")
                        else:
                            messagebox.showinfo("Успех", "Вы успешно вошли в свой аккаунт!")
                            user_id = self.cursor.execute("SELECT id FROM users WHERE email = ? OR phone = ?", [email, phone]).fetchone()[0]
                            examination = True
                except sqlite3.Error as er:
                    print(er.with_traceback())
                    messagebox.showerror("Ошибка!", "При работе с базой данный случилась не предвиденная ошибка!")
                finally:
                    self.cursor.close()
                    self.database.close()
            else:
                messagebox.showwarning("Пароль", "Введите пароль!")
        else:
            messagebox.showwarning("Предупреждение", "Введите логин!")

        if examination == True:
            self.simple_close_window(child_window)
            self.client_area(user_id)

    # TODO:========================================================================================================================

    def client_area(self, user_id):
        try:
            self.database = sqlite3.connect("clients.db")
            self.cursor = self.database.cursor()
            self.user.set_id(user_id)
            self.user.set_fname(self.cursor.execute("SELECT first_name FROM users WHERE id = ?", [user_id]).fetchone()[0])
            self.user.set_lname(self.cursor.execute("SELECT last_name FROM users WHERE id = ?", [user_id]).fetchone()[0])
            self.user.set_email(self.cursor.execute("SELECT email FROM users WHERE id = ?", [user_id]).fetchone()[0])
            self.user.set_password(self.cursor.execute("SELECT password FROM users WHERE id = ?", [user_id]).fetchone()[0])
            self.user.set_phone(self.cursor.execute("SELECT phone FROM users WHERE id = ?", [user_id]).fetchone()[0])
            self.user.set_age(self.cursor.execute("SELECT age FROM users WHERE id = ?", [user_id]).fetchone()[0])
            self.user.set_work_place(self.cursor.execute("SELECT work_place FROM users WHERE id = ?", [user_id]).fetchone()[0])
            self.user.set_work_position(self.cursor.execute("SELECT work_position FROM users WHERE id = ?", [user_id]).fetchone()[0])
            self.user.set_salary(self.cursor.execute("SELECT salary FROM users WHERE id = ?", [user_id]).fetchone()[0])
            self.user.set_credit(self.cursor.execute("SELECT credit FROM users WHERE id = ?", [user_id]).fetchone()[0])
            self.user.set_sum_use_credit(self.cursor.execute("SELECT sum_use_credit FROM users WHERE id = ?", [user_id]).fetchone()[0])
            self.user.set_credit_days(self.cursor.execute("SELECT credit_days FROM users WHERE id = ?", [user_id]).fetchone()[0])
            self.user.set_regula_client(self.cursor.execute("SELECT regular_client FROM users WHERE id = ?", [user_id]).fetchone()[0])     
        except sqlite3.Error as er:
            print(er.with_traceback())
            messagebox.showerror("Ошибка!", "При работе с базой данный случилась не предвиденная ошибка!")
        finally:
            self.cursor.close()
            self.database.close()
        self.window.root.withdraw() #! Когда будем выходить из аккаунта не забыть включить главное окно
        client_area_window = Child_window(self.window.root, "Пользовательский кабинет", 500, 500, 800, 250, "icon/registration.ico")
        client_area_window.root.protocol(
            "WM_DELETE_WINDOW",
            lambda this_window=client_area_window: self.exit(this_window, "Закрыть программу?"),
        )
    # TODO:========================================================================================================================

    def registration(self):
        self.window.root.withdraw()
        regis = Child_window(self.window.root, "Регистрация", 500, 500, 800, 250, "icon/registration.ico")
        regis.root.protocol(
            "WM_DELETE_WINDOW",
            lambda this_window=regis: self.exit(this_window, "Закрыть программу?"),
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
        title = "Закрыть окно регистрации"
        question = "Отменить регистрацию и вернуться в меню?"
        Button(
            regis.root,
            text="Вернуться в меню",
            command=lambda this_window=regis: self.close_window(this_window, title, question),
        ).place(relx=0.63, rely=0.58, anchor=CENTER)


  

