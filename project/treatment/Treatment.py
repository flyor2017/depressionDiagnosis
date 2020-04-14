import json
import os

__author__ = "flyor"

r"""
该类的主要功能是根据用户的患病概率，输出针对性的治疗建议。
"""


class Treatment(object):

    schemeFile = "resources/treatment.json"

    def __init__(self):
        super().__init__()

        # 治疗方案
        self._treatmentScheme = None

        # 每个疾病的具体规则
        self._rules = None

        # 整个json文件
        self._fileContent = None

        # 拿到当前脚本文件所在的mul
        dirname = os.path.dirname(__file__)
        dirname = os.path.dirname(dirname)

        schemeFile = os.path.join(dirname, Treatment.schemeFile)

        # 从资源文件中读取治疗规则
        self.readScheme(schemeFile)

    def readScheme(self, file):
        r"""
        从指定文件中读取治疗方案
        """
        with open(file, encoding="utf-8") as f:
            content = json.load(f)
            self._fileContent = content
            self._treatmentScheme = content["treatments"]
            self._rules = content["rules"]

    def __printScheme(self, keys):
        r"""
        该方法用于根据索引列表打印对应的治疗方案。
        """
        for key in keys:
            scheme = self._treatmentScheme[key]
            if "scheme" in scheme:
                print(" "*4, key, scheme["scheme"], sep="")
            else:
                print(" "*4, key, sep="")
            if "detail" in scheme:
                for i in scheme["detail"]:
                    print(" "*8, i, sep="")

    def printScheme(self, disease, g):
        r"""
        根据用户所患的疾病，打印对于的治疗方案
        """

        # 首先查找该疾病对于的方案
        rule = None
        for r in self._rules:
            if disease in r["illness"]:
                rule = r
                break
        else:
            # 没有找到对应的治疗方案
            print("目前还没有收录关于%s疾病的治疗方案！" % disease)
            return

        # 是否已经输出过“注”字
        notePrinted = False

        print("治疗方式：")
        if "treatment" in rule:
            # 对于没有限制的疾病直接输出治疗结果
            # 先输出治疗方式
            self.__printScheme(rule["treatment"])
        else:
            # 对于有限制的疾病，
            # 先找到没有限制的治疗方式
            # 再找满足限制的治疗方式

            norestiction = None
            treatments = []

            for t in rule["treatments"]:
                if "restriction" in t:
                    for r in t["restriction"]:
                        if g.getSyntheticalProbability(r) >= 0.5:
                            treatments.append(t)
                            break
                else:
                    norestiction = t

            # 先输出没有限制的治疗方式，
            # 再输出有限制的治疗方式
            if norestiction:
                self.__printScheme(norestiction["treatment"])
            for t in treatments:
                self.__printScheme(t["treatment"])

            # 然后输出没有限制的治疗方式的注意事项
            # 再输出有限制的治疗方式的注意事项
            if norestiction and "note" in norestiction:
                if notePrinted == False:
                    print("注：")
                    notePrinted = True
                for i in norestiction["note"]:
                    print(" "*4, i, sep="")

            for t in treatments:
                if notePrinted == False:
                    print("注：")
                    notePrinted = True
                for i in t["note"]:
                    print(" "*4, i, sep="")

        # 再输出治疗的注意事项
        if "note" in rule:
            if notePrinted == False:
                print("注：")
                notePrinted = True
            for i in rule["note"]:
                print(" "*4, i, sep="")

        # 输出最后的注意事项和禁忌
        if "note" in self._fileContent:
            for i in self._fileContent["note"]:
                print(" "*4, i, sep="")

        if "warnning" in self._fileContent:
            print("禁忌：")
            for i in self._fileContent["warnning"]:
                print(" "*4, i, sep="")
