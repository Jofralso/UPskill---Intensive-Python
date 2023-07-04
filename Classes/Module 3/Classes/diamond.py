class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

d = D()

'''
               A
             / |  \
            B  F  C
             \ | /
               D
               
'''

class Top:
    def m_top(self):
        print("top")

class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")

class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")

class Bottom(Middle_Right, Middle_Left):
    def m_bottom(self):
        print("bottom")



obj = Bottom()
obj.m_bottom()
obj.m_middle()
obj.m_top()