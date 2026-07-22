VERSION 12.6.1.12
SYSTYPE Process
UNITS Millimeters Seconds
SYSDEF UtilByAvail off RefCheck on debugger off warningMessages on report standard
FLAGS
	System Inherit
	Text Red
	Resources Inherit
	Resource Names Red
	Queues Inherit
	Queue Names Red
	Queue Amounts Red
	Blocks Inherit
	Block Names Invisible Red
	Labels Red
PROCDEF
PROC name pStart 0 traf Infinite nextproc die
PROC name pFromTo 0 traf Infinite nextproc die
PROC name pPreFromTo 0 traf Infinite nextproc die
PROC name pMove 0 traf Infinite nextproc die
PROC name pTimeDel 0 traf Infinite nextproc die
LDTYPE name lStart 0
picpos endx 1
 template Millimeters
700 17
2 2 0 1 1 none
1
310 0
1 1 1 1 1 0 0
end
		create con 1 Seconds stream stream_LoadType1_1 First pStart 0 Limit 1
RSRC name rOHT 0 cap 2147483647 prtime con 5 Seconds stream stream_rOHT_1

	UserDef
		
QUEUE name qOut 0 cap 2147483647

	UserDef

BLOCK name Block1472 0 cap 1
	color 0 6
 dis 0 picpos begx 30678.742 begy 23193.906 endx 30679.742 endy 23193.906 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1685 0 cap 1
	color 0 11
 dis 0 picpos begx 31328.742 begy 21243.906 endx 31329.742 endy 21243.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1471 0 cap 1
	color 0 6
 dis 0 picpos begx 30678.742 begy 29185.906 endx 30679.742 endy 29185.906 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1454 0 cap 1
	color 0 14
 dis 0 picpos begx 29628.742 begy 13190.906 endx 29629.742 endy 13190.906 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1348 0 cap 1
	color 0 11
 dis 0 picpos begx 31328.742 begy 27235.906 endx 31329.742 endy 27235.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1461 0 cap 1
	color 0 13
 dis 0 picpos begx 29128.742 begy 37280.904 endx 29129.742 endy 37280.904 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1702 0 cap 1
	color 0 5
 dis 0 picpos begx 57278.744 begy 21093.906 endx 57279.744 endy 21093.906 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1696 0 cap 1
	color 0 12
 dis 0 picpos begx 56628.744 begy 23043.906 endx 56629.744 endy 23043.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1526 0 cap 1
	color 0 12
 dis 0 picpos begx 39851.632 begy 11260.906 endx 39852.632 endy 11260.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1524 0 cap 1
	color 0 11
 dis 0 picpos begx 40451.632 begy 10760.906 endx 40452.632 endy 10760.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1713 0 cap 1
	color 0 11
 dis 0 picpos begx 31978.742 begy 21893.906 endx 31979.742 endy 21893.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1494 0 cap 1
	color 0 11
 dis 0 picpos begx 31558.102 begy 39210.904 endx 31559.102 endy 39210.904 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1435 0 cap 1
	color 0 5
 dis 0 picpos begx 57278.744 begy 27085.906 endx 57279.744 endy 27085.906 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1364 0 cap 1
	color 0 12
 dis 0 picpos begx 56628.744 begy 29035.906 endx 56629.744 endy 29035.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1708 0 cap 1
	color 0 12
 dis 0 picpos begx 43353.744 begy 22393.906 endx 43354.744 endy 22393.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1706 0 cap 1
	color 0 11
 dis 0 picpos begx 43953.744 begy 21893.906 endx 43954.744 endy 21893.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1424 0 cap 1
	color 0 14
 dis 0 picpos begx 58828.744 begy 14646.188 endx 58829.744 endy 14646.188 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1531 0 cap 1
	color 0 11
 dis 0 picpos begx 31978.742 begy 27885.906 endx 31979.742 endy 27885.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1715 0 cap 1
	color 0 12
 dis 0 picpos begx 55978.744 begy 22393.906 endx 55979.744 endy 22393.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1417 0 cap 1
	color 0 13
 dis 0 picpos begx 58328.744 begy 37280.904 endx 58329.744 endy 37280.904 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1522 0 cap 1
	color 0 12
 dis 0 picpos begx 43353.744 begy 28385.906 endx 43354.744 endy 28385.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1520 0 cap 1
	color 0 11
 dis 0 picpos begx 43953.744 begy 27885.906 endx 43954.744 endy 27885.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1405 0 cap 1
	color 0 11
 dis 0 picpos begx 25278.242 begy 10110.906 endx 25279.242 endy 10110.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1308 0 cap 1
	color 0 6
 dis 0 picpos begx 59228.744 begy 11735.906 endx 59229.744 endy 11735.906 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1533 0 cap 1
	color 0 12
 dis 0 picpos begx 55978.744 begy 28385.906 endx 55979.744 endy 28385.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1535 0 cap 1
	color 0 11
 dis 0 picpos begx 44278.744 begy 39210.904 endx 44279.744 endy 39210.904 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1537 0 cap 1
	color 0 12
 dis 0 picpos begx 43678.744 begy 39710.904 endx 43679.744 endy 39710.904 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1506 0 cap 1
	color 0 12
 dis 0 picpos begx 56398.744 begy 39710.904 endx 56399.744 endy 39710.904 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1433 0 cap 1
	color 0 6
 dis 0 picpos begx 59878.744 begy 13735.906 endx 59879.744 endy 13735.906 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1399 0 cap 1
	color 0 11
 dis 0 picpos begx 21068.71 begy 9460.906 endx 21069.71 endy 9460.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block40 0 cap 1
	color 0 5
 dis 0 picpos begx 104396.736 begy 8535.906 endx 104397.736 endy 8535.906 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block412 0 cap 1
	color 0 13
 dis 0 picpos begx 105446.736 begy 23569.812 endx 105447.736 endy 23569.812 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block366 0 cap 1
	color 0 13
 dis 0 picpos begx 105446.736 begy -1614.109375 endx 105447.736 endy -1614.109375 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block362 0 cap 1
	color 0 14
 dis 0 picpos begx 105946.736 begy -1014.109375 endx 105947.736 endy -1014.109375 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block408 0 cap 1
	color 0 14
 dis 0 picpos begx 105946.736 begy 24169.812 endx 105947.736 endy 24169.812 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block355 0 cap 1
	color 0 13
 dis 0 picpos begx 105446.736 begy -27318.86 endx 105447.736 endy -27318.86 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block346 0 cap 1
	color 0 14
 dis 0 picpos begx 105946.736 begy -26718.86 endx 105947.736 endy -26718.86 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4 0 cap 1
	color 0 13
 dis 0 picpos begx 106748.736 begy 56334.904 endx 106749.736 endy 56334.904 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block43 0 cap 1
	color 0 5
 dis 0 picpos begx 104396.736 begy -59989.096 endx 104397.736 endy -59989.096 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block12 0 cap 1
	color 0 13
 dis 0 picpos begx 106748.736 begy 82934.912 endx 106749.736 endy 82934.912 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1 0 cap 1
	color 0 14
 dis 0 picpos begx 107248.736 begy 56934.904 endx 107249.736 endy 56934.904 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block339 0 cap 1
	color 0 13
 dis 0 picpos begx 105446.736 begy -47908.088 endx 105447.736 endy -47908.088 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block330 0 cap 1
	color 0 14
 dis 0 picpos begx 105946.736 begy -47308.088 endx 105947.736 endy -47308.088 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block15 0 cap 1
	color 0 14
 dis 0 picpos begx 109129.744 begy 83534.912 endx 109130.744 endy 83534.912 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1554 0 cap 1
	color 0 14
 dis 0 picpos begx 57827.744 begy -62139.096 endx 57828.744 endy -62139.096 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1626 0 cap 1
	color 0 12
 dis 0 picpos begx 61492.54 begy -56939.096 endx 61493.54 endy -56939.096 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block379 0 cap 1
	color 0 13
 dis 0 picpos begx 105446.736 begy -82104.336 endx 105447.736 endy -82104.336 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block386 0 cap 1
	color 0 14
 dis 0 picpos begx 105946.736 begy -81504.336 endx 105947.736 endy -81504.336 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block198 0 cap 1
	color 0 12
 dis 0 picpos begx 109379.744 begy 99584.92 endx 109380.744 endy 99584.92 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1629 0 cap 1
	color 0 14
 dis 0 picpos begx 57827.744 begy -68409.088 endx 57828.744 endy -68409.088 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1607 0 cap 1
	color 0 13
 dis 0 picpos begx 54286.744 begy -62939.096 endx 54287.744 endy -62939.096 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block437 0 cap 1
	color 0 5
 dis 0 picpos begx 107780.736 begy -46396.124 endx 107781.736 endy -46396.124 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1770 0 cap 1
	color 0 11
 dis 0 picpos begx 37478.744 begy -61239.096 endx 37479.744 endy -61239.096 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1837 0 cap 1
	color 0 14
 dis 0 picpos begx 57827.744 begy -73223.056 endx 57828.744 endy -73223.056 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1120 0 cap 1
	color 0 13
 dis 0 picpos begx 105326.736 begy 121982.92 endx 105327.736 endy 121982.92 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1599 0 cap 1
	color 0 11
 dis 0 picpos begx 25278.228 begy -61889.096 endx 25279.228 endy -61889.096 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1577 0 cap 1
	color 0 3
 dis 0 picpos begx 44128.744 begy -62289.096 endx 44129.744 endy -62289.096 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1582 0 cap 1
	color 0 11
 dis 0 picpos begx 20923.836 begy -62539.096 endx 20924.836 endy -62539.096 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block421 0 cap 1
	color 0 13
 dis 0 picpos begx 105446.736 begy -99642.888 endx 105447.736 endy -99642.888 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block422 0 cap 1
	color 0 14
 dis 0 picpos begx 105946.736 begy -99042.896 endx 105947.736 endy -99042.896 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1118 0 cap 1
	color 0 14
 dis 0 picpos begx 105826.736 begy 122582.92 endx 105827.736 endy 122582.92 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1614 0 cap 1
	color 0 13
 dis 0 picpos begx 43078.744 begy -62939.096 endx 43079.744 endy -62939.096 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1589 0 cap 1
	color 0 11
 dis 0 picpos begx 53386.744 begy -79939.088 endx 53387.744 endy -79939.088 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1588 0 cap 1
	color 0 11
 dis 0 picpos begx 50528.744 begy -79939.088 endx 50529.744 endy -79939.088 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block441 0 cap 1
	color 0 5
 dis 0 picpos begx 107780.736 begy -115095.184 endx 107781.736 endy -115095.184 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1104 0 cap 1
	color 0 13
 dis 0 picpos begx 105326.736 begy 145685.888 endx 105327.736 endy 145685.888 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block395 0 cap 1
	color 0 13
 dis 0 picpos begx 105446.736 begy -116616.696 endx 105447.736 endy -116616.696 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block396 0 cap 1
	color 0 14
 dis 0 picpos begx 105946.736 begy -116016.696 endx 105947.736 endy -116016.696 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1821 0 cap 1
	color 0 14
 dis 0 picpos begx 46370.744 begy -73224.16 endx 46371.744 endy -73224.16 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block190 0 cap 1
	color 0 13
 dis 0 picpos begx 112888.736 begy 121982.92 endx 112889.736 endy 121982.92 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block188 0 cap 1
	color 0 14
 dis 0 picpos begx 113388.736 begy 122582.92 endx 113389.736 endy 122582.92 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1102 0 cap 1
	color 0 14
 dis 0 picpos begx 105826.736 begy 146285.888 endx 105827.736 endy 146285.888 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block450 0 cap 1
	color 0 12
 dis 0 picpos begx 114288.736 begy 165684.928 endx 114289.736 endy 165684.928 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1219 0 cap 1
	color 0 12
 dis 0 picpos begx 106726.736 begy 165684.928 endx 106727.736 endy 165684.928 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1224 0 cap 1
	color 0 13
 dis 0 picpos begx 105326.736 begy 165284.928 endx 105327.736 endy 165284.928 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1204 0 cap 1
	color 0 14
 dis 0 picpos begx 105946.736 begy -136610.976 endx 105947.736 endy -136610.976 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block172 0 cap 1
	color 0 14
 dis 0 picpos begx 113388.736 begy 146285.888 endx 113389.736 endy 146285.888 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block174 0 cap 1
	color 0 13
 dis 0 picpos begx 112888.736 begy 145685.888 endx 112889.736 endy 145685.888 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1203 0 cap 1
	color 0 13
 dis 0 picpos begx 105446.736 begy -137210.976 endx 105447.736 endy -137210.976 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block991 0 cap 1
	color 0 14
 dis 0 picpos begx -75296.368 begy -99042.896 endx -75295.368 endy -99042.896 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1010 0 cap 1
	color 0 5
 dis 0 picpos begx -73462.36 begy -115095.184 endx -73461.36 endy -115095.184 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block990 0 cap 1
	color 0 13
 dis 0 picpos begx -75796.368 begy -99642.888 endx -75795.368 endy -99642.888 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block955 0 cap 1
	color 0 14
 dis 0 picpos begx -75296.368 begy -81504.336 endx -75295.368 endy -81504.336 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block948 0 cap 1
	color 0 13
 dis 0 picpos begx -75796.368 begy -82104.336 endx -75795.368 endy -82104.336 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block965 0 cap 1
	color 0 14
 dis 0 picpos begx -75296.368 begy -116016.696 endx -75295.368 endy -116016.696 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1006 0 cap 1
	color 0 5
 dis 0 picpos begx -73462.368 begy -46396.124 endx -73461.368 endy -46396.124 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block964 0 cap 1
	color 0 13
 dis 0 picpos begx -75796.368 begy -116616.696 endx -75795.368 endy -116616.696 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block899 0 cap 1
	color 0 14
 dis 0 picpos begx -75296.368 begy -47308.088 endx -75295.368 endy -47308.088 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1283 0 cap 1
	color 0 14
 dis 0 picpos begx -75296.36 begy -136610.976 endx -75295.36 endy -136610.976 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block915 0 cap 1
	color 0 14
 dis 0 picpos begx -75296.368 begy -26718.86 endx -75295.368 endy -26718.86 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block924 0 cap 1
	color 0 13
 dis 0 picpos begx -75796.368 begy -27318.86 endx -75795.368 endy -27318.86 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1282 0 cap 1
	color 0 13
 dis 0 picpos begx -75796.36 begy -137210.976 endx -75795.36 endy -137210.976 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block504 0 cap 1
	color 0 5
 dis 0 picpos begx -76846.368 begy -60989.096 endx -76845.368 endy -60989.096 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block931 0 cap 1
	color 0 14
 dis 0 picpos begx -75296.368 begy -1014.109375 endx -75295.368 endy -1014.109375 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block935 0 cap 1
	color 0 13
 dis 0 picpos begx -75796.368 begy -1614.109375 endx -75795.368 endy -1614.109375 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1856 0 cap 1
	color 0 11
 dis 0 picpos begx -83039.376 begy -60839.096 endx -83038.376 endy -60839.096 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block977 0 cap 1
	color 0 14
 dis 0 picpos begx -75296.368 begy 24169.812 endx -75295.368 endy 24169.812 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block981 0 cap 1
	color 0 13
 dis 0 picpos begx -75796.368 begy 23569.812 endx -75795.368 endy 23569.812 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block502 0 cap 1
	color 0 5
 dis 0 picpos begx -76846.368 begy 7535.906 endx -76845.368 endy 7535.906 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block466 0 cap 1
	color 0 13
 dis 0 picpos begx -74494.368 begy 56334.904 endx -74493.368 endy 56334.904 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block463 0 cap 1
	color 0 14
 dis 0 picpos begx -73994.368 begy 56934.904 endx -73993.368 endy 56934.904 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1862 0 cap 1
	color 0 11
 dis 0 picpos begx -83039.376 begy 7685.906 endx -83038.376 endy 7685.906 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block474 0 cap 1
	color 0 13
 dis 0 picpos begx -74494.368 begy 82934.912 endx -74493.368 endy 82934.912 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block477 0 cap 1
	color 0 14
 dis 0 picpos begx -72113.368 begy 83534.912 endx -72112.368 endy 83534.912 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block769 0 cap 1
	color 0 12
 dis 0 picpos begx -71863.368 begy 99584.92 endx -71862.368 endy 99584.92 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1021 0 cap 1
	color 0 12
 dis 0 picpos begx -66954.368 begy 165684.928 endx -66953.368 endy 165684.928 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block755 0 cap 1
	color 0 14
 dis 0 picpos begx -67854.368 begy 122582.92 endx -67853.368 endy 122582.92 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block757 0 cap 1
	color 0 13
 dis 0 picpos begx -68354.368 begy 121982.92 endx -68353.368 endy 121982.92 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block723 0 cap 1
	color 0 14
 dis 0 picpos begx -67854.368 begy 146285.888 endx -67853.368 endy 146285.888 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block725 0 cap 1
	color 0 13
 dis 0 picpos begx -68354.368 begy 145685.888 endx -68353.368 endy 145685.888 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block759 0 cap 1
	color 0 14
 dis 0 picpos begx -75416.368 begy 122582.92 endx -75415.368 endy 122582.92 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block761 0 cap 1
	color 0 13
 dis 0 picpos begx -75916.368 begy 121982.92 endx -75915.368 endy 121982.92 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block727 0 cap 1
	color 0 14
 dis 0 picpos begx -75416.368 begy 146285.888 endx -75415.368 endy 146285.888 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block729 0 cap 1
	color 0 13
 dis 0 picpos begx -75916.368 begy 145685.888 endx -75915.368 endy 145685.888 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1020 0 cap 1
	color 0 12
 dis 0 picpos begx -74516.368 begy 165684.928 endx -74515.368 endy 165684.928 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1030 0 cap 1
	color 0 13
 dis 0 picpos begx -75916.368 begy 165284.928 endx -75915.368 endy 165284.928 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
COUNT name cWIP 0 cap Infinite
ATT name larLotPerHour 0 type Real
ATT name lapFromEq 0 type Location
ATT name lapToEq 0 type Location
VAR name vVehicleOrTime 0 type Integer
VAR name vParkLocFoup 0 type Location
VAR name vParkListFoup 0 type LocationList
VAR name vfpRead 0 type FilePtr
VAR name vi 0 type Integer
VAR name vStrTmp 0 type String
VAR name vFromEqsName 0 type String
VAR name vToEqsName 0 type String
VAR name vLotPerHour 0 type Real
VAR name vFromToCnt 0 type Real
VAR name vInitDel_Time 0 type Integer
VAR name vOHTDel_Time 0 type Integer
RNSTREAM stream0 0 type CMRG flags 1
	cmrgseed 1 12345 12345 12345 12345 12345 12345
RNSTREAM stream_LoadType1_1 0 type CMRG flags 1
	title "Generated automatically for LoadType1"
	cmrgseed 1 3692455944 1366884236 2968912127 335948734 4161675175 475798818
RNSTREAM stream_rOHT_1 0 type CMRG flags 1
	title "Generated automatically for rOHT"
	cmrgseed 1 1015873554 1310354410 2249465273 994084013 2912484720 3876682925
RNSTATE 2338701263 1119171942 2570676563 317077452 3194180850 618832124
SFileBegin	name vehicle.m
begin pm park ok function
	if vVehicleOrTime = 1 then
	begin
		if theVehicle type = "DefVehicle" then
		begin
			if theVehicle current distance parkLoc > 50000 mm then
			begin
				if parkLoc current > 1 then 
					return false
					
				for each vParkLocFoup in vParkListFoup do
				begin
					if vParkLocFoup = parkLoc then return false
				end
				
				insert parkLoc into vParkListFoup at end
				
				if vParkListFoup size > 1 then
					remove first object from vParkListFoup
				
				set theVehicle color to blue
				return true
			end
			
			return false
		end
		
		return false
	end
	return false
end

begin pm work ok function
	set theVehicle color to red
	return true
end

#@!
SFileBegin	name init.m
begin model initialization function

	set vVehicleOrTime = 0 /* Time 반송 = 0, Vehicle 반송 = 1 */
	set vInitDel_Time = 86400*15
	set vOHTDel_Time = 150
	return true

end

#@!
SFileBegin	name logic.m
begin pStart arriving
    
    clone 1 load to pTimeDel
	/*변수 설정*/
	open "arc/eqToeq.dat" for reading save result as vfpRead
	
	/*fromto 파일 읽어들이기*/
	set vi to 1
	while vfpRead eof = 0 do
	begin
		read vStrTmp from vfpRead with delimiter "\n"
		read vFromEqsName, vToEqsName,	vLotPerHour from vStrTmp with delimiter "\t"
			/*
			vFromEqsName = From 설비군 명(Str)  
			vToEqsName = To 설비군 명(Str)
			vLotPerHour = 시간당 Lot 수(int)
			*/
		
		if vFromEqsName index("-") <= vFromEqsName length then
			set vFromEqsName substring(vFromEqsName index("-"), 1) = "_"
			
		if vToEqsName index("-") <= vToEqsName length then
			set vToEqsName substring(vToEqsName index("-"), 1) = "_"
			
		if vFromEqsName substring(1,1) <> "*" then
		begin		
			print "pm:cp_"vFromEqsName to vStrTmp
			set lapFromEq to vStrTmp
			print "pm:cp_"vToEqsName to vStrTmp
			set lapToEq to vStrTmp
			set larLotPerHour to vLotPerHour
			clone 1 load to pPreFromTo
				
/*			wait for 86400 * 3.0 / vFromToCnt sec	*/
/*			wait for (1 + 86400 * 15.0 * u 0.5, 0.5) sec	*/
			wait for 0.1 sec
			inc vi by 1
		end
		else
		begin
			if vFromEqsName substring(1,6) = "* From" then
			begin
				set vFromToCnt to vLotPerHour
			end
		end
		
	end

end

begin pPreFromTo arriving
	wait for (1 + 86400 * 15.0 * u 0.5, 0.5) sec
	clone 1 load to pFromTo
end

begin pFromTo arriving
	while 1 = 1 do
	begin
		clone 1 load to pMove
		wait for n 60*60 / larLotPerHour, 60*60 / (larLotPerHour * 10) sec
	end
end



begin pMove arriving
	if lapFromEq <> null and lapToEq <> null then
	begin
		inc cWIP by 1
		if vVehicleOrTime = 1 then
		begin
    		move into lapFromEq
    		travel to lapToEq
    	end
    	else
    	begin
    		use rOHT for vOHTDel_Time sec
    	end
    	
		dec cWIP by 1
		move into qOut	
	end
	
end

begin pTimeDel arriving
    wait for vInitDel_Time sec
    set vVehicleOrTime = 1
end

#@!
