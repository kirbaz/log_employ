from flask import Flask, render_template, request, redirect, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'my_secret_key'  # Используйте более сложный ключ в рабочем коде

DATABASE = 'employee_log.db'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        full_name = request.form['full_name']
        action = request.form['action']
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rating = request.form['rating']

        conn = get_db_connection()
        conn.execute('INSERT INTO actions (full_name, action, date, rating) VALUES (?, ?, ?, ?)',
                     (full_name, action, date, rating))
        conn.commit()
        conn.close()

        flash('Запись успешно добавлена!')
        return redirect('/')

    return render_template('index.html')


@app.route('/log')
def log():
    conn = get_db_connection()
    actions = conn.execute('SELECT * FROM actions').fetchall()
    conn.close()

    return render_template('log.html', actions=actions)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    action = conn.execute('SELECT * FROM actions WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        new_rating = request.form['rating']
        new_note = request.form['note']  # Получаем новое примечание
        conn.execute('UPDATE actions SET rating = ?, note = ? WHERE id = ?', (new_rating, new_note, id))
        conn.commit()
        conn.close()
        flash('Запись успешно обновлена!')
        return redirect('/log')

    conn.close()
    return render_template('edit.html', action=action)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
