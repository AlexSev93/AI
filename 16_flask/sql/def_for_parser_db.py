import sqlite3

con = sqlite3.connect('C:/Users/Admin/PycharmProjects/AI/16_flask/sql/parser_hh.sqlite', check_same_thread=False)
cur = con.cursor()


def insert_request_info(country, vacancy, key_words):
    regions_db = cur.execute(f"select region from regions")
    regions_db = [region[0] for region in regions_db.fetchall()]
    if country not in regions_db:
        cur.execute(f"insert into regions (region) values ('{country}')")

    cur.execute(f"insert into vacancies (vacancy, region_name) values ('{vacancy}', '{country}')")
    con.commit()

    key_words_db = cur.execute(f"select word from key_words")
    key_words_db = [region[0] for region in key_words_db.fetchall()]
    for word in key_words:
        if word not in key_words_db:
            cur.execute(f"insert into key_words (word) values ('{word}')")
        cur.execute(f"insert into vacancies_key_words (word, vacancy) values ('{word}', '{vacancy}')")
        con.commit()

    con.commit()


def remove_data():
    tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in tables.fetchall()]

    cur.execute("PRAGMA foreign_keys = OFF")
    for table in tables:
        cur.execute(f"delete from {table}")
    cur.execute("PRAGMA foreign_keys = ON")
    con.commit()
    print('Все таблицы очищены')


if __name__ == '__main__':
    pass

