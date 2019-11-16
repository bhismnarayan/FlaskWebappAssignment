from flask import Flask,render_template,request,abort
from werkzeug.exceptions import BadRequest

import backendFunction as bf

app = Flask(__name__)

@app.route("/")
def home():
    data={}
    data['season']=bf.getUniqueSeason()
    data['topteam']=bf.top4TeamInWinnner()
    #data['teamToWinMostTossInSeason']=bf.TeamToWinMostTossInSeason(2009)
    data['PlayerToWinMaxManOfMatchInSeason']=bf.PlayerToWinMaxManOfMatchInSeason(2009)
    return render_template("home.html",data=data)


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
#@app.errorhandler()
def PlayerToWinMaxManOfMatchInSeason():
    season   = request.args.get('season')
    if season:
        return str(bf.PlayerToWinMaxManOfMatchInSeason(int(season)))
    else:
        #return 'Season query parameter expected', 500
        return abort(500,'Season query parameter expected')
        #raise BadRequest

if __name__ == "__main__":
    app.run(debug=True)