import sqlite3

database = sqlite3.connect("clients.db")
cursor = database.cursor()
# TODO: В будущем добавить баланс пользователя скорей всего это будет карта которую он сможет окрыть
cursor.execute(f"""CREATE TABLE IF NOT EXISTS users (
{id} INTENGET PRIMARY KEY,
{first_name} VARCHAR(30),
{last_name} VARCHAR(30),
{email} VARCHAR,
{password} VARCHAR,
{phone} INT,
{age} INT,
{work_place} VARCHAR,
{work_position} VARCHAR,
{salary} VARCHAR NOT NULL DEFAULT 0,
{credit} VARCHAR NOT NULL DEFAULT 0,
{sum_use_credit} VARCHAR NOT NULL DEFAULT 0,
{credit_days = INT NOT NULL DEFAULT 0
)""")
database.commit()
cursor.close()
database.close()
