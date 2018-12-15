from flask import Flask
from flask import request
from flask import render_template
from flask_table import Table, Col
from csv import reader
'''class Results(Table):
    id = Col('Id', show=False)
    TypeFlag = Col('TypeFlag')
    PlanetaryMassJpt = Col('PlanetaryMassJpt')
    RadiusJpt = Col('RadiusJpt')
    PeriodDays = Col('PeriodDays')
    Eccentricity = Col('Eccentricity')
    PeriastronDeg = Col('PeriastronDeg')
    LongitudeDeg = Col('LongitudeDeg')
    AscendingNodeDeg = Col('AscendingNodeDeg')
    InclinationDeg = Col('InclinationDeg')
    SurfaceTempK = Col('SurfaceTempK')    
    AgeGyr = Col('AgeGyr')
    DiscoveryMethod = Col('DiscoveryMethod')
    DiscoveryYear = Col('DiscoveryYear')    
    LastUpdated = Col('LastUpdated')
    RightAscension = Col('RightAscension')
    Declination = Col('Declination')    
    DistFromSunParsec = Col('DistFromSunParsec')
    HostStarMassSlrMass = Col('HostStarMassSlrMass')
    HostStarRadiusSlrRad = Col('HostStarRadiusSlrRad')    
    HostStarMetallicity = Col('HostStarMetallicity')
    HostStarTempK = Col('HostStarTempK')
    HostStarAgeGyr = Col('HostStarAgeGyr')
    ListsPlanetIsOn = Col('ListsPlanetIsOn')'''

def csv_search(item):
    with open("oec.csv", "r") as fo:
        read = reader(fo)
        ans = "Not Found"
        for row in read:
            if item in row:
                fo.close()
                return row
    fo.close()
    return ans 

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("base.html") # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['text1']
    planet = csv_search(text1)
    if planet == 0 :
        return "<h1>Not available</h1>"
    else :
        res = ""
        for i in planet:
            res += i + "|"
        ans = "<h1>"+res+"</h1>"
        return ans

if __name__ == '__main__':
    app.run()