class Top:
    def m_top(self):
        print("top")

class Middle(Top):
    def m_middle(self):
        print("middle")

class Bottom(Top, Middle): #MRO not possible
    def m_bottom(self):
        print("bottom")

object = Bottom()

object.m_bottom()
object.m_middle()
object.m_top()