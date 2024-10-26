from flask import Flask, render_template, request, redirect
import pymysql
app = Flask(__name__)

conn = pymysql.connect(
    host= "localhost", user = "root", passwd = "A141983", db = "TO_DO_APP")
cursor = conn.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT id, task, done FROM tasks")  # Fetch tasks from database
    tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)  # Pass tasks to the template


@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
    conn.commit()
    return redirect('/')

@app.route('/done/<int:id>', methods=['POST'])
def mark_done(id):
    cursor.execute("UPDATE tasks SET done = TRUE WHERE id = %s", (id,))
    conn.commit()
    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
    conn.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
