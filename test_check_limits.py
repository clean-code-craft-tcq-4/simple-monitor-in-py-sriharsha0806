from check_limits import main

assert(main.battery_is_ok(25, 70, 0.7) is True)
assert(main.battery_is_ok(50, 85, 0) is False)
