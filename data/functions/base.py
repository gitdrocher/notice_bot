import sqlite3


class Base():
    def add_user(self, user_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            cursor.execute('INSERT OR IGNORE INTO users VALUES (?)',
                           (user_id,)
                           )
            base.commit()

    def add_goal(self, user_id, goal, description):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            cursor.execute('INSERT OR IGNORE INTO goals (id, goal, description) VALUES (?, ?, ?)',
                           (user_id, goal, description)
                           )
            base.commit()

    def add_habit(self, user_id, habit, description):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            cursor.execute('INSERT OR IGNORE INTO habits (id, habit, description) VALUES (?, ?, ?)',
                           (user_id, habit, description)
                           )
            base.commit()

    def add_task(self, user_id, task, description):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            cursor.execute('INSERT OR IGNORE INTO tasks (id, task, description) VALUES (?, ?, ?)',
                           (user_id, task, description)
                           )
            base.commit()


class WatchAction():
    def watch_goals(self, user_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            list = []
            for watch_goals in cursor.execute('SELECT row_id, goal FROM goals WHERE id = ?',
                                              (user_id,)).fetchall():
                list.append(watch_goals)
            return list

    def watch_habits(self, user_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            list = []
            for watch_habits in cursor.execute('SELECT row_id, habit FROM habits WHERE id = ?',
                                               (user_id,)).fetchall():
                list.append(watch_habits)
            return list

    def watch_tasks(self, user_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            list = []
            for watch_tasks in cursor.execute('SELECT row_id, task FROM tasks WHERE id = ?',
                                              (user_id,)).fetchall():
                list.append(watch_tasks)
            return list

    def select_goal_text(self, row_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            var = cursor.execute('SELECT goal, description FROM goals WHERE row_id = ?',
                                 (row_id,)).fetchone()
            return var

    def select_habit_text(self, row_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            var = cursor.execute('SELECT habit, description FROM habits WHERE row_id = ?',
                                 (row_id,)).fetchone()
            return var

    def select_task_text(self, row_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            var = cursor.execute('SELECT task, description FROM tasks WHERE row_id = ?',
                                 (row_id,)).fetchone()
            return var


class ViewedAction():
    def insert_viewed_goal(self, row_id, user_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            cursor.execute('INSERT INTO viewed_goal (row_id, id) VALUES (?, ?)',
                           (row_id, user_id))
            base.commit()

    def select_viewed_goal(self, user_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            viewed_goal = cursor.execute('SELECT row_id FROM viewed_goal WHERE id = ? ORDER BY row_id DESC LIMIT 1',
                                         (user_id,)).fetchone()
            return viewed_goal

    def insert_viewed_habit(self, row_id, user_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            cursor.execute('INSERT INTO viewed_habit(row_id, id) VALUES (?, ?)',
                           (row_id, user_id))
            base.commit()

    def select_viewed_habit(self, user_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            viewed_goal = cursor.execute('SELECT row_id FROM viewed_habit WHERE id = ? ORDER BY row_id DESC LIMIT 1',
                                         (user_id,)).fetchone()
            return viewed_goal

    def insert_viewed_task(self, row_id, user_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            cursor.execute('INSERT INTO viewed_task (row_id, id) VALUES (?, ?)',
                           (row_id, user_id))
            base.commit()

    def select_viewed_task(self, user_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            viewed_goal = cursor.execute('SELECT row_id FROM viewed_task WHERE id = ? ORDER BY row_id DESC LIMIT 1',
                                         (user_id,)).fetchone()
            return viewed_goal


class DeleteAction():
    def delete_goal(self, row_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            cursor.execute('DELETE FROM viewed_goal WHERE row_id = ?',
                           (row_id,))
            cursor.execute('DELETE FROM goals WHERE row_id = ?',
                           (row_id,))
            base.commit()

    def delete_habit(self, row_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            cursor.execute('DELETE FROM viewed_habit WHERE row_id = ?',
                           (row_id,))
            cursor.execute('DELETE FROM habits WHERE row_id = ?',
                           (row_id,))
            base.commit()

    def delete_task(self, row_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            cursor.execute('DELETE FROM viewed_task WHERE row_id = ?',
                           (row_id,))
            cursor.execute('DELETE FROM tasks WHERE row_id = ?',
                           (row_id,))
            base.commit()


class EditAction():
    def edit_goal(self, goal, description, row_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            cursor.execute('UPDATE goals SET goal = ?, description = ? WHERE row_id = ?',
                           (goal, description, row_id))
            base.commit()

    def edit_habit(self, habit, description, row_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            cursor.execute('UPDATE habits SET habit = ?, description = ? WHERE row_id = ?',
                           (habit, description, row_id))
            base.commit()

    def edit_task(self, task, description, row_id):
        with sqlite3.connect('./data/base.db') as base:
            cursor = base.cursor()
            cursor.execute('UPDATE tasks SET task = ?, description = ? WHERE row_id = ?',
                           (task, description, row_id))
            base.commit()
