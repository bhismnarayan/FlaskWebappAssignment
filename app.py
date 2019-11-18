from flask import Flask,render_template,request,abort
from werkzeug.exceptions import BadRequest

import backendFunction as bf

app = Flask(__name__)

@app.route("/")
def home():
    try:
        data={}
        data['season']=bf.getUniqueSeason()
        data['topteam']=bf.top4TeamInWinnner()
        data['teamToWinMostTossInSeason']=bf.TeamToWinMostTossInSeason(data['season'][0])
        data['PlayerToWinMaxManOfMatchInSeason']=bf.PlayerToWinMaxManOfMatchInSeason(data['season'][0])
        data['TeamToWinMaxMaxinSeason']=bf.TeamToWinMaxMaxinSeason(data['season'][0])
        data['LocationWithMostWinsForTopTeam']=bf.LocationWithMostWinsForTopTeam()
        data['PercentageOfTeamDecidedToBatWhenWonTheToss']=bf.PercentageOfTeamDecidedToBatWhenWonTheToss()
        data['HighestMarginWinForaseason']=bf.HighestMarginWinForaseason(data['season'][0])
        data['HighestNumberofWicketWinForaseason']=bf.HighestNumberofWicketWinForaseason(data['season'][0])
        data['NumberOfTImeTeamWonTheTossAndTheMatch']=bf.NumberOfTImeTeamWonTheTossAndTheMatch()
        data['BatsmanGaveAwayMostNumberOfRunsInAMachInASeason']=bf.BatsmanGaveAwayMostNumberOfRunsInAMachInASeason(data['season'][0])
        data['MostNumberOfCatchesByFielderinMatchForTheSelectedSeason']=bf.MostNumberOfCatchesByFielderinMatchForTheSelectedSeason(data['season'][0])
        data['LocationHostedMostNumberOfMatchesAndWinLossPercentage']=bf.LocationHostedMostNumberOfMatchesAndWinLossPercentage(data['season'][0])


        return render_template("home.html",data=data)
    except Exception as e:
        return e   
    


@app.route("/teamToWinMostTossInSeason", methods=(['GET']))
def teamToWinMostTossInSeason():
    season = request.args.get('season')
    if season:
        return str(bf.TeamToWinMostTossInSeason(int(season)))
    else:
        return 'Season query parameter expected'    

@app.route("/winlossPercentageSeason", methods=(['GET']))
def winlossPercentageSeason():
    season = request.args.get('season')
    if season:
        return str(bf.LocationHostedMostNumberOfMatchesAndWinLossPercentage(int(season)))
    else:
        return 'Season query parameter expected'    

@app.route("/PlayerToWinMaxManOfMatchInSeason", methods=(['GET']))
def PlayerToWinMaxManOfMatchInSeason():
    season   = request.args.get('season')
    if season:
        return str(bf.PlayerToWinMaxManOfMatchInSeason(int(season)))
    else:
        return abort(500,'Season query parameter expected')

@app.route("/TeamToWinMaxMaxinSeason", methods=(['GET']))
def TeamToWinMaxMaxinSeason():
    season   = request.args.get('season')
    if season:
        return str(bf.TeamToWinMaxMaxinSeason(int(season)))
    else:
        return abort(500,'Season query parameter expected')

@app.route("/LocationWithMostWinsForTopTeam", methods=(['GET']))
def LocationWithMostWinsForTopTeam():
    try:
        return str(bf.LocationWithMostWinsForTopTeam())
    except Exception as e:
        return abort(500,e)

@app.route("/PercentageOfTeamDecidedToBatWhenWonTheToss", methods=(['GET']))
def PercentageOfTeamDecidedToBatWhenWonTheToss():
    try:
        return str(bf.PercentageOfTeamDecidedToBatWhenWonTheToss())
    except Exception as e:
        return abort(500,e)

@app.route("/HighestMarginWinForaseason", methods=(['GET']))
def HighestMarginWinForaseason():
    season   = request.args.get('season')
    if season:
        return str(bf.HighestMarginWinForaseason(int(season)))
    else:
        return abort(500,'Season query parameter expected')        

@app.route("/HighestNumberofWicketWinForaseason", methods=(['GET']))
def HighestNumberofWicketWinForaseason():
    season   = request.args.get('season')
    if season:
        return str(bf.HighestNumberofWicketWinForaseason(int(season)))
    else:
        return abort(500,'Season query parameter expected')        



@app.route("/NumberOfTImeTeamWonTheTossAndTheMatch", methods=(['GET']))
def NumberOfTImeTeamWonTheTossAndTheMatch():
    season   = request.args.get('season')
    if season:
        return str(bf.NumberOfTImeTeamWonTheTossAndTheMatch())
    else:
        return abort(500,'Season query parameter expected')        


@app.route("/BatsmanGaveAwayMostNumberOfRunsInAMachInASeason", methods=(['GET']))
def BatsmanGaveAwayMostNumberOfRunsInAMachInASeason():
    season   = request.args.get('season')
    if season:
        return str(bf.BatsmanGaveAwayMostNumberOfRunsInAMachInASeason(int(season)))
    else:
        return abort(500,'Season query parameter expected')        


@app.route("/MostNumberOfCatchesByFielderinMatchForTheSelectedSeason", methods=(['GET']))
def MostNumberOfCatchesByFielderinMatchForTheSelectedSeason():
    season   = request.args.get('season')
    if season:
        return str(bf.MostNumberOfCatchesByFielderinMatchForTheSelectedSeason(int(season)))
    else:
        return abort(500,'Season query parameter expected')    

if __name__ == "__main__":
    app.run(debug=True)