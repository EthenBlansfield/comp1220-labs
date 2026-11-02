"""Part A tests. Your code goes in Lab7/laser.py."""
from laser import LaserClass, RechargeableLaser


def test_new_laser_has_100_power():
    assert LaserClass().remaining_power == 100


def test_new_laser_can_start_with_other_power():
    assert LaserClass(50).remaining_power == 50


def test_new_laser_points_at_0():
    assert LaserClass().direction == 0


def test_turning_right_and_left():
    laser = LaserClass()
    laser.turn_right()
    laser.turn_right()
    laser.turn_left()
    assert laser.direction == 15


def test_fire_uses_10_power_and_returns_true():
    laser = LaserClass(50)
    assert laser.fire() is True
    assert laser.remaining_power == 40


def test_cannot_fire_with_less_than_10_power():
    laser = LaserClass(5)
    assert laser.fire() is False
    assert laser.remaining_power == 5


def test_rechargeable_laser_is_a_laser():
    assert isinstance(RechargeableLaser(), LaserClass)


def test_recharge_restores_full_power():
    laser = RechargeableLaser(20)
    laser.fire()
    laser.fire()
    assert laser.remaining_power == 0
    laser.recharge()
    assert laser.remaining_power == 20
