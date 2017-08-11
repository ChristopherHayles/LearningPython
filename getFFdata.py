# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:32:09 2017

@author: Chris Hayles
"""

seasonsToCheck=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
weeksToCheck=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117]

#seasonsToCheck=[2016]
#weeksToCheck=[101]

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

def GetAdditionalPages(markup):
    pagination = markup.find('div', class_="wisbb_paginator")
    if pagination:
        pagination = pagination.find_all('a')
        links = []
        for page in pagination:
            links.append(page.get("href"))
        uniqueLinks = set(links)
        additionalPages = len(uniqueLinks)
    else:
        additionalPages = 0
    return additionalPages

def ParseRushTable(RushTable):
    Player=[]
    Team=[]
    Att=[]
    Yds=[]
    Avg=[]
    TD=[]
    FstDn=[]
    Pct=[]
    Lng=[]
    Fum=[]
    FumL=[]
    for row in RushTable.find_all("tr"):
        cells = row.find_all("td")
        if cells:
            player = cells[0].find("a", class_="wisbb_fullPlayer")
            if player:
                name = player.find("span").string
                Player.append(name)
            teamLink = cells[0].find("span", class_="wisbb_tableAbbrevLink")
            if teamLink:
                teamStr = teamLink.find("a").string
                Team.append(teamStr)
            Att.append(cells[1].string)
            Yds.append(cells[2].string)
            Avg.append(cells[3].string)
            TD.append(cells[4].string)
            FstDn.append(cells[5].string)
            Pct.append(cells[6].string[:-1])
            Lng.append(cells[7].string)
            Fum.append(cells[8].string)
            FumL.append(cells[9].string)
    df = pd.DataFrame(Player, columns=['Name'])
    df['Team']=Team
    df['Att']=Att
    df['Yds']=Yds
    df['Avg']=Avg
    df['TD']=TD
    df['FstDn']=FstDn
    df['Pct']=Pct
    df['Lng']=Lng
    df['Fum']=Fum
    df['FumL']=FumL
    return df

def ParseRecTable(RecTable):
    Player=[]
    Team=[]
    Rec=[]
    Yds=[]
    Tgt=[]
    Avg=[]
    TD=[]
    FstDn=[]
    Pct=[]
    Lng=[]
    Fum=[]
    FumL=[]
    for row in RecTable.find_all("tr"):
        cells = row.find_all("td")
        if cells:
            player = cells[0].find("a", class_="wisbb_fullPlayer")
            if player:
                name = player.find("span").string
                Player.append(name)
            teamLink = cells[0].find("span", class_="wisbb_tableAbbrevLink")
            if teamLink:
                teamStr = teamLink.find("a").string
                Team.append(teamStr)
            Rec.append(cells[1].string)
            Yds.append(cells[2].string)
            Tgt.append(cells[3].string)
            Avg.append(cells[4].string)
            TD.append(cells[5].string)
            FstDn.append(cells[6].string)
            Pct.append(cells[7].string[:-1])
            Lng.append(cells[8].string)
            Fum.append(cells[9].string)
            FumL.append(cells[10].string)
    df = pd.DataFrame(Player, columns=['Name'])
    df['Team']=Team
    df['Rec']=Rec
    df['Yds']=Yds
    df['Tgt']=Tgt
    df['Avg']=Avg
    df['TD']=TD
    df['FstDn']=FstDn
    df['Pct']=Pct
    df['Lng']=Lng
    df['Fum']=Fum
    df['FumL']=FumL
    return df
    
def ParsePassTable(PassTable):
    Player=[]
    Team=[]
    Comp=[]
    Att=[]
    CompPct=[]
    Yds=[]
    Avg=[]
    TD=[]
    Inter=[]
    Qbr=[]
    FstDn=[]
    FstDnPct=[]
    Lng=[]
    Sck=[]
    SckYds=[]
    Fum=[]
    FumL=[]
    for row in PassTable.find_all("tr"):
        cells = row.find_all("td")
        if cells:
            player = cells[0].find("a", class_="wisbb_fullPlayer")
            if player:
                name = player.find("span").string
                Player.append(name)
            teamLink = cells[0].find("span", class_="wisbb_tableAbbrevLink")
            if teamLink:
                teamStr = teamLink.find("a").string
                Team.append(teamStr)
            Comp.append(cells[1].string)
            Att.append(cells[2].string)
            CompPct.append(cells[3].string[:-1])
            Yds.append(cells[4].string)
            Avg.append(cells[5].string)
            TD.append(cells[6].string)
            Inter.append(cells[7].string)
            Qbr.append(cells[8].string)
            FstDn.append(cells[9].string)
            FstDnPct.append(cells[10].string[:-1])
            Lng.append(cells[11].string)
            Sck.append(cells[12].string)
            SckYds.append(cells[13].string)
            Fum.append(cells[14].string)
            FumL.append(cells[15].string)
    df = pd.DataFrame(Player, columns=['Name'])
    df['Team']=Team
    df['Comp']=Comp
    df['Att']=Att
    df['CompPct']=CompPct
    df['Yds']=Yds
    df['Avg']=Avg
    df['TD']=TD
    df['Int']=Inter
    df['Qbr']=Qbr
    df['FstDn']=FstDn
    df['FstDnPct']=FstDnPct
    df['Lng']=Lng
    df['Sck']=Sck
    df['SckYds']=SckYds
    df['Fum']=Fum
    df['FumL']=FumL
    return df

def GetRushStats(season, week):
    url = "http://www.foxsports.com/nfl/stats?season=" + season + "&week=" + week +"&category=RUSHING&opp=0&sort=1&qualified=0&sortOrder=0"
    content = urllib.request.urlopen(url)
    soup = BeautifulSoup(content)
    additional = GetAdditionalPages(soup)
    player_data = soup.find('table', class_="wisbb_standardTable")
    data = ParseRushTable(player_data)
    frames=[data]
    if additional > 0:
        page=2
        while (page <= additional+1):
            newurl = url + "&page=" + str(page)
            newcontent = urllib.request.urlopen(newurl)
            newsoup = BeautifulSoup(newcontent)
            newplayer_data = newsoup.find('table', class_="wisbb_standardTable")
            newdata = ParseRushTable(newplayer_data)
            frames.append(newdata)
            page = page+1
    allPlayers = pd.concat(frames, ignore_index=True)
    allPlayers['Season'] = season
    allPlayers['Wk'] = week
    return allPlayers
    
def GetRecStats(season, week):
    url = "http://www.foxsports.com/nfl/stats?season=" + season + "&week=" + week +"&category=RECEIVING&opp=0&sort=1&qualified=0&sortOrder=0"
    content = urllib.request.urlopen(url)
    soup = BeautifulSoup(content)
    additional = GetAdditionalPages(soup)
    player_data = soup.find('table', class_="wisbb_standardTable")
    data = ParseRecTable(player_data)
    frames=[data]
    if additional > 0:
        page=2
        while (page <= additional+1):
            newurl = url + "&page=" + str(page)
            newcontent = urllib.request.urlopen(newurl)
            newsoup = BeautifulSoup(newcontent)
            newplayer_data = newsoup.find('table', class_="wisbb_standardTable")
            newdata = ParseRecTable(newplayer_data)
            frames.append(newdata)
            page = page+1
    allPlayers = pd.concat(frames, ignore_index=True)
    allPlayers['Season'] = season
    allPlayers['Wk'] = week
    return allPlayers
    
def GetPassStats(season, week):
    url = "http://www.foxsports.com/nfl/stats?season=" + season + "&week=" + week +"&category=PASSING&opp=0&sort=3&qualified=0&sortOrder=0"
    content = urllib.request.urlopen(url)
    soup = BeautifulSoup(content)
    additional = GetAdditionalPages(soup)
    player_data = soup.find('table', class_="wisbb_standardTable")
    data = ParsePassTable(player_data)
    frames=[data]
    if additional > 0:
        page=2
        while (page <= additional+1):
            newurl = url + "&page=" + str(page)
            newcontent = urllib.request.urlopen(newurl)
            newsoup = BeautifulSoup(newcontent)
            newplayer_data = newsoup.find('table', class_="wisbb_standardTable")
            newdata = ParsePassTable(newplayer_data)
            frames.append(newdata)
            page = page+1
    allPlayers = pd.concat(frames, ignore_index=True)
    allPlayers['Season'] = season
    allPlayers['Wk'] = week
    return allPlayers
    
def GetRushStatsIteratable(seasons,weeks):
    frames=[]
    for season in seasons:
        for week in weeks:
            print("Getting " + str(season) + " week " + str(week))
            frames.append(GetRushStats(str(season),str(week)))
    allData = pd.concat(frames, ignore_index=True)
    return allData
    
def GetRecStatsIteratable(seasons,weeks):
    frames=[]
    for season in seasons:
        for week in weeks:
            print("Getting " + str(season) + " week " + str(week))
            frames.append(GetRecStats(str(season),str(week)))
    allData = pd.concat(frames, ignore_index=True)
    return allData
    
def GetPassStatsIteratable(seasons,weeks):
    frames=[]
    for season in seasons:
        for week in weeks:
            print("Getting " + str(season) + " week " + str(week))
            frames.append(GetPassStats(str(season),str(week)))
    allData = pd.concat(frames, ignore_index=True)
    return allData
"""    
RushStats = GetRushStatsIteratable(seasonsToCheck,weeksToCheck)
rushFile_name="rushing.csv"
RushStats.to_csv(rushFile_name, encoding='utf-8', index=False)

RecStats = GetRecStatsIteratable(seasonsToCheck,weeksToCheck)
recFile_name="receiving.csv"
RecStats.to_csv(recFile_name, encoding='utf-8', index=False)
"""
PassingStats = GetPassStatsIteratable(seasonsToCheck,weeksToCheck)
passFile_name="passing.csv"
PassingStats.to_csv(passFile_name, encoding='utf-8', index=False)