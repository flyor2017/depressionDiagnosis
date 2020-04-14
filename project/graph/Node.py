
__author__ = "flyor"


class Node(object):

    def __init__(self, parent=None):
        super().__init__()

        # 实现自动绑定
        # 如果当前节点有父节点，
        # 则自动将当前节点添加到父节点的子节点列表中
        if parent:
            self._parent = parent
            parent.addChild(self)

    def addChild(self, child):
        r"""
        如果存在子节点列表则添加子节点到列表中，
        否则创建子节点列表再添加子节点到列表中。
        """
        if not hasattr(self, "_children"):
            self._children = set()
        self._children.add(child)

    def getParent(self):
        r"""
        返回当前节点的父节点
        """
        return self._parent

    def getChildren(self):
        r"""
        返回当前节点的子节点
        """
        return getattr(self, "_children", None)

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError()

    def printGraph(self, deep=0):
        r"""
        从当前节点开始递归打印节点树
        """
        s = ""
        if deep != 0:
            s += "│ " * deep
            s += "├─"
        # 打印当前节点
        print(s, self, sep="")

        # 递归打印子节点
        if hasattr(self, "_children"):
            for e in self._children:
                e.printGraph(deep + 1)
