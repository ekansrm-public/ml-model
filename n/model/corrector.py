"""
拼写纠正器

参数: ngram的阶数, ngramModel,

过程: 获取候选词, 还有上下文 -> 汉明距 -> 通过 ngramModel 在里面选择一个最高的(频率极少概率)

"""

