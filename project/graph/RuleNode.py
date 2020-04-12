from .ComputableNode import ComputableNode
from .SymptomNode import SymptomNode

__author__ = "flyor"

"""

这个类是规则节点，用于连接疾病和症状 一个疾病可以通过多个规则对应多个症状 其中一个规则也可以对应多个症状

一个疾病的各个规则之间是【与】的关系 只有满足所有规则才能满足该疾病

而一个规则和各个症状之间是【或】的关系 并且这个【或】是带数量限制的 比如某个规则有8个症状，只要满足至少3条即满足规则
则这8个症状之间为【或】关系，但需要满足 ≥3

"""


class RuleNode(ComputableNode):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 症状中默认的【或】关系的个数限制
        self._count = ComputableNode.N

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if isinstance(value, int):
            symptoms = self.getChildren()
            if value <= len(symptoms):
                self._count = value
        else:
            raise TypeError()

    def setSymptoms(self, symptoms):
        r"""
        向该规则添加症状节点
        """
        self._children = symptoms

    def getSyntheticalProbability(self):
        r"""
        实现父类的求综合概率的函数，首先获得该规则所含症状综合概率≥0.5的所有症状，
        求这些症状的平均值，然后返回该平均值与(normalDistribute(x, u, s) + 0.6)相乘的结果。
        normalDistribute是用来计算正态分布概率密度的函数，x是随机变量，u是期望值，s是标准差。
        """

        # 求所有子症状的概率值
        arr = (node.getSyntheticalProbability() for node in self.getChildren())

        # 筛选出概率值大于等于0.5的所有概率值
        arr = list(filter(lambda v: True if v >= 0.5 else False, arr))

        # 没有任何症状的综合概率值≥0.5
        if len(arr) == 0:
            return 0

        # 求平均值
        avg = sum(arr) / len(arr)

        return (ComputableNode.normalDitribute(len(arr), self._count) + 0.6) * avg

    def __str__(self):
        return "rule %.4f" % self.getSyntheticalProbability()
