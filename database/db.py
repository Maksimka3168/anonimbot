import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def check_user_search_await(self, user_id):
        """
        Проверка пользователя в поиске(ожидание)
        :param user_id:
        :return:
        """
        with self.connection:
            result = self.cursor.execute(
                "SELECT * FROM `search` WHERE `user_id_2` = (?) OR `user_id_1` = (?)").fetchone()
            return result

    def check_available_user(self, user_id):
        """
        Проверка пользователя на регистрацию
        :param user_id:
        :return: False - если пользователь не зарегистрирован
                 True - если пользователь зарегистрирован
        """
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = (?)", (user_id,)).fetchone()
            if result is None:
                return False
            else:
                return True

    def check_available_search_user(self, user_id):
        """
        Проверка пользователя на допуск к поиску
        :param user_id:
        :return: False - если пользователь не в поиске
                 True - если пользователь в поиске
        """
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `search` WHERE `user_id_1` = (?) OR `user_id_2` = (?)",
                                         (user_id, user_id,)).fetchone()
            if result is None:
                return False
            else:
                return True

    def check_available_talk(self, user_id):
        """
        Проверка, есть ли у пользователя собеседник
        :param user_id:
        :return:
        """
        result = self.cursor.execute("SELECT * FROM `search` WHERE (`user_id_1` = (?) AND `user_id_2` IS NOT NULL) "
                                     "OR "
                                     "(`user_id_2` = (?) AND `user_id_1` IS NOT NULL)",
                                     (user_id, user_id,)).fetchone()
        if result is None:
            return False
        else:
            return True

    def check_available_dialogue_user(self, user_id):
        """
        Получение ID собеседника
        :param user_id:
        :return:
        """
        with self.connection:
            user_id_answer = self.cursor.execute("SELECT CASE "
                                                 "WHEN user_id_2 = (?) THEN user_id_1 "
                                                 "WHEN user_id_1 = (?) THEN user_id_2 "
                                                 "END AS result "
                                                 "FROM `search`", (user_id, user_id, )).fetchone()
            print(user_id_answer)
            return user_id_answer

    def get_all_users_search(self):
        """
        Получение списка пользователей, находящихся в поиске
        :return: list
        """
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `search` WHERE `user_id_2` IS NULL OR `user_id_1` IS NULL").fetchall()
            return result

    def add_search_await(self, user_id):
        """
        Добавление пользователя в ожидании поиска
        :param user_id:
        :return:
        """
        with self.connection:
            self.cursor.execute(f"INSERT INTO `search` VALUES ((?), NULL)",
                                (user_id,))

    def add_companion_user(self, user_id_1, user_id_2):
        """
        Добавление пользователя в беседу
        :param user_id_1:
        :param user_id_2:
        :return:
        """
        with self.connection:
            self.cursor.execute("UPDATE `search` "
                                "SET user_id_1 = CASE "
                                "WHEN user_id_2 = (?) THEN (?) "
                                "ELSE user_id_1 "
                                "END, "
                                "user_id_2 = CASE "
                                "WHEN user_id_1 = (?) THEN (?) "
                                "ELSE user_id_2 "
                                "END "
                                "WHERE user_id_1 = (?) OR user_id_2 = (?)", (user_id_1, user_id_2, user_id_1, user_id_2, user_id_1, user_id_1, ))

    def delete_companion_user(self, user_id):
        """
        Удаление пользователя из беседы
        :param user_id:
        :return:
        """
        with self.connection:
            self.cursor.execute("UPDATE `search` "
                                "SET user_id_1 = CASE "
                                "WHEN user_id_1 = (?) THEN NULL "
                                "ELSE user_id_1 "
                                "END, "
                                "user_id_2 = CASE "
                                "WHEN user_id_2 = (?) THEN NULL "
                                "ELSE user_id_2 "
                                "END "
                                "WHERE user_id_1 = (?) OR user_id_2 = (?)", (user_id, user_id, user_id, user_id,))
            self.cursor.execute("DELETE FROM `search` WHERE user_id_1 IS NULL AND user_id_2 IS NULL")

    def get_info_messaging(self, user_id):
        with self.connection:
            result = self.cursor.execute(f"SELECT * FROM `search` WHERE user_id_1 = (?) OR user_id_2 = (?)", (user_id, user_id, ))
            return result

    def register_user(self, user_id, username, name):
        """
        Регистрация пользователя в базе данных
        :param user_id: user_id пользователя
        :param username: username пользователя
        :param name: name пользователя
        :return:
        """
        with self.connection:
            self.cursor.execute(f"INSERT INTO `users` VALUES ((?), (?), (?))",
                                (user_id, username, name,))

    def get_info_user(self, user_id):
        """
        Получение полной информации о пользователе из базы данных
        :param user_id:
        :return:
        """
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = (?)", (user_id,)).fetchone()
            return result

