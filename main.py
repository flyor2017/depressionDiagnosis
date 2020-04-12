from project import Graph
from project.graph import SymptomNode


def printProbability(g, diseases):
    print("-------start---------")
    for i in diseases:
        print("{0:　<16}{1:.4f}".format(i, g.getSyntheticalProbability(i)))
    print("--------end----------")


if __name__ == "__main__":
    diseaseFile = "resources/知识图谱-核心实体关系v1.3.xlsx"
    symptomFile = "resources/知识图谱-核心实体关系v1.3.xlsx"
    ruleFile = "resources/rule.json"
    g = Graph()
    g.readDisease(diseaseFile, "疾病-疾病关系")
    g.readSymptom(symptomFile, "大症状-小症状关系")
    g.readSymptom(symptomFile, "小症状-小症状关系")
    g.readRule(ruleFile)

    # 需要查看的疾病列表
    arr = ["轻度抑郁发作", "轻度抑郁发作不伴躯体症状",
           "轻度抑郁发作伴躯体症状", "中度抑郁发作",
           "中度抑郁发作不伴躯体症状", "中度抑郁发作伴躯体症状",
           "重度抑郁发作", "重度抑郁发作不伴精神病性症状",
           "重度抑郁发作伴有精神病性症状"]

    g.setProbability("自卑", 0.7, SymptomNode.DEEP_DEGREE)
    g.setProbability("自责自罪", 0.6)
    g.setProbability("哭泣", 0.2, negator=True)

    # g.printGraph()
    printProbability(g, arr)

    g.reset()
    printProbability(g, arr)

    g.setProbability("哭泣", 0.6)
    g.setProbability("失去兴趣", 0.5)
    g.setProbability("精力丧失", 0.58)
    g.setProbability("食欲减少", 0.62)
    g.setProbability("自卑", 0.53)
    g.setProbability("自责", 0.77)
    g.setProbability("早醒", 0.57)
    # g.printGraph()
    printProbability(g, arr)
