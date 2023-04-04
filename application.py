from flask import Flask, request, app,render_template,redirect
from flask import Response
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd
import seaborn as sns
from flask_cors import CORS,cross_origin

application = Flask(__name__)
app=application

@app.route("/",methods=["GET","POST"])
@cross_origin()
def home():
    team1=['Rajasthan Royals', 'Royal Challengers Bangalore','Sunrisers Hyderabad', 'Delhi Capitals', 'Chennai Super Kings','Gujarat Titans', 'Lucknow Super Giants', 'Kolkata Knight Riders','Punjab Kings', 'Mumbai Indians']
    team2=['Rajasthan Royals', 'Royal Challengers Bangalore','Sunrisers Hyderabad', 'Delhi Capitals', 'Chennai Super Kings','Gujarat Titans', 'Lucknow Super Giants', 'Kolkata Knight Riders','Punjab Kings', 'Mumbai Indians']
    return render_template("home.html",team1=team1,team2=team2)


@app.route("/plot",methods=["GET","POST"])
@cross_origin()
def plot():
    if request.method == 'POST':
        img = BytesIO()
        df=pd.read_csv('Cleaned.csv')
        a=request.form['mycheckbox1']
        b=request.form['mycheckbox2']
        if(a==b):
            return render_template("error.html")
        if(a=='Royal'):
            a='Royal Challengers Bangalore'
        elif(a=='Rajasthan'):
            a='Rajasthan Royals'
        elif(a=='Sunrisers'):
            a='Sunrisers Hyderabad'
        elif(a=='Delhi'):
            a='Delhi Capitals'
        elif(a=='Chennai'):
            a='Chennai Super Kings'
        elif(a=='Gujarat'):
            a='Gujarat Titans'
        elif(a=='Lucknow'):
            a='Lucknow Super Giants'
        elif(a=='Kolkata'):
            a='Kolkata Knight Riders'
        elif(a=='Punjab'):
            a='Punjab Kings'
        elif(a=='Mumbai'):
            a='Mumbai Indians'

        if(b=='Royal'):
            b='Royal Challengers Bangalore'
        elif(b=='Rajasthan'):
            b='Rajasthan Royals'
        elif(b=='Sunrisers'):
            b='Sunrisers Hyderabad'
        elif(b=='Delhi'):
            b='Delhi Capitals'
        elif(b=='Chennai'):
            b='Chennai Super Kings'
        elif(b=='Gujarat'):
            b='Gujarat Titans'
        elif(b=='Lucknow'):
                b='Lucknow Super Giants'
        elif(b=='Kolkata'):
            b='Kolkata Knight Riders'
        elif(b=='Punjab'):
            b='Punjab Kings'
        elif(b=='Mumbai'):
            b='Mumbai Indians'


        print(a,b)
        lst=[a,b]
        df1=df[df['Team1'].isin(lst)]
        df2=df1[df1['Team2'].isin(lst)]
        Total_Matches_Played=df2.count()[0]
        a_won=df2[df2['WinningTeam']==a].count()[0]
        b_won=df2[df2['WinningTeam']==b].count()[0]
        draw=df2[df2['SuperOver']=='Y'].count()[0]
        a_homeground=df2[df2['HomeTeam']==a].count()[0]
        b_homeground=df2[df2['HomeTeam']==b].count()[0]
        a_toss_winner=df2[df2['TossWinner']==a].count()[0]
        b_toss_winner=df2[df2['TossWinner']==b].count()[0]
        df3=df2[df2['TossWinner']==a]
        a_tosswin_and_matchwin=df3[df3['WinningTeam']==a].count()[0]
        df3=df2[df2['TossWinner']==b]
        b_tosswin_and_matchwin=df3[df3['WinningTeam']==b].count()[0]
        df4=df2[df2['HomeTeam']==a]
        a_homeground_win=df4[df4['WinningTeam']==a].count()[0]
        df4=df2[df2['HomeTeam']==b]
        b_homeground_win=df4[df4['WinningTeam']==b].count()[0]
        df4=df2[df2['HomeTeam']==b]
        b_homeground_awin=df4[df4['WinningTeam']==a].count()[0]
        df4=df2[df2['HomeTeam']==a]
        a_homeground_bwin=df4[df4['WinningTeam']==b].count()[0]
        df4=df2[df2['HomeTeam']=='out']
        a_out_win=df4[df4['WinningTeam']==a].count()[0]
        df4=df2[df2['HomeTeam']=='out']
        b_out_win=df4[df4['WinningTeam']==b].count()[0]

        if a=='Chennai Super Kings':
            i='#f7f414'
        elif a=='Rajasthan Royals':
            i='#f507ae'
        elif a=='Royal Challengers Bangalore':
            i='#fa0e0a'
        elif a=='Sunrisers Hyderabad':
            i='#ee7429'
        elif a=='Delhi Capitals':
            i='#d71921'
        elif a=='Gujarat Titans':
            i='#1B2133'
        elif a=='Lucknow Super Giants':
            i='#8ad8ee'
        elif a=='Kolkata Knight Riders':
            i='#3A225D'
        elif a=='Punjab Kings':
            i='#dd1f2d'
        else:
            i='#004b8d'
        
        
        
        if b=='Chennai Super Kings':
            j='#f7f414'
        elif b=='Rajasthan Royals':
            j='#f507ae'
        elif b=='Royal Challengers Bangalore':
            j='#fa0e0a'
        elif b=='Sunrisers Hyderabad':
            j='#ee7429'
        elif b=='Delhi Capitals':
            j='#d71921'
        elif b=='Gujarat Titans':
            j='#1B2133'
        elif b=='Lucknow Super Giants':
            j='#8ad8ee'
        elif b=='Kolkata Knight Riders':
            j='#3A225D'
        elif b=='Mumbai Indians':
            j='#004b8d'
        else:
            j='#dd1f2d'


        data = [a_won,b_won,draw]
        keys = [a+' Win',b+' Win','Draw']
        colors = [i,j,'#1c1c1c']
        explode = [0.1, 0.1, 0]
        plt.pie(data, labels=keys, autopct='%.0f%%',explode=explode,wedgeprops = { 'linewidth' : 2, 'edgecolor' : 'white' },colors=colors, shadow=True, startangle=150)
        plt.title("Match Win Percentage", bbox={'facecolor':'0.8', 'pad':3})
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url1 = base64.b64encode(img.getvalue()).decode('utf8')


        data = [a_tosswin_and_matchwin,b_tosswin_and_matchwin,draw]
        keys = [a+' Win',b+' Win','Draw']
        colors = [i,j,'#1c1c1c']
        explode = [0.1, 0.1, 0]
        plt.pie(data, labels=keys, autopct='%.0f%%',explode=explode,wedgeprops = { 'linewidth' : 2, 'edgecolor' : 'white' },colors=colors, shadow=True, startangle=150)
        plt.title("Team After Winning Toss Win Percentage", bbox={'facecolor':'0.8', 'pad':3})
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url2 = base64.b64encode(img.getvalue()).decode('utf8')

        a_hometeam=a.split()[0]
        b_hometeam=b.split()[0]
        if(a=='Royal Challengers Bangalore'):
            a_hometeam=a.split()[2]
        elif(b=='Royal Challengers Bangalore'):
            b_hometeam=b.split()[2]
        elif(a=='Sunrisers Hyderabad'):
            a_hometeam=a.split()[1]
        elif(b=='Sunrisers Hyderabad'):
            b_hometeam=b.split()[1]
        df5=pd.DataFrame({'Host Team':[a_hometeam,a_hometeam,b_hometeam,b_hometeam,'Away','Away'],'Team':[a,b,a,b,a,b],'Win':[a_homeground_win,a_homeground_bwin,b_homeground_awin,b_homeground_win,a_out_win,b_out_win]})
        ax=sns.barplot(x="Host Team",y="Win",hue="Team",data=df5,palette=[i,j],)
        for container in ax.containers:
            ax.bar_label(container)
        plt.legend(loc='upper right')
        plt.title("Matches Win in Homeground and Away from Home", bbox={'facecolor':'0.8', 'pad':3})
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url3 = base64.b64encode(img.getvalue()).decode('utf8')


        df6=df1[(df1['Team1']==a) | (df1['Team2']==a)]
        df7=df6[df6['TossWinner']==a]
        a_bat=df7[df7['TossDecision']=='bat'].count()[0]
        df8=df7[df7['TossDecision']=='bat']
        a_bowl_win=df8[df8['WinningTeam']==a].count()[0]
        df6=df1[(df1['Team1']==a) | (df1['Team2']==a)]
        df7=df6[df6['TossWinner']==a]
        a_field=df7[df7['TossDecision']=='field'].count()[0]
        df8=df7[df7['TossDecision']=='field']
        a_chase_win=df8[df8['WinningTeam']==a].count()[0]
        df6=df1[(df1['Team1']==b) | (df1['Team2']==b)]
        df7=df6[df6['TossWinner']==b]
        b_bat=df7[df7['TossDecision']=='bat'].count()[0]
        df8=df7[df7['TossDecision']=='bat']
        b_bowl_win=df8[df8['WinningTeam']==b].count()[0]
        df6=df1[(df1['Team1']==b) | (df1['Team2']==b)]
        df7=df6[df6['TossWinner']==b]
        b_field=df7[df7['TossDecision']=='field'].count()[0]
        df8=df7[df7['TossDecision']=='field']
        b_chase_win=df8[df8['WinningTeam']==b].count()[0]
        data = [a_bat,a_field]
        keys = ['Batting','Fielding']
        col=['green','blue']
        plt.pie(data, labels=keys, autopct='%.0f%%',wedgeprops = { 'linewidth' : 2, 'edgecolor' : 'white' }, shadow=True, startangle=150,colors=col)
        plt.title("After Winning Toss "+ a +' Chosses', bbox={'facecolor':'0.8', 'pad':3})
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url4 = base64.b64encode(img.getvalue()).decode('utf8')


        data = [b_bat,b_field]
        keys = ['Batting','Fielding']
        col=['green','blue']
        plt.pie(data, labels=keys, autopct='%.0f%%',wedgeprops = { 'linewidth' : 2, 'edgecolor' : 'white' }, shadow=True, startangle=150,colors=col)  
        plt.title("After Winning Toss "+ b +' Chosses', bbox={'facecolor':'0.8', 'pad':3})
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url5 = base64.b64encode(img.getvalue()).decode('utf8')


        data = [a_chase_win,b_bowl_win]
        keys = ['Chassing','Fielding']
        col=['green','blue']
        plt.pie(data, labels=keys, autopct='%.0f%%',wedgeprops = { 'linewidth' : 2, 'edgecolor' : 'white' }, shadow=True, startangle=150,colors=col)
        plt.title(a+" Win while Chasing and Fielding", bbox={'facecolor':'0.8', 'pad':3})
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url6 = base64.b64encode(img.getvalue()).decode('utf8')


        data = [b_chase_win,b_bowl_win]
        keys = ['Chassing','Fielding']
        col=['green','blue']
        plt.pie(data, labels=keys, autopct='%.0f%%',wedgeprops = { 'linewidth' : 2, 'edgecolor' : 'white' }, shadow=True, startangle=150,colors=col)
        plt.title(b+" Win while Chasing and Fielding", bbox={'facecolor':'0.8', 'pad':3})
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url7 = base64.b64encode(img.getvalue()).decode('utf8')
        return render_template('plot.html', plot_url1=plot_url1,plot_url2=plot_url2,plot_url3 =plot_url3,plot_url4 =plot_url4,plot_url5 =plot_url5,plot_url6 =plot_url6,plot_url7 =plot_url7 )
    return render_template("error.html")
    
if __name__=="__main__":
    app.run(host="0.0.0.0")
