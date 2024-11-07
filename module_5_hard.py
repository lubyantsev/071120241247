import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()  # Хэширование пароля
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration  # Продолжительность в секундах
        self.time_now = 0  # Текущая секунда воспроизведения
        self.adult_mode = adult_mode  # Ограничение по возрасту


class UrTube:
    def __init__(self):
        self.users = []  # Список объектов User
        self.videos = []  # Список объектов Video
        self.current_user = None  # Текущий пользователь

    def log_in(self, nickname, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = user
                print(f"Добро пожаловать, {nickname}!")
                return
        print("Неверный логин или пароль.")

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует.")
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован.")

    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта.")

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, query):
        return [video.title for video in self.videos if query.lower() in video.title.lower()]

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((v for v in self.videos if v.title == title), None)
        if video is None:
            print("Видео не найдено")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Воспроизведение видео '{video.title}'...")
        for i in range(1, video.duration + 1):
            print(f"{i} сек.")
            time.sleep(1)  # Пауза в 1 секунду
        video.time_now = 0  # Сброс текущего времени просмотра
        print("Конец видео")


# Пример проверки
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')  # Войдите в аккаунт, чтобы смотреть видео
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')  # Вам нет 18 лет, пожалуйста покиньте страницу
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')  # Воспроизведение видео...

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)  # Пользователь vasya_pupkin уже существует.
print(ur.current_user.nickname)  # urban_pythonist