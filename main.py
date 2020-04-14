from project import Graph
from project.graph import SymptomNode


if __name__ == "__main__":

    g = Graph()

    # 需要查看的疾病列表
    arr = ["轻度抑郁发作", "轻度抑郁发作不伴躯体症状",
           "轻度抑郁发作伴躯体症状", "中度抑郁发作",
           "中度抑郁发作不伴躯体症状", "中度抑郁发作伴躯体症状",
           "重度抑郁发作", "重度抑郁发作不伴精神病性症状",
           "重度抑郁发作伴有精神病性症状"]

    # 设置某一症状的概率，程度，和描述该症状是否用了否定词
    g.setProbability("自卑", 0.7, SymptomNode.DEEP_DEGREE)
    g.setProbability("自责自罪", 0.6)
    g.setProbability("哭泣", 0.2, negator=True)

    # g.printGraph()

    # 打印建议的治疗方案
    g.printTreatmentScheme(arr)

    # 可以调用下面的方法获取具体某一疾病的概率值
    # g.getSyntheticalProbability(diseaseName)

    # 重置整个模型
    g.reset()

    g.setProbability("哭泣", 0.6)
    g.setProbability("失去兴趣", 0.5)
    g.setProbability("精力丧失", 0.58)
    g.setProbability("食欲减少", 0.62)
    g.setProbability("自卑", 0.53)
    g.setProbability("自责", 0.77)
    g.setProbability("早醒", 0.57)
    # g.printGraph()
    g.printTreatmentScheme(arr)
