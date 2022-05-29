#### Details about the provided dataset
###### Electrical Load Measurements
- Spikes of greater than 4000 Watts have been removed from the Individual Appliance Monitor (IAM) values and replaced with zeros. 
- There is also an additional issues column which is set to 1 if the sum of the sub-metering (IAMs) is greater than that of the household aggregate. In these cases the data should be discarded or noted that there is a discrepancy.

INFORMATION
Collection of this dataset was supported by the Engineering and Physical Sciences Research Council (EPSRC) via the project entitled Personalised Retrofit Decision Support Tools for UK Homes using Smart Home Technology (REFIT), which is a collaboration among the Universities of Strathclyde, Loughborough and East Anglia. The dataset includes data from 20 households from the Loughborough area over the period 2013 – 2014.  Additional information about REFIT is available from www.refitsmarthomes.org.

LICENCING
This work is licensed under the Creative Commons Attribution 4.0 International Public License. See https://creativecommons.org/licenses/by/4.0/legalcode for further details.
Please cite the following paper if you use the dataset:

@inbook{278e1df91d22494f9be2adfca2559f92,
title = "A data management platform for personalised real-time energy feedback",
keywords = "smart homes, real-time energy, smart energy meter, energy consumption, Electrical engineering. Electronics Nuclear engineering, Electrical and Electronic Engineering",
author = "David Murray and Jing Liao and Lina Stankovic and Vladimir Stankovic and Richard Hauxwell-Baldwin and Charlie Wilson and Michael Coleman and Tom Kane and Steven Firth",
year = "2015",
booktitle = "Proceedings of the 8th International Conference on Energy Efficiency in Domestic Appliances and Lighting",
}

Each of the houses is labelled, House 1 - House 21 (skipping House 14), each house has 10 power sensors comprising a current clamp for the household aggregate and 9 Individual Appliance Monitors (IAMs). Only active power in Watts is collected at 8-second interval.
The subset of all appliances in a household that was monitored reflects the document from DECC of the largest consumers in UK households, https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/274778/9_Domestic_appliances__cooking_and_cooling_equipment.pdf

FILE FORMAT
The file format is csv and is laid out as follows;
DATETIME, UNIX TIMESTAMP (UCT), Aggregate, Appliance1, Appliance2, Appliance3, ... , Appliance9, Issues
Additionally data was only recorded when there was a change in load; this data has been filled with intermediate values where not available. 


The sensors are also not synchronised as our collection script polled every 6-8 seconds; the sensor may have updated anywhere in the last 6-8 seconds.




The file name _Part1 refers to the first iteration of the database where sensors that were not available were set to 0.
The file name _Part2 refers to the second iteration of the database where sensors that were not available were set to NaN to distinguish from 0.

MISSING DATA
During the course of the study there are a few periods of missing data (notably February 2014). Outages were due to a number of factors, including household internet failure, hardware failures, network routing issues, etc.

Household Information
House, Occupancy, Construction Year, Appliances Owned, Type, Size
1	,	2	,	1975-1980				, 35 , Detached			, 4 bed
2	,	4	,	-						, 15 , Semi-detached	, 3 bed
3	,	2	,	1988					, 27 , Detached			, 3 bed
4	,	2	,	1850-1899 				, 33 , Detached			, 4 bed
5	,	4	,	1878					, 44 , Mid-terrace		, 4 bed
6	,	2	,	2005					, 49 , Detached			, 4 bed
7	,	4	,	1965-1974				, 25 , Detached			, 3 bed
8	,	2	,	1966					, 35 , Detached			, 2 bed
9	,	2	,	1919-1944				, 24 , Detached			, 3 bed
10	,	4	,	1919-1944				, 31 , Detached			, 3 bed
11	,	1	,	1945-1964				, 25 , Detached			, 3 bed
12	,	3	,	1991-1995				, 26 , Detached			, 3 bed
13	,	4	,	post 2002				, 28 , Detached			, 4 bed
15	,	1	,	1965-1974				, 19 , Semi-detached	, 3 bed
16	,	6	,	1981-1990				, 48 , Detached			, 5 bed
17	,	3	,	mid 60s					, 22 , Detached			, 3 bed
18	,	2	,	1965-1974				, 34 , Detached			, 3 bed
19	,	4	,	1945-1964				, 26 , Semi-detached	, 3 bed
20	,	2	,	1965-1974				, 39 , Detached			, 3 bed
21	,	4	,	1981-1990				, 23 , Detached			, 3 bed

APPLIANCE LIST
The following list shows the appliances that were known to be monitored at the beginning of the study period. Although occupants were asked not to remove or switch appliances monitored by the IAMs, we cannot guarantee this to be the case. It should also be noted that Television and Computer Site may consist of multiple appliances, e.g. Television, SkyBox, DvD Player, Computer, Speakers, etc. Makes and Models specified here are gathered from pictures gathered by the installation team.

House 1
- Aggregate
- Fridge, Hotpoint, RLA50P
- Freezer(1),Beko, CF393APW
- Freezer(2), Unknown, Unknown
- Washer Dryer, Creda, T522VW
- Washing Machine, Beko, WMC6140
- Dishwasher, Bosch, Unknown
- Computer, Lenovo, H520s
- Television Site, Toshiba, 32BL502b
- Electric Heater, GLEN, 2172

House 2
- Aggregate,
- Fridge-Freezer, Unknown, Unknown
- Washing Machine, LG, F1289TD
- Dishwasher, Unknown, Unknown
- Television Site,
- Microwave, Unknown, Unknown
- Toaster, Unknown, Unknown
- Hi-Fi, Unknown, Unknown
- Kettle, Unknown, Unknown
- Overhead Fan

House 3
-  Aggregate,
-  Toaster, Dualit, DPP2
-  Fridge-Freezer, Whirlpool, ARC7612
-  Freezer, Frigidaire, Freezer Elite
-  Tumble Dryer, Unknown, Unknown
-  Dishwasher, Bosch, Exxcel Auto Option
-  Washing Machine, Unknown, Unknown
-  Television Site, Samsung, LE46A656A1FXXU
-  Microwave, Panasoinc, NN-CT565MBPQ
-  Kettle, Dualit, JKt3 (Kettle changed 16 Apr 2014 - Jan 19 2015 Vektra Vacuum Kettle)

House 4
- Aggregate,
- Fridge, Neff, K1514X0GB/31
- Freezer, Ocean, UF 1025
- Fridge-Freezer, Ariston, DF230, (change Aug 17 2014)
- Washing Machine(1), Servis, 6065
- Washing Machine(2), Zanussi, Z917
- Desktop Computer, Unknown, Unknown
- Television Site, Sony, KDL-32W706B, (change at 19 Dec 2014)
- Microwave, Matsui, 170TC
- Kettle, Swan, Unknown

House 5
- Aggregate,
- Fridge-Freezer, Fisher & Paykel, Unknown
- Tumble Dryer, Unknown, Unknown
- Washing Machine, AEG, L99695HWD
- Dishwasher, Unknown, Unknown
- Desktop Computer, Unknown, Unknown, (change 17 Mar 2015)
- Television Site, Unknown, Unknown
- Microwave, Unknown, Unknown
- Kettle, Logik, L17SKC14
- Toaster, Breville, TT33

House 6
- Aggregate,
- Freezer, Whirlpool, CV128W
- Washing Machine, Bosch, Classixx 1200 Express
- Dishwasher, Neff, Unknown
- MJY Computer, Unknown, Unknown
- TV/Satellite, Samsung, UE55F6500SB
- Microwave, Neff, H5642N0GB/02
- Kettle, ASDA, GPK101W
- Toaster, Breville, PT15
- PGM Computer, Unknown, Unknown

House 7
- Aggregate,
- Fridge, Bosch, KSR30422GB
- Freezer(1), Whirlpool, AFG 392/H
- Freezer(2), Unknown, Unknown, (Change 23 Nov 2013)
- Tumble Dryer, White Knight, Unknown
- Washing Machine, Bosch, Unknown
- Dishwasher, Unknown, Unknown, (Change 20 May 2014)
- Television Site,
- Toaster, Unknown, Unknown
- Kettle, Sainsburys, 121988254

House 8
- Aggregate,
- Fridge, Liebherr, KP2620
- Freezer, Unknown, Unknown
- Washer Dryer, Zanussi, Unknown
- Washing Machine,
- Toaster, Bosch, TAT6101GB/02
- Computer, Unknown, Unknown
- Television Site, Sony, KDL-32V2000
- Microwave, Panasoinc, NN-CT565MBPQ
- Kettle, Morphy Richards, 43615

House 9
- Aggregate,
- Fridge-Freezer, Bosch, KGH34X05GB/05
- Washer Dryer, Hotpoint, TCM580
- Washing Machine, Bosch, Classixx 6 1200 Express
- Dishwasher, Bosch, Classixx
- Television Site, LG, 32LH3000
- Microwave, Argos, MM717CFA
- Kettle, Russel Hobbs, Unknown
- Hi-Fi, Unknown, Unknown
- Electric Heater

House 10
- Aggregate,
- Magimix(Blender), Unknown, Unknown, (Change 17 Jun 2014)
- Toaster, Unknown, Unknown, (Change 17 Oct 2014)
- Chest Freezer, Unknown, Unknown
- Fridge-Freezer, Unknown, Unknown
- Washing Machine, Beko, WI1382
- Dishwasher, AEG, Unknown
- Television Site, Samsung, UE40ES5500K
- Microwave, Unknown, Unknown
- K Mix, Unknown, Unknown

House 11
- Aggregate,
- Fridge, Gorenje, HPI 1566, (Starts 7 Oct 2014)
- Fridge-Freezer, Unknown, Unknown
- Washing Machine, Unknown, Unknown
- Dishwasher, Unknown, Unknown, (Change 4 Oct 2014)
- Computer Site, Unknown, Unknown
- Microwave, Unknown, Unknown
- Kettle, Unknown, Unknown
- Router, Unknown, Unknown
- Hi-Fi, Unknown, Unknown

House 12
- Aggregate,
- Fridge-Freezer, Gorenje, HZS 3266
- ???, Unknown, Unknown
- ???, Unknown, Unknown
- Computer Site, Unknown, Unknown
- Microwave, Unknown, Unknown
- Kettle, Unknown, Unknown
- Toaster, Unknown, Unknown, (Nothing Recorded)
- Television, Unknown, Unknown, (Nothing Recorded)
- ???, Unknown, Unknown, (Nothing Recorded)

House 13
- Aggregate,
- Television Site, Samsung, UE55H6400AK
- Freezer, Unknown, Unknown, (Stops 18 Aug 2014)
- Washing Machine, Unknown, Unknown, (Changes 25 Mar 2015)
- Dishwasher, Unknown, Unknown
- ???, Unknown, Unknown
- Network Site, Unknown, Unknown
- Microwave, Unknown, Unknown
- Microwave, Unknown, Unknown
- Kettle, Unknown, Unknown

House 15
- Aggregate,
- Fridge-Freezer, Unknown, Unknown
- Tumble Dryer, Unknown, Unknown
- Washing Machine, Beko, WMB91242LB
- Dishwasher, Unknown, Unknown
- Computer Site, Unknown, Unknown
- Television Site, LG, 22LS4D
- Microwave, Unknown, Unknown
- Hi-Fi, Unknown, Unknown
- Toaster, Unknown, Unknown

House 16
- Aggregate,
- Fridge-Freezer(1), Bosch, KGN30VW20G/01, (Change 7 Apr 2015)
- Fridge-Freezer(2), Unknown, Unknown
- Electric Heater(1), Unknown, Unknown
- Electric Heater(2), Unknown, Unknown
- Washing Machine, Bosch, WAB24262GB/01
- Dishwasher, Unknown, Unknown
- Computer Site, Unknown, Unknown
- Television Site, Samsung, UE55HU8500T
- Dehumidifier, Unknown, Unknown

House 17
- Aggregate,
- Freezer, Unknown, Unknown
- Fridge-Freezer, Whirlpool, ARC 2990
- Tumble Dryer, Unknown, Unknown
- Washing Machine, Bosch, Exxcel 8 Vario Perfect
- Computer Site, Unknown, Unknown
- Television Site, Unknown, Unknown
- Microwave, Matsui, M195T
- Kettle, Russel Hobbs, 17869
- TV Site(Bedroom), Unknown, Unknown

House 18
- Aggregate,
- Fridge(garage), LEC, R.403W
- Freezer(garage), Unknown, Unknown
- Fridge-Freezer, Unknown, Unknown
- Washer Dryer(garage), Unknown, Unknown
- Washing Machine, Unknown, Unknown
- Dishwasher, Unknown, Unknown
- Desktop Computer, Unknown, Unknown
- Television Site, Unknown, Unknown
- Microwave, Unknown, Unknown

House 19
- Aggregate,
- Fridge Freezer, Bosch, KGS-3272-GB/01
- Washing Machine, Bosch, WAE24060GB/03
- Television Site, Sony, KDL32EX703
- Microwave, Kenwood, K20MSS10
- Kettle, Breville, VKJ336
- Toaster, Bellini, BET240
- Bread-maker, Unknown, Unknown
- Games Console, Unknown, Unknown
- Hi-Fi, Unknown, Unknown

House 20
- Aggregate,
- Fridge, Unknown, Unknown
- Freezer, Unknown, Unknown
- Tumble Dryer, Unknown, Unknown
- Washing Machine, Unknown, Unknown
- Dishwasher, Unknown, Unknown
- Computer Site, Unknown, Unknown
- Television Site, Unknown, Unknown
- Microwave, Unknown, Unknown
- Kettle, Unknown, Unknown

House 21
- Aggregate,
- Fridge-Freezer, Samsung, SR-L3216B
- Tumble Dryer, Unknown, Unknown
- Washing Machine, Beko, WMB81241LW
- Dishwasher, AEG, FAVORIT
- Food Mixer, Unknown, Unknown
- Television, Unknown, Unknown
- Kettle, Unknown, Unknown, (Changes 16 Aug 2014)
- Vivarium, Unknown, Unknown
- Pond Pump, Unknown, Unknown
