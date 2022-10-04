

class InfoMessage:
    """Информационное сообщение о тренировке"""
    def __init__(self,
        training_type: str,
        duration: float,
        distance: float,
        speed: float,
        calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type};'
                f' Длительность: {self.duration:.3f} ч.;'
                f' Дистанция: {self.distance:.3f} км;'
                f' Ср. скорость: {self.speed:.3f} км/ч;'
                f' Потрачено ккал: {self.calories:.3f}.')
        

class Training:
    """Базовый класс тренировки"""
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    def __init__(self, action: int,
                 duration: float,
                 weight: float):
        self.action = action
        self.duration = duration
        self.weight = weight         
    def get_distance(self):
        return self.action * self.LEN_STEP() / self.M_IN_KM
    def get_mean_speed(self):
        return self.get_distance() / self.duration
    def get_spent_calories():
        pass
    def show_training_info(self):
        return InfoMessage

class Running(Training):
    """Тренировка: Бег."""
    def 

if __name__ == '__main__':
    packages = [        
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training) 