import sqlite3


if __name__ == '__main__':

    conn = sqlite3.connect('notebook.sqlite')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS our_notes (id integer primary key autoincrement, note text)')
    length = cursor.execute('SELECT count(*) FROM our_notes').fetchone()[0]

    while True:
        command = input('Введите команду: ').split()

        if command[0] == 'список':
            if length == 0:
                print('Записей пока что нет.')
            else:
                cursor.execute('SELECT * FROM our_notes')
                notes = cursor.fetchall()
                for note in notes:
                    print('{}: {}'.format(note[0], note[1]))

        if command[0] == 'добавить':
            if len(command) < 2:
                print('Не введена запись.')
            else:
                note = ' '.join(command[1:])
                cursor.execute('INSERT INTO our_notes (note) VALUES (?)', (note,))
                conn.commit()
                length += 1
                print('Добавлено.')

        if command[0] == 'удалить':
            if len(command) < 2:
                print('Не введен номер записи.')
            else:
                cursor.execute('DELETE FROM our_notes WHERE id = ?', (int(command[1]),))
                conn.commit()
                length -= 1
                print('Запись удалена.')

        if command[0] == 'выход':
            exit()
