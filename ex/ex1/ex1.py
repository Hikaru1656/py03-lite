from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score


# X, Y
learn_data = [[0], [1], [2], [3], [4], [5], [6]]

# X and Y
learn_label = [0,2,4,6,8,10,12]

# アルゴリズムの推定
clf = LinearRegression()

# 学習用データと結果の学習
clf.fit(learn_data, learn_label)

# テストデータによる予測
test_data = [[7], [8], [9], [10]]
test_label = clf.predict(test_data)

# 予測結果の評価
print(test_data, "の予測結果:", test_label)
print(" 正解率 = ", accuracy_score([14,16,18,20], test_label))
