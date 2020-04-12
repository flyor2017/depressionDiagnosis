from .ComputableNode import ComputableNode

__author__ = "flyor"


class SymptomNode(ComputableNode):

    # 程度词
    SHALLOW_DEGREE = 4/3
    NORMAL_DEGREE = 1
    DEEP_DEGREE = 3/4

    def __init__(self):
        super().__init__()

        # 该症状的概率值
        self._probability = ComputableNode.K

        # 该症状的程度值
        self._degree = SymptomNode.NORMAL_DEGREE

        # 用户描述该症状是否用了否定词，False表示没用否定词，即肯定该症状
        self._negator = False

    @property
    def probability(self):
        return self._probability

    @probability.setter
    def probability(self, value):
        if isinstance(value, int) or isinstance(value, float):
            if value >= 0 and value <= 1:
                self._probability = value
            else:
                raise ValueError()
        else:
            raise TypeError()

    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, value):
        if isinstance(value, int) or isinstance(value, float):
            if value > 0:
                self._degree = value
            else:
                raise ValueError()
        else:
            raise TypeError()

    @property
    def negator(self):
        return self._negator

    @negator.setter
    def negator(self, value):
        if isinstance(value, bool):
            self._negator = value
        else:
            raise TypeError()

    def getSubSymptoms(self):
        r"""
        获取该症状所含的所有子症状
        """
        return self.getChildren()

    def addSubSymptom(self, symptom):
        r"""
        添加该症状所含的子症状
        """
        if isinstance(symptom, SymptomNode):
            self.addChild(symptom)

    def getSyntheticalProbability(self):
        r"""
        实现父类的抽象方法，用于计算当前症状树的综合概率。
        其中当前症状树的综合概率计算需要考虑到以下内容：
        1、程度词
        2、否定词
        3、当前症状的概率
        4、子症状树的综合概率
        """

        prob = 1 - self._probability if self._negator else self._probability

        # 先计算当前症状的综合概率
        cur = ComputableNode.sigmoid(prob, self._degree)

        # 判断子症状树的个数
        # 如果没有子症状树则直接返回当前症状的综合概率作为当前症状树的综合概率
        if self.getChildren() == None or len(self.getChildren()) == 0:
            return cur

        # 如果存在子症状树，则获取子症状树综合概率的最大值
        arr = (node.getSyntheticalProbability() for node in self.getChildren())
        maximum = max(arr)

        # 返回当前症状和子症状树的综合概率的最大值作为当前症状树的综合概率
        return maximum if maximum >= cur else cur
