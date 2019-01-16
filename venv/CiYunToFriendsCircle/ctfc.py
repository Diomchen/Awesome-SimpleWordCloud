#-*-coding:utf-8-*-
import jieba
from jieba.analyse import extract_tags
import wordcloud

def analyseKeyWord2Dict(path):
    #加载自行设置的停止词（一些无关紧要的术语和常用词）
    jieba.analyse.set_stop_words(stop_words_path='F:\\PythonDemo\\词云\\venv\\CiYunToFriendsCircle\\停止词.txt')

    #加载词典
    jieba.load_userdict("F:\\PythonDemo\\词云\\venv\\CiYunToFriendsCircle\\词典.txt")

    #为词典增加词汇（如果要增强程序的灵活性，可采取文件路径读取方式载入）
    # jieba.add_word("孔乙己")
    # jieba.add_word("鲁镇")
    jieba.add_word("死侍")

    #读入文件
    f = open(path, 'r', encoding='utf-8')
    text = f.read()
    f.close()

    #关键词是一个含元组的list
    keyword = extract_tags(text, topK=100, withWeight=True, allowPOS=())

    #此处只是为准备将关键字写入文件查看，便于筛选出停止词
    # with open("F:\\PythonDemo\\词云\\venv\\CiYunToFriendsCircle\\dict.txt", 'w', encoding='utf-8') as file:
    #     for word,weight in keyword:
    #         file.write(word+'\n')
    #         print(word)
    # print(dict(keyword))
    return keyword

def main():
    # print(type(analyseKeyWord2Dict("F:\\PythonDemo\\词云\\venv\\CiYunToFriendsCircle\\孔乙己.txt")))
    return analyseKeyWord2Dict("F:\\PythonDemo\\词云\\venv\\CiYunToFriendsCircle\\死侍.txt")

if __name__ == '__main__':
    main()