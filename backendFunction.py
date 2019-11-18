import pandas as pd 

matchdata = pd.read_csv(r"matches.csv")
deliveriesdata = pd.read_csv(r"deliveries.csv")

def getUniqueSeason():
    return matchdata.season.sort_values().unique()



#Top 4 teams in terms of wins
def top4TeamInWinnner():
    resultdata=list(matchdata.groupby('winner').size().sort_values(ascending=False).head(4).index)
    return resultdata

#Which team won the most number of tosses in the season
def TeamToWinMostTossInSeason(season):
    resultdata=list(matchdata[matchdata['season']==season].groupby('toss_winner').size().sort_values(ascending=False).head(1).index)
    return resultdata[0]

#Which player won the maximum number of Player of the Match awards in the whole season
def PlayerToWinMaxManOfMatchInSeason(season):
    resultdata=list(matchdata.loc[(matchdata['season'] == season)].groupby('player_of_match').size().sort_values(ascending=False).head(1).index)
    return resultdata[0]


#Which team won max matches in the whole season
def TeamToWinMaxMaxinSeason(season):
    resultdata=list(matchdata.loc[(matchdata['season'] == season)].groupby('winner').size().sort_values(ascending=False).head(1).index)
    return resultdata[0]

#   Which location has the most number of wins for the top team
def LocationWithMostWinsForTopTeam():
    topteamdata=top4TeamInWinnner()
    resultdata=list(matchdata.loc[(matchdata['winner'] ==topteamdata[0]) ].groupby('city').size().sort_values(ascending=False).head(1).index)
    return resultdata[0]

#	Which % of teams decided to bat when they won the toss
def PercentageOfTeamDecidedToBatWhenWonTheToss():
    resultdata=matchdata.loc[(matchdata['toss_decision'] =='bat') ].groupby('toss_decision').size().sort_values(ascending=False).head()[0]/matchdata.shape[0]
    return round(resultdata*100,2)

#	Which location hosted most number of matches and win % and loss % for the season
def LocationHostedMostNumberOfMatchesAndWinLossPercentage(season):
    currentseasondata=matchdata[matchdata['season']==season]
    cityname=currentseasondata.groupby('city').size().sort_values(ascending=False).head(1).index[0]
    currentCityData=currentseasondata[currentseasondata['city']==cityname]
    winnerdata=currentCityData.groupby('winner').size().sort_values(ascending=False).to_frame()
    team1data=currentCityData.groupby(['team1']).size().to_frame()
    team2data=currentCityData.groupby(['team2']).size().to_frame()
    winlossdata=team1data.join(team2data,lsuffix='team1',rsuffix='team2',how='outer').join(winnerdata).fillna(0)
    winlossdata['totalMatchesPlayed']=winlossdata['0team1']+winlossdata['0team2']
    #winlossdata['win%']=winlossdata['totalMatchesPlayed']+winlossdata[]
    winlossdata.rename(columns = {'0':'Won'}, inplace = True) 
    winlossdata['Win_Percentage']=winlossdata.iloc[:,2]*100/winlossdata.iloc[:,3]
    winlossdata['Loss_Percentage']=100-winlossdata['Win_Percentage']
    winlossdata['city']=cityname
    resultdata=(winlossdata[['Win_Percentage','Loss_Percentage','city']])
    print(resultdata)
    return resultdata





#	Which team won by the highest margin of runs  for the season
def HighestMarginWinForaseason(season):
    resultdata=matchdata.loc[(matchdata['win_by_runs'] > 0) & (matchdata['season'] == season)].sort_values(ascending=False,by='win_by_runs').head(1).winner
    
    return resultdata.iat[0]

    
#Which team won by the highest number of wickets for the season
def HighestNumberofWicketWinForaseason(season):
    resultdata=matchdata.loc[(matchdata['win_by_wickets'] > 0) & (matchdata['season'] == season)].sort_values(ascending=False,by='win_by_wickets').head(1).winner
    print(resultdata)
    return resultdata

#	How many times has a team won the toss and the match
def NumberOfTImeTeamWonTheTossAndTheMatch():
    resultdata=matchdata.loc[(matchdata['toss_winner'] ==matchdata['winner'])].head().shape[0]
    print(resultdata)
    return resultdata

#	Which Batsman gave away the most number of runs in a match for the selected season
def BatsmanGaveAwayMostNumberOfRunsInAMachInASeason(season):
    matchid=matchdata.loc[(matchdata['season'] ==season)].id
    subdata=deliveriesdata.loc[(deliveriesdata['batsman_runs'] >0)]
    resultdata=subdata[subdata['match_id'].isin(matchid)].groupby(['batsman','match_id']).size().sort_values(ascending=False).head(1)
    print(resultdata)
    return resultdata
#	Most number of catches by a fielder in a match for the selected season.
def MostNumberOfCatchesByFielderinMatchForTheSelectedSeason(season):
    matchid=matchdata.loc[(matchdata['season'] ==season)].id
    catchdata1=deliveriesdata.loc[(deliveriesdata['dismissal_kind'] =='caught')]
    resultdata=catchdata1[catchdata1['match_id'].isin(matchid)].groupby(['match_id','fielder']).size().sort_values(ascending=False).head(1)
    print(resultdata)
    return resultdata

 
PercentageOfTeamDecidedToBatWhenWonTheToss()