"""
DESCRIPTION:
    Electoral systems across the world can vary widely. In some systems, such as winner-take-all, the winner is
    determined by the plurality of votes—the candidate that receives the most votes wins, and the loser(s) do not get a
    position.

    Such elections can have “wasted votes.” Conceptually, a wasted vote is a vote that did not affect the election
    outcome. While the exact definition of a wasted vote varies, we’ll adopt the following definition: in an election
    with 'V' voters, every vote for a losing candidate is wasted (these are called lost votes), and every vote for a
    winning candidate beyond the strict majority of [V/2]+1 votes the candidate needs to win is wasted (these are called
    excess votes). For this problem we’ll consider a two-party system (let’s call the parties A and B) with elections
    that always involve one candidate from each party.

    Let’s illustrate wasted votes with a simple example between two candidates in a district. Suppose that the candidate
     party A receives 100 votes and the candidate for party B receives 200 votes. All 100 votes for party A are wasted
     (lost votes for A), and 49 votes for party B are wasted (excess votes for B). This is because B needs 151
     ([(100+200)/2]+1) votes to win (over A), so the remaining 49 are wasted.

     E(V,wA,wB)=|wA−wB|/V

     A low efficiency gap indicates that the elections are competitive, and that the number of candidates elected from
     each party is representative of the total voting share for each party. When the efficiency gap is high, this can
     be an indication of gerrymandering. Gerrymandering refers to organizing voting districts in a way that favors a
     particular political outcome. Two common ways of doing this are to “pack” similar voters into districts, or “crack”
     them across multiple districts; both ways tend to diminish those voters’ influence in electing candidates they
     would like to win.

    In an election, districts are made up of precincts. A precinct is an indivisible group of voters. The votes for all
    precincts in a district are added together to find the results for that district. In this problem you are given a
    description of a number of precincts: the party vote totals for each precinct, and how those precincts have been
    grouped into districts. For each district, determine the party that wins and the wasted votes for each party. Then
    determine the efficiency gap between the two parties over all the districts.


INPUT:
    The input describes one election. The first line contains two integers P and D, where 1≤P≤10000 and 1≤D≤min(1000,P).
    These indicate, respectively, the number of voting precincts and districts. Following this are P lines describing
    the precincts. Line i contains 3 numbers: the district di that precinct i is assigned to (1≤di≤D), the number of
    votes for the candidate from party A (0≤ai≤100000), and the number of votes for the candidate from party B
    (0≤bi≤100000). It is guaranteed that:

    1) for each precinct i, 0<ai+bi
    2) each district is assigned at least one precinct, and
    3) there are no ties within any district.


OUTPUT:
    For each of the districts from 1 to D, print which party wins (a single character, either A or B). Then print the
    number of wasted votes for party A and for party B, in order. Finally, after reporting on all the districts, print
    the efficiency gap as measured over all the districts. The efficiency gap should be accurate to within an absolute
    error of 10−6.


EXAMPLES:
    (1)
    Input:              Output:
    5 3                 B 100 49
    1 100 200           A 1 197
    2 100 99            A 49 100
    3 100 50            0.1965897693
    3 100 50
    2 100 98

    (2)
    Input:              Output:
    4 4                 A 0 99
    3 100 99            A 0 99
    2 100 99            A 0 99
    1 100 99            A 0 99
    4 100 99            0.4974874372

    (3)
    Input:              Output:
    4 4                 A 0 99
    4 99 100            B 99 0
    1 100 99            A 0 99
    3 100 99            B 99 0
    2 99 100            0.0000000000
"""

import sys

district_map = {}

for i, line in enumerate(sys.stdin):
    if i > 0:
        if len(line) > 0:
            voting_data = line.split(' ')
            if int(voting_data[0]) in district_map:
                district_map[int(voting_data[0])]['A'] += float(voting_data[1])
                district_map[int(voting_data[0])]['B'] += float(voting_data[2])
            else:
                district_map[int(voting_data[0])] = {
                    'A': 0 + float(voting_data[1]),
                    'B': 0 + float(voting_data[2])
                }
    else:
        start_data = line.split(' ')
        P = int(start_data[0])
        D = int(start_data[1])

ordered_district_map = {}
for item in sorted(district_map.items()):
    ordered_district_map[item[0]] = item[1]
district_map = ordered_district_map
district_total = sum(sum(x.values()) for x in district_map.values())
wasted_a_total = 0.0
wasted_b_total = 0.0

for k in district_map:
    party_data = district_map[k]
    # Finding a Winner
    winner = 'A' if party_data['A'] > party_data['B'] else 'B'
    # Finding wasted Votes per precinct
    majority = int(sum(party_data.values()) / 2 + 1)
    if winner == 'A':
        wasted_a = party_data['A'] - majority
        wasted_b = party_data['B']
    else:
        wasted_a = party_data['A']
        wasted_b = party_data['B'] - majority
    wasted_a_total += wasted_a
    wasted_b_total += wasted_b
    print(f"""{winner} {int(wasted_a)} {int(wasted_b)}""")
print("{:.10}".format(abs(wasted_a_total - wasted_b_total) / district_total))