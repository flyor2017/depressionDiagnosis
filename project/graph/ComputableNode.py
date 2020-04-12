from .Node import Node
from math import pi
from math import e

__author__ = "flyor"


class ComputableNode(Node):

    # 每个症状的默认概率值
    K = 0.2

    # S型曲线的默认指数
    E = 1

    # 默认情况下需要参与计算的子节点的个数
    N = 1

    def __init__(self, parent=None):
        super().__init__(parent)

    @staticmethod
    def sigmoid(prob, exp=E):
        r"""
        S型激活函数
        当指数小于1时，数值向0和1两端偏移映射
        当指数等于1时，为恒等映射
        当指数大于1时，数值向中点1/2偏移映射
        """
        if exp < 0:
            raise ValueError()
        tmp = 2 * prob - 1
        if tmp < 0:
            tmp = -(-tmp) ** exp
        else:
            tmp = tmp ** exp
        return (tmp+1)/2

    def getSyntheticalProbability(self):
        r"""
        该函数用于计算综合概率，但是是一个未实现的抽象函数
        不同的子类需要根据具体情况进行实现。
        """
        raise NotImplementedError()

    @staticmethod
    def normalDitribute(x, u=0, s=1):
        r"""
        计算正态分布概率密度函数在某一点的值
        """
        exp = -((x - u) ** 2 / (2 * s ** 2))
        factor = s * (2 * pi) ** 0.5
        return e ** exp / factor

    def __str__(self):
        return super().__str__() + " %0.4f" % self.getSyntheticalProbability()
