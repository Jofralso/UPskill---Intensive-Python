class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"
    var= "l"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Left, Right):
    pass

obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())
