from .ComputableNode import ComputableNode
from .RuleNode import RuleNode

__author__ = "flyor"


class DiseaseNode(ComputableNode):

    def __init__(self, parent=None):
        super().__init__(parent)

    # 定义两个属性
    # diseaseId
    # diseaseConcept

    @property
    def diseaseId(self):
        return self._deseaseId

    @diseaseId.setter
    def diseaseId(self, id):
        if isinstance(id, str):
            self._deseaseId = id
        else:
            raise TypeError()

    @property
    def diseaseConcept(self):
        return self._diseaseConcept

    @diseaseConcept.setter
    def diseaseConcept(self, concept):
        if isinstance(concept, str):
            self._diseaseConcept = concept
        else:
            raise TypeError()

    def getSyntheticalProbability(self):
        r"""
        实现父类的求综合概率的函数
        """

        # 如果当前疾病没有子节点，则其概率为0
        if self.getChildren() == None:
            return 0

        # 如果当前节点有诊断规则，则利用诊断规则得出概率
        # 求所有诊断规则综合概率的平均概率的sigmoid
        size = 0
        total = 0
        for node in self.getChildren():
            if isinstance(node, RuleNode):
                total += node.getSyntheticalProbability()
                size += 1

        if size > 0:
            return total / size

        # 如果当前疾病的所有子节点全是疾病，则
        # 当前疾病的概率等于子疾病概率的最大值
        probs = (node.getSyntheticalProbability()
                 for node in self.getChildren())
        return max(probs)
