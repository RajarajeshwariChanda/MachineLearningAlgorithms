import math as math
#step 0 create a entrophy formula
def find_entrophy(probabilty_yes,probabilty_no):
    # print("finidng entrophy ",probabilty_yes,probabilty_no)
    print(-1*(probabilty_yes*math.log(probabilty_yes,2)+probabilty_no*math.log(probabilty_no,2)))
    return (-1*(probabilty_yes*math.log(probabilty_yes,2)+probabilty_no*math.log(probabilty_no,2)))

def informationgain(entrophy_outlook):
    return totalsetentrophy-entrophy_outlook

#step 1 decide the root node
print("there are total 4 input and 1 output \nOutlook tempartue humidity windy")
print("Outlook is categorised into 3 categories sunny(2y,3n) overcast(4y,0n) rainy(2y,3n)")
print("tempartue is categorised into hot(2y,2n) mild(4y,2n) cool(3y,1n)")
print("humidity is categorised into high(3y,4n) normal(6y,1n)")
print("windy is categorised into true(3y,3n) false(6y,2n)")

#step 1 find entrpohy of total data set
totalnumberofentries=14;
totalnumberofyes=9
totalnumberofno=5
#step 2 find entrophy of dataset
totalsetentrophy=find_entrophy(totalnumberofyes/totalnumberofentries,totalnumberofno/totalnumberofentries)
#step 3 list all in colomuns wise yes or no
outlook_sunny=5
outlook_sunnyyes=2
outlook_sunnyno=3

outlook_overcast=4
outlook_overcastyes=4
outlook_overcastno=0

outlook_rainy=5
outlook_rainyyes=2
outlook_rainyno=3
###########################
tempertaure_hot=4
tempertaure_hotyes=2
tempertaure_hotno=2

tempertaure_mild=6
tempertaure_mildyes=4
tempertaure_mildno=2

tempertaure_cold=4
tempertaure_coldyes=3
tempertaure_coldno=1
###########################

# humidity_high=
# humidity_normal=
humidity_high=7
humidity_highyes=3
humidity_highno=4

humidity_normal=7
humidity_normalyes=6
humidity_normalno=1
###########################
windy_true=6
windy_trueyes=3
windy_trueno=3

windy_false=8
windy_falseyes=6
windy_falseno=2
###########################

#step 4 find entrphy of all coloumns
#coloumn 1 entropy
entrophy_outlook=((outlook_sunny/totalnumberofentries)*find_entrophy(outlook_sunnyyes/outlook_sunny,outlook_sunnyno/outlook_sunny))+((outlook_rainy/totalnumberofentries)*find_entrophy(outlook_rainyyes/outlook_rainy,outlook_rainyno/outlook_rainy))#+find_entrophy(outlook_overcastyes/outlook_overcast,outlook_overcastno/outlook_overcast)
print("entrphy of outlook",entrophy_outlook)
informationgain_outlook=informationgain(entrophy_outlook)
print("informationgain_outlook is",informationgain_outlook)
