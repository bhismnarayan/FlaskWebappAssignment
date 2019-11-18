
    function teamToWinMostTossInSeason(){
        season=$("#seasonToss").val()
        console.log(season)
        $.ajax({
                   url: "/teamToWinMostTossInSeason?season="+season,
                   method: "GET",
                   headers: { "Accept": "application/json; odata=verbose" },
                   success: function (data) {
                        if (data) {
                            console.log(data)
                            $('#teamToWinMostTossInSeason').text(data);
                             //This section can be used to iterate through data and show it on screen
                        }       
                  },
                  error: function (data) {
                      alert("Error: "+ data);
                 }
          });
   
    }

    function PlayerToWinMaxManOfMatchInSeason(){
        season=$("#seasonMostManOfTheMatch").val()
        console.log(season)
        $.ajax({
                   url: "/PlayerToWinMaxManOfMatchInSeason?season="+season,
                   method: "GET",
                   headers: { "Accept": "application/json; odata=verbose" },
                   success: function (data) {
                        if (data) {
                            console.log(data)
                            $('#PlayerToWinMaxManOfMatchInSeason').text(data);
                             //This section can be used to iterate through data and show it on screen
                        }       
                  },
                  error: function (data) {
                      alert("Error: "+ data);
                 }
          });
   
    }

    //team to win most match in a season
    function TeamToWinMaxMaxinSeason(){
        season=$("#seasonTeamWonMaxMatches").val()
        console.log(season)
        $.ajax({
                   url: "/TeamToWinMaxMaxinSeason?season="+season,
                   method: "GET",
                   headers: { "Accept": "application/json; odata=verbose" },
                   success: function (data) {
                        if (data) {
                            console.log(data)
                            $('#TeamToWinMaxMaxinSeason').text(data);
                             //This section can be used to iterate through data and show it on screen
                        }       
                  },
                  error: function (data) {
                      alert("Error: "+ data);
                 }
          });
   
    }

    function teamToWinByHighestMarginOfRun(){
        season=$("#seasonTeamWonMaxMatches").val()
        console.log(season)
        $.ajax({
                   url: "/HighestMarginWinForaseason?season="+season,
                   method: "GET",
                   headers: { "Accept": "application/json; odata=verbose" },
                   success: function (data) {
                        if (data) {
                            console.log(data)
                            $('#teamWinByHighestMarginOfRun').text(data);
                             //This section can be used to iterate through data and show it on screen
                        }       
                  },
                  error: function (data) {
                      alert("Error: "+ data);
                 }
          });
   
    }
    function winlossstasts(){
        season=$("#winlossseason").val()
        console.log(season)
        $.ajax({
                   url: "/winlossPercentageSeason?season="+season,
                   method: "GET",
                   headers: { "Accept": "application/json; odata=verbose" },
                   success: function (data) {
                        if (data) {
                            console.log(data)
                             //This section can be used to iterate through data and show it on screen
                        }       
                  },
                  error: function (data) {
                      alert("Error: "+ data);
                 }
          });
   
    }