from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
from importlib import reload
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import EDA
reload(EDA)

df = EDA.clean_df()

x = df.iloc[:,:-1]

x = pd.get_dummies(
    x,
    columns=[
        "gender",
    ],
    dtype=int
)
y= df.iloc[:,-1]

x_train , x_test ,y_train ,y_test = train_test_split(x,y, test_size=0.1 ,random_state=40)



from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
# making the bagging classifier with 500 decision treee # n_estimstord=

Rmodel = RandomForestClassifier(n_estimators=500)

Rmodel.fit(x_train, y_train)

pred = Rmodel.predict(x_test)

from sklearn.metrics import accuracy_score , confusion_matrix , classification_report

print(f"accuracy_score is {accuracy_score(y_test,pred)*100}")
cm = confusion_matrix(y_test,pred)
print(f"confusion_matrix Result\n{cm}")

