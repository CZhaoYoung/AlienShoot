class Settings():
    """存储 alien 的所有设置的类"""

    def __init__(self):
        """初始化游戏静态设置"""
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # alien 设置
        self.fleet_drop_speed = 10

        # 以怎样的速度加速游戏节奏
        self.speedup_scale = 1.1

        # 外星人点数提高
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化游戏的设置"""
        # 1表示向右，-1表示向左
        self.fleet_direction = 1
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 3
        self.ship_speed_factor = 1.5

        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """提高子弹速度及点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)