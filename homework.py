

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
    MINUTES_IN_HOUR = 60
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
    coeff_calorie_1 = 18
    coeff_calorie_2 = 20
    def get_spent_calories(self) -> float:
        callories = (self.coeff_calorie_1 * self.speed - self.coeff_calorie_2) * self.weight / self.M_IN_KM * self.duration

class SportWalking(Training):
    """Тренировка: Спортивная ходьба."""
    height: float
    coeff_calorie_1 = 0.035
    coeff_calorie_2 = 2
    coeff_calorie_3 = 0.029
    def get_spent_calories(self) -> float:
        self.callories = (self.coeff_calorie_1 * self.weight + (self.speed**self.coeff_calorie_2 // self.height) * self.coeff_calorie_3 * self.weight) * self.MINUTES_IN_HOUR

class Swimming(Training):
    """Тренировка: Плавание."""
    LEN_STEP = 1.38
    def __init__ (self, length_pool: float,
                 count_pool: float):
        self.length_pool = length_pool
        self.count_pool = count_pool
    coeff_calorie_1 = 1.1
    coeff_calori_2 = 2
    def get_spent_calories(self) -> float:
        self.callories = (self.speed + self.coeff_calorie_1) * self.coeff_calorie_2 * self.weight
    def get_mean_speed(self) -> float:
        self.speed = self.length_pool * self.count_pool / self.M_IN_KM / self.duration

def read_package(workout_type: str, data: list) -> Training:
    """Данные полученные от датчиков"""
    dict_train: Dict[str, Type[Training]] = {
    'SWM': Swimming,
    'RUN': Running,
    'WLK': SportWalking 
    }
    if workout_type not in dict_train:
        
if __name__ == '__main__':
    packages = [        
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training) 