from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(features, labels)
pred = clf.predict(predict_set)