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

BLOCK name Block6930 0 cap 1
	color 0 6
 dis 0 picpos begx -78445.136 begy -21003.5 endx -78444.136 endy -21003.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6987 0 cap 1
	color 0 14
 dis 0 picpos begx -78845.136 begy -7048.7345 endx -78844.136 endy -7048.7345 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6926 0 cap 1
	color 0 5
 dis 0 picpos begx -77345.136 begy -21603.5 endx -77344.136 endy -21603.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6925 0 cap 1
	color 0 5
 dis 0 picpos begx -77345.136 begy -2469.5 endx -77344.136 endy -2469.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6917 0 cap 1
	color 0 6
 dis 0 picpos begx -78445.136 begy -40137.496 endx -78444.136 endy -40137.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5751 0 cap 1
	color 0 12
 dis 0 picpos begx -78595.136 begy 1680.5 endx -78594.136 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5750 0 cap 1
	color 0 5
 dis 0 picpos begx -76345.136 begy 1030.5 endx -76344.136 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5056 0 cap 1
	color 0 12
 dis 0 picpos begx -66674.056 begy 1680.5 endx -66673.056 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5058 0 cap 1
	color 0 6
 dis 0 picpos begx -78445.136 begy -43637.496 endx -78444.136 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5755 0 cap 1
	color 0 12
 dis 0 picpos begx -89968.552 begy 1680.5 endx -89967.552 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5037 0 cap 1
	color 0 11
 dis 0 picpos begx -76195.136 begy -44287.496 endx -76194.136 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4570 0 cap 1
	color 0 12
 dis 0 picpos begx -54288.272 begy 1680.5 endx -54287.272 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5009 0 cap 1
	color 0 5
 dis 0 picpos begx -64524.056 begy 1030.5 endx -64523.056 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4862 0 cap 1
	color 0 5
 dis 0 picpos begx -87718.552 begy 1030.5 endx -87717.552 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block470 0 cap 1
	color 0 4
 dis 0 picpos begx -80940.512 begy 2730.5 endx -80939.512 endy 2730.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5753 0 cap 1
	color 0 11
 dis 0 picpos begx -87568.552 begy -44287.496 endx -87567.552 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block468 0 cap 1
	color 0 3
 dis 0 picpos begx -80340.512 begy 4030.5 endx -80339.512 endy 4030.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5778 0 cap 1
	color 0 12
 dis 0 picpos begx -100953.28 begy 1680.5 endx -100952.28 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6908 0 cap 1
	color 0 5
 dis 0 picpos begx -87718.552 begy -2349.5 endx -87717.552 endy -2349.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block476 0 cap 1
	color 0 4
 dis 0 picpos begx -40657.752 begy 2730.5 endx -40656.752 endy 2730.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6817 0 cap 1
	color 0 12
 dis 0 picpos begx -42639.876 begy 1680.5 endx -42638.876 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7033 0 cap 1
	color 0 5
 dis 0 picpos begx -51788.272 begy 1030.5 endx -51787.272 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6949 0 cap 1
	color 0 5
 dis 0 picpos begx -65524.056 begy -2469.5 endx -65523.056 endy -2469.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4863 0 cap 1
	color 0 5
 dis 0 picpos begx -98803.28 begy 1030.5 endx -98802.28 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5146 0 cap 1
	color 0 11
 dis 0 picpos begx -64374.056 begy -44287.496 endx -64373.056 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5008 0 cap 1
	color 0 6
 dis 0 picpos begx -66524.056 begy -43637.496 endx -66523.056 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5754 0 cap 1
	color 0 6
 dis 0 picpos begx -89818.552 begy -43637.496 endx -89817.552 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7261 0 cap 1
	color 0 14
 dis 0 picpos begx -54538.272 begy -6073.5 endx -54537.272 endy -6073.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block595 0 cap 1
	color 0 3
 dis 0 picpos begx -110684.04 begy 3380.50775 endx -110683.04 endy 3380.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5835 0 cap 1
	color 0 12
 dis 0 picpos begx -112503.272 begy 1680.5 endx -112502.272 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2542 0 cap 1
	color 0 3
 dis 0 picpos begx -77384.768 begy -45337.496 endx -77383.768 endy -45337.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5777 0 cap 1
	color 0 11
 dis 0 picpos begx -98653.28 begy -44287.496 endx -98652.28 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2544 0 cap 1
	color 0 4
 dis 0 picpos begx -77984.768 begy -45837.496 endx -77983.768 endy -45837.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block474 0 cap 1
	color 0 3
 dis 0 picpos begx -40057.752 begy 4030.5 endx -40056.752 endy 4030.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6833 0 cap 1
	color 0 12
 dis 0 picpos begx -29504.556 begy 1680.5 endx -29503.556 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5188 0 cap 1
	color 0 5
 dis 0 picpos begx -40489.876 begy 1030.5 endx -40488.876 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5838 0 cap 1
	color 0 5
 dis 0 picpos begx -110253.272 begy 1030.5 endx -110252.272 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7063 0 cap 1
	color 0 11
 dis 0 picpos begx -51638.272 begy -44287.496 endx -51637.272 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6950 0 cap 1
	color 0 5
 dis 0 picpos begx -65524.056 begy -21603.5 endx -65523.056 endy -21603.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block463 0 cap 1
	color 0 3
 dis 0 picpos begx -121393.272 begy 4030.5 endx -121392.272 endy 4030.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6876 0 cap 1
	color 0 5
 dis 0 picpos begx -99803.28 begy -2339.5 endx -99802.28 endy -2339.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6903 0 cap 1
	color 0 6
 dis 0 picpos begx -88818.552 begy -20933.5 endx -88817.552 endy -20933.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7245 0 cap 1
	color 0 6
 dis 0 picpos begx -54138.272 begy -43637.496 endx -54137.272 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6900 0 cap 1
	color 0 6
 dis 0 picpos begx -88818.552 begy -40137.496 endx -88817.552 endy -40137.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4630 0 cap 1
	color 0 11
 dis 0 picpos begx -80547.368 begy 5080.5 endx -80546.368 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6954 0 cap 1
	color 0 6
 dis 0 picpos begx -66524.056 begy -21003.5 endx -66523.056 endy -21003.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5879 0 cap 1
	color 0 12
 dis 0 picpos begx -119466.016 begy 1680.5 endx -119465.016 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6941 0 cap 1
	color 0 6
 dis 0 picpos begx -66524.056 begy -40137.496 endx -66523.056 endy -40137.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5831 0 cap 1
	color 0 11
 dis 0 picpos begx -110103.272 begy -44287.496 endx -110102.272 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5032 0 cap 1
	color 0 6
 dis 0 picpos begx -100803.28 begy -43637.496 endx -100802.28 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2360 0 cap 1
	color 0 3
 dis 0 picpos begx -122093.272 begy -45337.496 endx -122092.272 endy -45337.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block606 0 cap 1
	color 0 4
 dis 0 picpos begx -5452.1095 begy 2730.50775 endx -5451.1095 endy 2730.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8070 0 cap 1
	color 0 11
 dis 0 picpos begx -71545.088 begy 5080.5 endx -71544.088 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6846 0 cap 1
	color 0 12
 dis 0 picpos begx -21446.156 begy 1680.5 endx -21445.156 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4943 0 cap 1
	color 0 5
 dis 0 picpos begx -28454.86 begy 1030.5 endx -28453.86 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8502 0 cap 1
	color 0 3
 dis 0 picpos begx -130910.272 begy 4030.5 endx -130909.272 endy 4030.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5849 0 cap 1
	color 0 5
 dis 0 picpos begx -118016.016 begy 1030.5 endx -118015.016 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6998 0 cap 1
	color 0 11
 dis 0 picpos begx -40339.876 begy -44287.496 endx -40338.876 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2523 0 cap 1
	color 0 3
 dis 0 picpos begx -28170.406 begy -45337.496 endx -28169.406 endy -45337.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2525 0 cap 1
	color 0 4
 dis 0 picpos begx -28770.406 begy -45837.496 endx -28769.406 endy -45837.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2489 0 cap 1
	color 0 12
 dis 0 picpos begx -97243.28 begy -46237.496 endx -97242.28 endy -46237.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4768 0 cap 1
	color 0 11
 dis 0 picpos begx -86807.584 begy 5080.5 endx -86806.584 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9080 0 cap 1
	color 0 14
 dis 0 picpos begx -29754.556 begy -6016.547 endx -29753.556 endy -6016.547 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7337 0 cap 1
	color 0 5
 dis 0 picpos begx -41489.876 begy -4469.5 endx -41488.876 endy -4469.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6907 0 cap 1
	color 0 5
 dis 0 picpos begx -87718.552 begy -21533.5 endx -87717.552 endy -21533.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7034 0 cap 1
	color 0 6
 dis 0 picpos begx -42489.876 begy -43637.496 endx -42488.876 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8389 0 cap 1
	color 0 5
 dis 0 picpos begx -94593.28 begy -46887.496 endx -94592.28 endy -46887.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6606 0 cap 1
	color 0 12
 dis 0 picpos begx -13716.086 begy 1680.5 endx -13715.086 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8067 0 cap 1
	color 0 6
 dis 0 picpos begx -73661.168 begy 7252.5 endx -73660.168 endy 7252.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6116 0 cap 1
	color 0 6
 dis 0 picpos begx -82077.368 begy 5730.5 endx -82076.368 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7740 0 cap 1
	color 0 4
 dis 0 picpos begx -75811.168 begy 5980.5 endx -75810.168 endy 5980.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6608 0 cap 1
	color 0 11
 dis 0 picpos begx -63715.064 begy 5080.5 endx -63714.064 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8359 0 cap 1
	color 0 13
 dis 0 picpos begx -28054.556 begy -3841.578 endx -28053.556 endy -3841.578 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5850 0 cap 1
	color 0 5
 dis 0 picpos begx -118016.016 begy -2469.5 endx -118015.016 endy -2469.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5828 0 cap 1
	color 0 5
 dis 0 picpos begx -111253.272 begy -2469.5 endx -111252.272 endy -2469.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6877 0 cap 1
	color 0 5
 dis 0 picpos begx -99803.28 begy -21533.5 endx -99802.28 endy -21533.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7333 0 cap 1
	color 0 6
 dis 0 picpos begx -54138.272 begy -40137.496 endx -54137.272 endy -40137.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5876 0 cap 1
	color 0 11
 dis 0 picpos begx -117866.016 begy -44287.496 endx -117865.016 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5004 0 cap 1
	color 0 6
 dis 0 picpos begx -112353.272 begy -43637.496 endx -112352.272 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8077 0 cap 1
	color 0 11
 dis 0 picpos begx -39637.82 begy 5080.5 endx -39636.82 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6727 0 cap 1
	color 0 12
 dis 0 picpos begx -5583.25 begy 1680.5 endx -5582.25 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block482 0 cap 1
	color 0 4
 dis 0 picpos begx 4077.0625 begy 2730.5 endx 4078.0625 endy 2730.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6154 0 cap 1
	color 0 6
 dis 0 picpos begx -65245.064 begy 5730.5 endx -65244.064 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4733 0 cap 1
	color 0 11
 dis 0 picpos begx -98787.136 begy 5080.5 endx -98786.136 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6101 0 cap 1
	color 0 5
 dis 0 picpos begx -20196.156 begy 1030.5 endx -20195.156 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6881 0 cap 1
	color 0 6
 dis 0 picpos begx -100803.28 begy -20933.5 endx -100802.28 endy -20933.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5215 0 cap 1
	color 0 11
 dis 0 picpos begx -28304.86 begy -44287.496 endx -28303.86 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6868 0 cap 1
	color 0 6
 dis 0 picpos begx -100803.28 begy -40137.496 endx -100802.28 endy -40137.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4769 0 cap 1
	color 0 6
 dis 0 picpos begx -87857.584 begy 5730.5 endx -87856.584 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6147 0 cap 1
	color 0 13
 dis 0 picpos begx -86557.584 begy 9830.5 endx -86556.584 endy 9830.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8074 0 cap 1
	color 0 11
 dis 0 picpos begx -56078.96 begy 5080.5 endx -56077.96 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6978 0 cap 1
	color 0 5
 dis 0 picpos begx -118016.016 begy -21603.5 endx -118015.016 endy -21603.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6784 0 cap 1
	color 0 11
 dis 0 picpos begx -25316.704 begy -44287.496 endx -25315.704 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6835 0 cap 1
	color 0 6
 dis 0 picpos begx -29354.25 begy -43637.496 endx -29353.25 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7454 0 cap 1
	color 0 13
 dis 0 picpos begx -40089.876 begy -37554.248 endx -40088.876 endy -37554.248 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2469 0 cap 1
	color 0 12
 dis 0 picpos begx -32993.272 begy -46887.496 endx -32992.272 endy -46887.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block460 0 cap 1
	color 0 6
 dis 0 picpos begx -97093.28 begy -53480.496 endx -97092.28 endy -53480.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6612 0 cap 1
	color 0 11
 dis 0 picpos begx -30832.804 begy 5080.5 endx -30831.804 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5990 0 cap 1
	color 0 5
 dis 0 picpos begx -12036.086 begy 1030.5 endx -12035.086 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6092 0 cap 1
	color 0 3
 dis 0 picpos begx -18146.156 begy 780.5 endx -18145.156 endy 780.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6473 0 cap 1
	color 0 6
 dis 0 picpos begx -73661.168 begy 13280.672 endx -73660.168 endy 13280.672 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4781 0 cap 1
	color 0 5
 dis 0 picpos begx -86957.584 begy 24646.5 endx -86956.584 endy 24646.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6131 0 cap 1
	color 0 6
 dis 0 picpos begx -82077.368 begy 13280.672 endx -82076.368 endy 13280.672 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7748 0 cap 1
	color 0 4
 dis 0 picpos begx -58978.96 begy 5980.5 endx -58977.96 endy 5980.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6460 0 cap 1
	color 0 6
 dis 0 picpos begx -56828.96 begy 13280.672 endx -56827.96 endy 13280.672 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7358 0 cap 1
	color 0 5
 dis 0 picpos begx -41489.876 begy -21548.688 endx -41488.876 endy -21548.688 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7468 0 cap 1
	color 0 5
 dis 0 picpos begx -52788.272 begy -28557.772 endx -52787.272 endy -28557.772 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4568 0 cap 1
	color 0 11
 dis 0 picpos begx -117272.848 begy 5080.5 endx -117271.848 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6974 0 cap 1
	color 0 6
 dis 0 picpos begx -118666.032 begy -21003.5 endx -118665.032 endy -21003.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2461 0 cap 1
	color 0 12
 dis 0 picpos begx -13793.273 begy -46237.496 endx -13792.273 endy -46237.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5878 0 cap 1
	color 0 6
 dis 0 picpos begx -119316.016 begy -43637.496 endx -119315.016 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4656 0 cap 1
	color 0 6
 dis 0 picpos begx -32363.772 begy 5730.5 endx -32362.772 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6610 0 cap 1
	color 0 11
 dis 0 picpos begx -46882.848 begy 5080.5 endx -46881.848 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6237 0 cap 1
	color 0 6
 dis 0 picpos begx -40387.82 begy 7242.5 endx -40386.82 endy 7242.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6238 0 cap 1
	color 0 6
 dis 0 picpos begx -48412.86 begy 5730.5 endx -48411.86 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5984 0 cap 1
	color 0 5
 dis 0 picpos begx -4053.24225 begy 1030.5 endx -4052.24225 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6006 0 cap 1
	color 0 3
 dis 0 picpos begx -9986.086 begy 780.5 endx -9985.086 endy 780.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4583 0 cap 1
	color 0 12
 dis 0 picpos begx 3288.71875 begy 1680.5 endx 3289.71875 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block480 0 cap 1
	color 0 3
 dis 0 picpos begx 4677.0625 begy 4030.5 endx 4678.0625 endy 4030.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4735 0 cap 1
	color 0 6
 dis 0 picpos begx -100037.136 begy 5730.5 endx -100036.136 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6052 0 cap 1
	color 0 5
 dis 0 picpos begx -20196.156 begy -7397.2655 endx -20195.156 endy -7397.2655 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8208 0 cap 1
	color 0 6
 dis 0 picpos begx -29354.556 begy -21003.516 endx -29353.556 endy -21003.516 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6767 0 cap 1
	color 0 12
 dis 0 picpos begx -34802.58 begy 680.5 endx -34801.58 endy 680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7357 0 cap 1
	color 0 6
 dis 0 picpos begx -42489.876 begy -20948.688 endx -42488.876 endy -20948.688 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7466 0 cap 1
	color 0 6
 dis 0 picpos begx -54138.272 begy -27757.772 endx -54137.272 endy -27757.772 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6579 0 cap 1
	color 0 6
 dis 0 picpos begx -119292.848 begy 5730.5 endx -119291.848 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5829 0 cap 1
	color 0 5
 dis 0 picpos begx -111253.272 begy -21603.5 endx -111252.272 endy -21603.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7356 0 cap 1
	color 0 6
 dis 0 picpos begx -42489.876 begy -40137.496 endx -42488.876 endy -40137.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5982 0 cap 1
	color 0 11
 dis 0 picpos begx -18046.156 begy -44287.496 endx -18045.156 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8408 0 cap 1
	color 0 5
 dis 0 picpos begx -94593.28 begy -60754.492 endx -94592.28 endy -60754.492 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6480 0 cap 1
	color 0 6
 dis 0 picpos begx -32363.772 begy 13730.672 endx -32362.772 endy 13730.672 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7961 0 cap 1
	color 0 11
 dis 0 picpos begx -23590.728 begy 5080.5 endx -23589.728 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6477 0 cap 1
	color 0 6
 dis 0 picpos begx -48412.86 begy 13280.672 endx -48411.86 endy 13280.672 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4775 0 cap 1
	color 0 5
 dis 0 picpos begx -86957.584 begy 43962.5 endx -86956.584 endy 43962.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6644 0 cap 1
	color 0 4
 dis 0 picpos begx -78227.624 begy 13530.672 endx -78226.624 endy 13530.672 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6676 0 cap 1
	color 0 4
 dis 0 picpos begx -53642.86 begy 13530.672 endx -53641.86 endy 13530.672 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4688 0 cap 1
	color 0 11
 dis 0 picpos begx -111924.576 begy 5080.5 endx -111923.576 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6972 0 cap 1
	color 0 6
 dis 0 picpos begx -118666.032 begy -40137.496 endx -118665.032 endy -40137.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5851 0 cap 1
	color 0 6
 dis 0 picpos begx -112353.272 begy -21003.5 endx -112352.272 endy -21003.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6672 0 cap 1
	color 0 13
 dis 0 picpos begx -28054.602 begy -33726.688 endx -28053.602 endy -33726.688 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5983 0 cap 1
	color 0 6
 dis 0 picpos begx -18796.156 begy -42525.66 endx -18795.156 endy -42525.66 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block316 0 cap 1
	color 0 6
 dis 0 picpos begx -32843.272 begy -64937.496 endx -32842.272 endy -64937.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2467 0 cap 1
	color 0 5
 dis 0 picpos begx -32343.272 begy -47537.496 endx -32342.272 endy -47537.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4942 0 cap 1
	color 0 6
 dis 0 picpos begx -112353.272 begy -40137.496 endx -112352.272 endy -40137.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6467 0 cap 1
	color 0 6
 dis 0 picpos begx -40387.82 begy 13530.672 endx -40386.82 endy 13530.672 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7965 0 cap 1
	color 0 6
 dis 0 picpos begx -24340.728 begy 8430.5 endx -24339.728 endy 8430.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6614 0 cap 1
	color 0 11
 dis 0 picpos begx -14786.273 begy 5080.5 endx -14785.273 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6115 0 cap 1
	color 0 5
 dis 0 picpos begx -12036.086 begy -7397.2655 endx -12035.086 endy -7397.2655 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6811 0 cap 1
	color 0 12
 dis 0 picpos begx 8406.719 begy 1680.5 endx 8407.719 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6774 0 cap 1
	color 0 14
 dis 0 picpos begx -88257.584 begy 15052.359 endx -88256.584 endy 15052.359 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4778 0 cap 1
	color 0 6
 dis 0 picpos begx -87857.584 begy 25246.5 endx -87856.584 endy 25246.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6452 0 cap 1
	color 0 14
 dis 0 picpos begx -82477.368 begy 25146.5 endx -82476.368 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8281 0 cap 1
	color 0 13
 dis 0 picpos begx -74661.376 begy 24546.5 endx -74660.376 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6468 0 cap 1
	color 0 6
 dis 0 picpos begx -65245.064 begy 19852.672 endx -65244.064 endy 19852.672 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8300 0 cap 1
	color 0 14
 dis 0 picpos begx -57228.96 begy 25146.5 endx -57227.96 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6508 0 cap 1
	color 0 12
 dis 0 picpos begx -51062.86 begy 13130.672 endx -51061.86 endy 13130.672 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8239 0 cap 1
	color 0 5
 dis 0 picpos begx -28454.556 begy -21603.5 endx -28453.556 endy -21603.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8591 0 cap 1
	color 0 5
 dis 0 picpos begx -132610.28 begy 16019.508 endx -132609.28 endy 16019.508 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8576 0 cap 1
	color 0 6
 dis 0 picpos begx -133110.28 begy -17576.734 endx -133109.28 endy -17576.734 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8567 0 cap 1
	color 0 5
 dis 0 picpos begx -132610.28 begy -18176.734 endx -132609.28 endy -18176.734 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8584 0 cap 1
	color 0 6
 dis 0 picpos begx -133110.28 begy 16619.508 endx -133109.28 endy 16619.508 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2521 0 cap 1
	color 0 3
 dis 0 picpos begx 9896.031 begy -45337.496 endx 9897.031 endy -45337.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2527 0 cap 1
	color 0 4
 dis 0 picpos begx 9296.031 begy -45837.496 endx 9297.031 endy -45837.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2457 0 cap 1
	color 0 5
 dis 0 picpos begx -8243.273 begy -46887.496 endx -8242.273 endy -46887.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2466 0 cap 1
	color 0 12
 dis 0 picpos begx -15093.273 begy -46887.496 endx -15092.273 endy -46887.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6691 0 cap 1
	color 0 4
 dis 0 picpos begx -29570.728 begy 13980.672 endx -29569.728 endy 13980.672 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7992 0 cap 1
	color 0 11
 dis 0 picpos begx -19995.648 begy 5080.5 endx -19994.648 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6616 0 cap 1
	color 0 11
 dis 0 picpos begx -6761.117 begy 5080.5 endx -6760.117 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6534 0 cap 1
	color 0 4
 dis 0 picpos begx -45597.82 begy 13530.672 endx -45596.82 endy 13530.672 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6024 0 cap 1
	color 0 5
 dis 0 picpos begx -4053.24225 begy -13902.758 endx -4052.24225 endy -13902.758 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6038 0 cap 1
	color 0 5
 dis 0 picpos begx 3938.71875 begy -531.5 endx 3939.71875 endy -531.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8280 0 cap 1
	color 0 14
 dis 0 picpos begx -74061.376 begy 25146.5 endx -74060.376 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6451 0 cap 1
	color 0 13
 dis 0 picpos begx -83077.368 begy 24546.5 endx -83076.368 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8289 0 cap 1
	color 0 13
 dis 0 picpos begx -57828.96 begy 24546.5 endx -57827.96 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4687 0 cap 1
	color 0 6
 dis 0 picpos begx -112574.576 begy 5730.5 endx -112573.576 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8604 0 cap 1
	color 0 5
 dis 0 picpos begx -132610.28 begy 36608.736 endx -132609.28 endy 36608.736 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6716 0 cap 1
	color 0 11
 dis 0 picpos begx -9986.086 begy -44287.496 endx -9985.086 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block425 0 cap 1
	color 0 6
 dis 0 picpos begx -13643.273 begy -52970.496 endx -13642.273 endy -52970.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4191 0 cap 1
	color 0 11
 dis 0 picpos begx -32193.272 begy -65587.5 endx -32192.272 endy -65587.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8403 0 cap 1
	color 0 6
 dis 0 picpos begx -97093.28 begy -65587.5 endx -97092.28 endy -65587.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8390 0 cap 1
	color 0 11
 dis 0 picpos begx -94443.28 begy -66237.5 endx -94442.28 endy -66237.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6509 0 cap 1
	color 0 12
 dis 0 picpos begx -26990.728 begy 13580.672 endx -26989.728 endy 13580.672 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7580 0 cap 1
	color 0 4
 dis 0 picpos begx -37175.976 begy 13780.672 endx -37174.976 endy 13780.672 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7980 0 cap 1
	color 0 4
 dis 0 picpos begx -20765.79 begy 8680.5 endx -20764.79 endy 8680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6288 0 cap 1
	color 0 6
 dis 0 picpos begx -8291.125 begy 5730.5 endx -8290.125 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7962 0 cap 1
	color 0 11
 dis 0 picpos begx 1013.90625 begy 5080.5 endx 1014.90625 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6589 0 cap 1
	color 0 12
 dis 0 picpos begx -43037.82 begy 13130.672 endx -43036.82 endy 13130.672 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block615 0 cap 1
	color 0 3
 dis 0 picpos begx 20715.952 begy 3380.50775 endx 20716.952 endy 3380.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6792 0 cap 1
	color 0 11
 dis 0 picpos begx -93007.856 begy 15302.359 endx -93006.856 endy 15302.359 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4773 0 cap 1
	color 0 12
 dis 0 picpos begx -88007.584 begy 44612.5 endx -88006.584 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8294 0 cap 1
	color 0 13
 dis 0 picpos begx -66245.06 begy 24526.5 endx -66244.06 endy 24526.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4713 0 cap 1
	color 0 14
 dis 0 picpos begx -100437.136 begy 15052.359 endx -100436.136 endy 15052.359 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7801 0 cap 1
	color 0 3
 dis 0 picpos begx -130112.272 begy -30138.5 endx -130111.272 endy -30138.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6724 0 cap 1
	color 0 11
 dis 0 picpos begx -2003.25 begy -44287.496 endx -2002.25 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5981 0 cap 1
	color 0 6
 dis 0 picpos begx -10636.086 begy -43537.496 endx -10635.086 endy -43537.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7299 0 cap 1
	color 0 4
 dis 0 picpos begx -15160.289 begy -42275.66 endx -15159.289 endy -42275.66 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6253 0 cap 1
	color 0 6
 dis 0 picpos begx -16315.648 begy 5730.5 endx -16314.648 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7753 0 cap 1
	color 0 4
 dis 0 picpos begx -10441.125 begy 5980.5 endx -10440.125 endy 5980.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7969 0 cap 1
	color 0 6
 dis 0 picpos begx -266.09375 begy 8340.5 endx -265.09375 endy 8340.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8262 0 cap 1
	color 0 14
 dis 0 picpos begx -19196.156 begy -21003.5 endx -19195.156 endy -21003.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5187 0 cap 1
	color 0 5
 dis 0 picpos begx 9906.031 begy 1030.5 endx 9907.031 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5239 0 cap 1
	color 0 12
 dis 0 picpos begx 19664.124 begy 1680.5 endx 19665.124 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block488 0 cap 1
	color 0 4
 dis 0 picpos begx 43102.984 begy 2730.5 endx 43103.984 endy 2730.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8288 0 cap 1
	color 0 14
 dis 0 picpos begx -65645.06 begy 25126.5 endx -65644.06 endy 25126.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8196 0 cap 1
	color 0 5
 dis 0 picpos begx -98937.136 begy 24546.5 endx -98936.136 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8266 0 cap 1
	color 0 13
 dis 0 picpos begx -19796.156 begy -21603.5 endx -19795.156 endy -21603.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8188 0 cap 1
	color 0 5
 dis 0 picpos begx -112074.576 begy 24646.5 endx -112073.576 endy 24646.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8185 0 cap 1
	color 0 6
 dis 0 picpos begx -112574.576 begy 25246.5 endx -112573.576 endy 25246.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8944 0 cap 1
	color 0 6
 dis 0 picpos begx -118642.848 begy 9230.5 endx -118641.848 endy 9230.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8555 0 cap 1
	color 0 6
 dis 0 picpos begx -133110.272 begy -35115.3 endx -133109.272 endy -35115.3 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8551 0 cap 1
	color 0 5
 dis 0 picpos begx -132610.272 begy -35715.3 endx -132609.272 endy -35715.3 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2476 0 cap 1
	color 0 3
 dis 0 picpos begx -130112.912 begy 38987.5 endx -130111.912 endy 38987.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8526 0 cap 1
	color 0 13
 dis 0 picpos begx -130910.272 begy 53533.264 endx -130909.272 endy 53533.264 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4413 0 cap 1
	color 0 4
 dis 0 picpos begx -120342.848 begy 38387.5 endx -120341.848 endy 38387.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8597 0 cap 1
	color 0 6
 dis 0 picpos begx -133110.28 begy 37208.736 endx -133109.28 endy 37208.736 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6025 0 cap 1
	color 0 6
 dis 0 picpos begx -2653.25 begy -43537.496 endx -2652.25 endy -43537.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block427 0 cap 1
	color 0 6
 dis 0 picpos begx -13643.273 begy -56387.496 endx -13642.273 endy -56387.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8318 0 cap 1
	color 0 14
 dis 0 picpos begx -32763.772 begy 25146.5 endx -32762.772 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8307 0 cap 1
	color 0 13
 dis 0 picpos begx -33363.772 begy 24546.5 endx -33362.772 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8311 0 cap 1
	color 0 14
 dis 0 picpos begx -40787.82 begy 25146.5 endx -40786.82 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8310 0 cap 1
	color 0 13
 dis 0 picpos begx -41387.82 begy 24546.5 endx -41386.82 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7758 0 cap 1
	color 0 4
 dis 0 picpos begx -2416.09375 begy 5980.5 endx -2415.09375 endy 5980.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6476 0 cap 1
	color 0 6
 dis 0 picpos begx -8291.125 begy 12930.672 endx -8290.125 endy 12930.672 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8306 0 cap 1
	color 0 14
 dis 0 picpos begx -48812.86 begy 25146.5 endx -48811.86 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8302 0 cap 1
	color 0 13
 dis 0 picpos begx -49412.86 begy 24546.5 endx -49411.86 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8272 0 cap 1
	color 0 13
 dis 0 picpos begx -11636.086 begy -21603.5 endx -11635.086 endy -21603.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8268 0 cap 1
	color 0 13
 dis 0 picpos begx -3653.25 begy -21603.5 endx -3652.25 endy -21603.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8273 0 cap 1
	color 0 13
 dis 0 picpos begx 4338.719 begy -21603.5 endx 4339.719 endy -21603.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6133 0 cap 1
	color 0 5
 dis 0 picpos begx -75061.168 begy 43862.5 endx -75060.168 endy 43862.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6323 0 cap 1
	color 0 5
 dis 0 picpos begx -49812.86 begy 43962.5 endx -49811.86 endy 43962.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6538 0 cap 1
	color 0 11
 dis 0 picpos begx -105793.832 begy 15302.359 endx -105792.832 endy 15302.359 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6577 0 cap 1
	color 0 14
 dis 0 picpos begx -119716.016 begy -29987.5 endx -119715.016 endy -29987.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4414 0 cap 1
	color 0 4
 dis 0 picpos begx -120366.016 begy -30737.5 endx -120365.016 endy -30737.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8614 0 cap 1
	color 0 5
 dis 0 picpos begx -132610.28 begy 62313.484 endx -132609.28 endy 62313.484 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5035 0 cap 1
	color 0 11
 dis 0 picpos begx 10056.031 begy -44287.496 endx 10057.031 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2464 0 cap 1
	color 0 12
 dis 0 picpos begx 51006.72 begy -46237.496 endx 51007.72 endy -46237.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1 0 cap 1
	color 0 3
 dis 0 picpos begx -100466.376 begy -66637.5 endx -100465.376 endy -66637.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8323 0 cap 1
	color 0 14
 dis 0 picpos begx -24740.728 begy 25146.5 endx -24739.728 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8315 0 cap 1
	color 0 13
 dis 0 picpos begx -25340.728 begy 24546.5 endx -25339.728 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7977 0 cap 1
	color 0 11
 dis 0 picpos begx 5298.0625 begy 5080.5 endx 5299.0625 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7982 0 cap 1
	color 0 4
 dis 0 picpos begx 3655.28125 begy 8590.5 endx 3656.28125 endy 8590.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8190 0 cap 1
	color 0 14
 dis 0 picpos begx -11036.086 begy -21003.5 endx -11035.086 endy -21003.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8275 0 cap 1
	color 0 14
 dis 0 picpos begx -3053.25 begy -21003.5 endx -3052.25 endy -21003.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6813 0 cap 1
	color 0 14
 dis 0 picpos begx 8156.719 begy -4415.789 endx 8157.719 endy -4415.789 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8279 0 cap 1
	color 0 14
 dis 0 picpos begx 4938.719 begy -21003.5 endx 4939.719 endy -21003.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6720 0 cap 1
	color 0 12
 dis 0 picpos begx 30410.188 begy 1680.5 endx 30411.188 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4739 0 cap 1
	color 0 12
 dis 0 picpos begx -100187.136 begy 44612.5 endx -100186.136 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4692 0 cap 1
	color 0 5
 dis 0 picpos begx -112074.576 begy 43962.5 endx -112073.576 endy 43962.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4693 0 cap 1
	color 0 12
 dis 0 picpos begx -112724.576 begy 44612.5 endx -112723.576 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8951 0 cap 1
	color 0 5
 dis 0 picpos begx -117422.848 begy 24646.5 endx -117421.848 endy 24646.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6547 0 cap 1
	color 0 14
 dis 0 picpos begx -119692.848 begy 39137.5 endx -119691.848 endy 39137.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6807 0 cap 1
	color 0 6
 dis 0 picpos begx 8556.719 begy -43637.496 endx 8557.719 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5988 0 cap 1
	color 0 4
 dis 0 picpos begx -7116.664 begy -43287.496 endx -7115.664 endy -43287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2552 0 cap 1
	color 0 4
 dis 0 picpos begx 54113.44 begy -45837.496 endx 54114.44 endy -45837.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2459 0 cap 1
	color 0 12
 dis 0 picpos begx 49706.72 begy -46887.496 endx 49707.72 endy -46887.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3499 0 cap 1
	color 0 11
 dis 0 picpos begx -6793.2735 begy -65587.5 endx -6792.2735 endy -65587.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block430 0 cap 1
	color 0 5
 dis 0 picpos begx -8243.273 begy -57187.496 endx -8242.273 endy -57187.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6397 0 cap 1
	color 0 5
 dis 0 picpos begx -25740.728 begy 43862.5 endx -25739.728 endy 43862.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8317 0 cap 1
	color 0 13
 dis 0 picpos begx -17315.648 begy 24546.5 endx -17314.648 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6618 0 cap 1
	color 0 11
 dis 0 picpos begx 10108.062 begy 5080.5 endx 10109.062 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4812 0 cap 1
	color 0 11
 dis 0 picpos begx 26012.672 begy 5080.5 endx 26013.672 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6363 0 cap 1
	color 0 5
 dis 0 picpos begx -41787.82 begy 43862.5 endx -41786.82 endy 43862.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6809 0 cap 1
	color 0 6
 dis 0 picpos begx 8556.719 begy -20503.5 endx 8557.719 endy -20503.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5336 0 cap 1
	color 0 5
 dis 0 picpos begx 20714.124 begy 1030.5 endx 20715.124 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block486 0 cap 1
	color 0 3
 dis 0 picpos begx 43702.984 begy 4030.5 endx 43703.984 endy 4030.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5370 0 cap 1
	color 0 12
 dis 0 picpos begx 40715.656 begy 1680.5 endx 40716.656 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7569 0 cap 1
	color 0 13
 dis 0 picpos begx -98537.136 begy 33095.72 endx -98536.136 endy 33095.72 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4741 0 cap 1
	color 0 5
 dis 0 picpos begx -98937.136 begy 43962.5 endx -98936.136 endy 43962.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8194 0 cap 1
	color 0 6
 dis 0 picpos begx -100037.136 begy 25146.5 endx -100036.136 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8544 0 cap 1
	color 0 6
 dis 0 picpos begx -133110.272 begy -52089.1 endx -133109.272 endy -52089.1 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8541 0 cap 1
	color 0 5
 dis 0 picpos begx -132610.272 begy -52689.1 endx -132609.272 endy -52689.1 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8613 0 cap 1
	color 0 6
 dis 0 picpos begx -133110.28 begy 62913.484 endx -133109.28 endy 62913.484 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5335 0 cap 1
	color 0 11
 dis 0 picpos begx 20864.124 begy -44287.496 endx 20865.124 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6011 0 cap 1
	color 0 4
 dis 0 picpos begx 859.953125 begy -43287.496 endx 860.953125 endy -43287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4237 0 cap 1
	color 0 3
 dis 0 picpos begx -74271.752 begy -66637.5 endx -74270.752 endy -66637.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4235 0 cap 1
	color 0 4
 dis 0 picpos begx -74871.752 begy -67137.504 endx -74870.752 endy -67137.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6226 0 cap 1
	color 0 5
 dis 0 picpos begx -33763.772 begy 43862.5 endx -33762.772 endy 43862.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6267 0 cap 1
	color 0 5
 dis 0 picpos begx -17715.648 begy 43862.5 endx -17714.648 endy 43862.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8331 0 cap 1
	color 0 14
 dis 0 picpos begx -8691.125 begy 25146.5 endx -8690.125 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8329 0 cap 1
	color 0 13
 dis 0 picpos begx -9291.125 begy 24546.5 endx -9290.125 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6669 0 cap 1
	color 0 6
 dis 0 picpos begx 16603.094 begy 13180.672 endx 16604.094 endy 13180.672 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7561 0 cap 1
	color 0 5
 dis 0 picpos begx 17103.094 begy 9951.289 endx 17104.094 endy 9951.289 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4813 0 cap 1
	color 0 6
 dis 0 picpos begx 24962.672 begy 5733.5545 endx 24963.672 endy 5733.5545 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6152 0 cap 1
	color 0 5
 dis 0 picpos begx -66645.06 begy 43862.5 endx -66644.06 endy 43862.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4663 0 cap 1
	color 0 5
 dis 0 picpos begx -58228.96 begy 41900.5 endx -58227.96 endy 41900.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8948 0 cap 1
	color 0 6
 dis 0 picpos begx -118642.848 begy 25246.5 endx -118641.848 endy 25246.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8500 0 cap 1
	color 0 5
 dis 0 picpos begx -132610.28 begy 82402.496 endx -132609.28 endy 82402.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1065 0 cap 1
	color 0 12
 dis 0 picpos begx -117428.312 begy 97262.496 endx -117427.312 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5186 0 cap 1
	color 0 6
 dis 0 picpos begx 19814.124 begy -43637.496 endx 19815.124 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2546 0 cap 1
	color 0 3
 dis 0 picpos begx 54713.44 begy -45337.496 endx 54714.44 endy -45337.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block431 0 cap 1
	color 0 5
 dis 0 picpos begx -8243.273 begy -60754.492 endx -8242.273 endy -60754.492 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4233 0 cap 1
	color 0 3
 dis 0 picpos begx -53186.844 begy -66637.5 endx -53185.844 endy -66637.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7964 0 cap 1
	color 0 6
 dis 0 picpos begx 8578.062 begy 5730.5 endx 8579.062 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8197 0 cap 1
	color 0 14
 dis 0 picpos begx -666.09375 begy 25146.5 endx -665.09375 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8333 0 cap 1
	color 0 13
 dis 0 picpos begx -1266.09375 begy 24546.5 endx -1265.09375 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5191 0 cap 1
	color 0 5
 dis 0 picpos begx 9906.031 begy -21103.5 endx 9907.031 endy -21103.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5364 0 cap 1
	color 0 5
 dis 0 picpos begx 31460.188 begy 1030.5 endx 31461.188 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2498 0 cap 1
	color 0 4
 dis 0 picpos begx -67320.8 begy 45662.5 endx -67319.8 endy 45662.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4664 0 cap 1
	color 0 12
 dis 0 picpos begx -58878.96 begy 44612.5 endx -58877.96 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4683 0 cap 1
	color 0 13
 dis 0 picpos begx -111674.576 begy 33095.72 endx -111673.576 endy 33095.72 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4433 0 cap 1
	color 0 12
 dis 0 picpos begx -119442.848 begy 44612.5 endx -119441.848 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block433 0 cap 1
	color 0 6
 dis 0 picpos begx 51156.72 begy -52970.5 endx 51157.72 endy -52970.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2486 0 cap 1
	color 0 5
 dis 0 picpos begx 56556.72 begy -46887.496 endx 56557.72 endy -46887.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block306 0 cap 1
	color 0 6
 dis 0 picpos begx -13643.273 begy -65587.5 endx -13642.273 endy -65587.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3801 0 cap 1
	color 0 12
 dis 0 picpos begx -96778.08 begy -68187.504 endx -96777.08 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8326 0 cap 1
	color 0 14
 dis 0 picpos begx -16715.648 begy 25146.5 endx -16714.648 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6520 0 cap 1
	color 0 6
 dis 0 picpos begx -16315.648 begy 21196.688 endx -16314.648 endy 21196.688 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7763 0 cap 1
	color 0 4
 dis 0 picpos begx 14453.094 begy 5980.5 endx 14454.094 endy 5980.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7530 0 cap 1
	color 0 13
 dis 0 picpos begx 26262.672 begy 9850.5 endx 26263.672 endy 9850.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7457 0 cap 1
	color 0 11
 dis 0 picpos begx 15090.484 begy -33632.844 endx 15091.484 endy -33632.844 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5405 0 cap 1
	color 0 12
 dis 0 picpos begx 51471.608 begy 1680.5 endx 51472.608 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5057 0 cap 1
	color 0 5
 dis 0 picpos begx 41765.656 begy 1030.5 endx 41766.656 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6601 0 cap 1
	color 0 5
 dis 0 picpos begx -64745.064 begy 43962.5 endx -64744.064 endy 43962.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6995 0 cap 1
	color 0 5
 dis 0 picpos begx -117422.848 begy 43962.5 endx -117421.848 endy 43962.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8499 0 cap 1
	color 0 6
 dis 0 picpos begx -133110.28 begy 83002.496 endx -133109.28 endy 83002.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5194 0 cap 1
	color 0 11
 dis 0 picpos begx 31610.188 begy -44287.496 endx 31611.188 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5319 0 cap 1
	color 0 14
 dis 0 picpos begx 19414.124 begy -33882.844 endx 19415.124 endy -33882.844 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3501 0 cap 1
	color 0 11
 dis 0 picpos begx -8093.2735 begy -66237.5 endx -8092.2735 endy -66237.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4231 0 cap 1
	color 0 4
 dis 0 picpos begx -53786.844 begy -67137.504 endx -53785.844 endy -67137.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8340 0 cap 1
	color 0 13
 dis 0 picpos begx 7578.0625 begy 24546.5 endx 7579.0625 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6449 0 cap 1
	color 0 5
 dis 0 picpos begx 7178.0625 begy 43962.5 endx 7179.0625 endy 43962.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6604 0 cap 1
	color 0 12
 dis 0 picpos begx 5648.0625 begy 44612.5 endx 5649.0625 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4569 0 cap 1
	color 0 11
 dis 0 picpos begx 37062.608 begy 5080.5 endx 37063.608 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2628 0 cap 1
	color 0 3
 dis 0 picpos begx -66720.8 begy 46162.5 endx -66719.8 endy 46162.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8783 0 cap 1
	color 0 5
 dis 0 picpos begx -132610.28 begy -73283.376 endx -132609.28 endy -73283.376 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8787 0 cap 1
	color 0 6
 dis 0 picpos begx -133110.28 begy -72683.376 endx -133109.28 endy -72683.376 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1111 0 cap 1
	color 0 12
 dis 0 picpos begx -100297.368 begy 97262.496 endx -100296.368 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1067 0 cap 1
	color 0 5
 dis 0 picpos begx -115178.312 begy 96612.496 endx -115177.312 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5302 0 cap 1
	color 0 11
 dis 0 picpos begx 41915.656 begy -44287.496 endx 41916.656 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5055 0 cap 1
	color 0 6
 dis 0 picpos begx 30560.188 begy -43637.496 endx 30561.188 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2550 0 cap 1
	color 0 4
 dis 0 picpos begx 96836.376 begy -45837.496 endx 96837.376 endy -45837.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block435 0 cap 1
	color 0 6
 dis 0 picpos begx 51156.72 begy -56387.48 endx 51157.72 endy -56387.48 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6651 0 cap 1
	color 0 4
 dis 0 picpos begx -12756 begy 21446.688 endx -12755 endy 21446.688 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6487 0 cap 1
	color 0 6
 dis 0 picpos begx 8578.062 begy 13080.672 endx 8579.062 endy 13080.672 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7565 0 cap 1
	color 0 13
 dis 0 picpos begx 21114.124 begy -9128.039 endx 21115.124 endy -9128.039 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block494 0 cap 1
	color 0 4
 dis 0 picpos begx 86409.952 begy 2730.5 endx 86410.952 endy 2730.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2278 0 cap 1
	color 0 3
 dis 0 picpos begx -122093.272 begy 46162.5 endx -122092.272 endy 46162.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8954 0 cap 1
	color 0 5
 dis 0 picpos begx -117422.848 begy 40395.904 endx -117421.848 endy 40395.904 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5338 0 cap 1
	color 0 11
 dis 0 picpos begx 52671.608 begy -44287.496 endx 52672.608 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5298 0 cap 1
	color 0 6
 dis 0 picpos begx 40865.656 begy -43637.496 endx 40866.656 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7549 0 cap 1
	color 0 13
 dis 0 picpos begx 21114.124 begy -33782.844 endx 21115.124 endy -33782.844 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3745 0 cap 1
	color 0 12
 dis 0 picpos begx -86336.864 begy -68187.504 endx -86335.864 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3802 0 cap 1
	color 0 5
 dis 0 picpos begx -94528.08 begy -68839.12 endx -94527.08 endy -68839.12 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6417 0 cap 1
	color 0 5
 dis 0 picpos begx -1666.09375 begy 43862.5 endx -1665.09375 endy 43862.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8348 0 cap 1
	color 0 14
 dis 0 picpos begx 16203.094 begy 25146.5 endx 16204.094 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8336 0 cap 1
	color 0 13
 dis 0 picpos begx 15603.094 begy 24546.5 endx 15604.094 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6741 0 cap 1
	color 0 6
 dis 0 picpos begx 35532.608 begy 7242.5 endx 35533.608 endy 7242.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5893 0 cap 1
	color 0 6
 dis 0 picpos begx 43497.656 begy 5830.5 endx 43498.656 endy 5830.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8212 0 cap 1
	color 0 6
 dis 0 picpos begx 19814.124 begy -21003.5 endx 19815.124 endy -21003.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5038 0 cap 1
	color 0 5
 dis 0 picpos begx 52521.608 begy 1030.5 endx 52522.608 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5403 0 cap 1
	color 0 12
 dis 0 picpos begx 62341.796 begy 1680.5 endx 62342.796 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2443 0 cap 1
	color 0 11
 dis 0 picpos begx -83693.28 begy 46562.5 endx -83692.28 endy 46562.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2500 0 cap 1
	color 0 4
 dis 0 picpos begx -34610.032 begy 45662.5 endx -34609.032 endy 45662.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7845 0 cap 1
	color 0 3
 dis 0 picpos begx -116340.896 begy 98912.496 endx -116339.896 endy 98912.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7842 0 cap 1
	color 0 3
 dis 0 picpos begx -126593.272 begy 98912.496 endx -126592.272 endy 98912.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5381 0 cap 1
	color 0 6
 dis 0 picpos begx 51621.608 begy -43637.496 endx 51622.608 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2548 0 cap 1
	color 0 3
 dis 0 picpos begx 97436.376 begy -45337.496 endx 97437.376 endy -45337.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3525 0 cap 1
	color 0 3
 dis 0 picpos begx 11636.766 begy -66637.5 endx 11637.766 endy -66637.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3518 0 cap 1
	color 0 4
 dis 0 picpos begx 11036.766 begy -67137.504 endx 11037.766 endy -67137.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8339 0 cap 1
	color 0 14
 dis 0 picpos begx 8178.0625 begy 25146.5 endx 8179.0625 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8203 0 cap 1
	color 0 5
 dis 0 picpos begx 25862.672 begy 24549.556 endx 25863.672 endy 24549.556 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8201 0 cap 1
	color 0 6
 dis 0 picpos begx 24962.672 begy 25149.556 endx 24963.672 endy 25149.556 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8451 0 cap 1
	color 0 13
 dis 0 picpos begx 31860.188 begy -9128.039 endx 31861.188 endy -9128.039 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4579 0 cap 1
	color 0 11
 dis 0 picpos begx 52772.188 begy 5080.5 endx 52773.188 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6722 0 cap 1
	color 0 12
 dis 0 picpos begx 73423.448 begy 1680.5 endx 73424.448 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1143 0 cap 1
	color 0 12
 dis 0 picpos begx -84744.464 begy 97262.496 endx -84743.464 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1113 0 cap 1
	color 0 5
 dis 0 picpos begx -97547.368 begy 96612.496 endx -97546.368 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1691 0 cap 1
	color 0 5
 dis 0 picpos begx -116178.312 begy 93722.496 endx -116177.312 endy 93722.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block662 0 cap 1
	color 0 4
 dis 0 picpos begx -83981.808 begy 98312.496 endx -83980.808 endy 98312.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8215 0 cap 1
	color 0 5
 dis 0 picpos begx 20714.124 begy -21603.5 endx 20715.124 endy -21603.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3564 0 cap 1
	color 0 3
 dis 0 picpos begx 33258.812 begy -66637.5 endx 33259.812 endy -66637.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3837 0 cap 1
	color 0 12
 dis 0 picpos begx -64741.648 begy -68187.504 endx -64740.648 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2632 0 cap 1
	color 0 3
 dis 0 picpos begx -34010.032 begy 46162.5 endx -34009.032 endy 46162.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6432 0 cap 1
	color 0 5
 dis 0 picpos begx -9691.125 begy 42778.5 endx -9690.125 endy 42778.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7315 0 cap 1
	color 0 4
 dis 0 picpos begx 12228.688 begy 13330.672 endx 12229.688 endy 13330.672 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6745 0 cap 1
	color 0 4
 dis 0 picpos begx 39236.28 begy 7492.5 endx 39237.28 endy 7492.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4850 0 cap 1
	color 0 11
 dis 0 picpos begx 60841.36 begy 5080.5 endx 60842.36 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5908 0 cap 1
	color 0 6
 dis 0 picpos begx 51522.188 begy 5730.5 endx 51523.188 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5427 0 cap 1
	color 0 12
 dis 0 picpos begx 81910.248 begy 1680.5 endx 81911.248 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block492 0 cap 1
	color 0 3
 dis 0 picpos begx 87009.952 begy 4030.5 endx 87010.952 endy 4030.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1071 0 cap 1
	color 0 6
 dis 0 picpos begx -117278.312 begy 87237.504 endx -117277.312 endy 87237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7576 0 cap 1
	color 0 14
 dis 0 picpos begx 51221.608 begy -37424.568 endx 51222.608 endy -37424.568 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7553 0 cap 1
	color 0 14
 dis 0 picpos begx 40465.656 begy -37424.568 endx 40466.656 endy -37424.568 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block797 0 cap 1
	color 0 4
 dis 0 picpos begx 131902.72 begy -45837.496 endx 131903.72 endy -45837.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3495 0 cap 1
	color 0 11
 dis 0 picpos begx 58006.72 begy -65587.5 endx 58007.72 endy -65587.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block438 0 cap 1
	color 0 5
 dis 0 picpos begx 56556.72 begy -57187.48 endx 56557.72 endy -57187.48 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3496 0 cap 1
	color 0 11
 dis 0 picpos begx 56706.72 begy -66237.5 endx 56707.72 endy -66237.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3562 0 cap 1
	color 0 4
 dis 0 picpos begx 32658.812 begy -67137.504 endx 32659.812 endy -67137.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3747 0 cap 1
	color 0 12
 dis 0 picpos begx -43462.272 begy -68187.504 endx -43461.272 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7667 0 cap 1
	color 0 12
 dis 0 picpos begx -75673.16 begy -68187.504 endx -75672.16 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7627 0 cap 1
	color 0 5
 dis 0 picpos begx -84086.864 begy -68837.504 endx -84085.864 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3866 0 cap 1
	color 0 12
 dis 0 picpos begx -54192.5 begy -68187.504 endx -54191.5 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4587 0 cap 1
	color 0 12
 dis 0 picpos begx 18600.562 begy 44612.5 endx 18601.562 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6542 0 cap 1
	color 0 4
 dis 0 picpos begx 47315.484 begy 6080.5 endx 47316.484 endy 6080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4840 0 cap 1
	color 0 6
 dis 0 picpos begx 59791.36 begy 5730.5 endx 59792.36 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5428 0 cap 1
	color 0 5
 dis 0 picpos begx 63391.796 begy 1030.5 endx 63392.796 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7542 0 cap 1
	color 0 14
 dis 0 picpos begx 62091.796 begy -2169.5 endx 62092.796 endy -2169.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2283 0 cap 1
	color 0 6
 dis 0 picpos begx -89243.28 begy 47212.5 endx -89242.28 endy 47212.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2452 0 cap 1
	color 0 11
 dis 0 picpos begx -82393.28 begy 47212.5 endx -82392.28 endy 47212.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1730 0 cap 1
	color 0 5
 dis 0 picpos begx -97547.368 begy 93952.496 endx -97546.368 endy 93952.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5374 0 cap 1
	color 0 11
 dis 0 picpos begx 63541.796 begy -44287.496 endx 63542.796 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block795 0 cap 1
	color 0 12
 dis 0 picpos begx 131406.72 begy -46887.496 endx 131407.72 endy -46887.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block328 0 cap 1
	color 0 6
 dis 0 picpos begx 51156.72 begy -65587.5 endx 51157.72 endy -65587.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3009 0 cap 1
	color 0 12
 dis 0 picpos begx -32669.272 begy -68187.504 endx -32668.272 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3905 0 cap 1
	color 0 5
 dis 0 picpos begx -95528.08 begy -71728.304 endx -95527.08 endy -71728.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7669 0 cap 1
	color 0 5
 dis 0 picpos begx -73423.16 begy -68837.504 endx -73422.16 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2494 0 cap 1
	color 0 4
 dis 0 picpos begx 6622.7655 begy 45662.5 endx 6623.7655 endy 45662.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7786 0 cap 1
	color 0 12
 dis 0 picpos begx 31232.516 begy 44612.5 endx 31233.516 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5081 0 cap 1
	color 0 5
 dis 0 picpos begx 74273.448 begy 1030.5 endx 74274.448 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block360 0 cap 1
	color 0 5
 dis 0 picpos begx -83843.28 begy 53245.484 endx -83842.28 endy 53245.484 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8749 0 cap 1
	color 0 13
 dis 0 picpos begx -130910.28 begy -85637.504 endx -130909.28 endy -85637.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8743 0 cap 1
	color 0 6
 dis 0 picpos begx -133110.28 begy -98912.496 endx -133109.28 endy -98912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1147 0 cap 1
	color 0 5
 dis 0 picpos begx -82344.472 begy 96612.496 endx -82343.472 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block664 0 cap 1
	color 0 3
 dis 0 picpos begx -83381.808 begy 99562.496 endx -83380.808 endy 99562.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5376 0 cap 1
	color 0 11
 dis 0 picpos begx 74423.448 begy -44287.496 endx 74424.448 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5300 0 cap 1
	color 0 6
 dis 0 picpos begx 62491.796 begy -43637.496 endx 62492.796 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7305 0 cap 1
	color 0 11
 dis 0 picpos begx 46911.5 begy -37174.568 endx 46912.5 endy -37174.568 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block439 0 cap 1
	color 0 5
 dis 0 picpos begx 56556.72 begy -60754.492 endx 56557.72 endy -60754.492 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3045 0 cap 1
	color 0 12
 dis 0 picpos begx -21800.272 begy -68187.504 endx -21799.272 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3867 0 cap 1
	color 0 5
 dis 0 picpos begx -51942.5 begy -68839.12 endx -51941.5 endy -68839.12 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7693 0 cap 1
	color 0 5
 dis 0 picpos begx -84086.864 begy -71331.112 endx -84085.864 endy -71331.112 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3838 0 cap 1
	color 0 5
 dis 0 picpos begx -62491.648 begy -68839.12 endx -62490.648 endy -68839.12 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6433 0 cap 1
	color 0 5
 dis 0 picpos begx 15203.094 begy 43862.5 endx 15204.094 endy 43862.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8242 0 cap 1
	color 0 14
 dis 0 picpos begx 43097.656 begy 25146.5 endx 43098.656 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8209 0 cap 1
	color 0 6
 dis 0 picpos begx 30560.188 begy -21003.5 endx 30561.188 endy -21003.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5596 0 cap 1
	color 0 11
 dis 0 picpos begx 74179.408 begy 5080.5 endx 74180.408 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4572 0 cap 1
	color 0 12
 dis 0 picpos begx 97119.608 begy 1680.5 endx 97120.608 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5725 0 cap 1
	color 0 5
 dis 0 picpos begx 84660.248 begy 1030.5 endx 84661.248 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8220 0 cap 1
	color 0 6
 dis 0 picpos begx 40865.656 begy -20933.5 endx 40866.656 endy -20933.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block256 0 cap 1
	color 0 12
 dis 0 picpos begx -90693.28 begy 65912.5 endx -90692.28 endy 65912.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8989 0 cap 1
	color 0 11
 dis 0 picpos begx -103699.208 begy -84587.504 endx -103698.208 endy -84587.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1073 0 cap 1
	color 0 5
 dis 0 picpos begx -116178.312 begy 86637.504 endx -116177.312 endy 86637.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4594 0 cap 1
	color 0 11
 dis 0 picpos begx 84810.248 begy -44287.496 endx 84811.248 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5379 0 cap 1
	color 0 6
 dis 0 picpos begx 73573.448 begy -43637.496 endx 73574.448 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4519 0 cap 1
	color 0 3
 dis 0 picpos begx 75095.448 begy -66637.5 endx 75096.448 endy -66637.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4505 0 cap 1
	color 0 4
 dis 0 picpos begx 74495.448 begy -67137.504 endx 74496.448 endy -67137.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3083 0 cap 1
	color 0 12
 dis 0 picpos begx -10501.258 begy -68187.504 endx -10500.258 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3748 0 cap 1
	color 0 5
 dis 0 picpos begx -41212.272 begy -68837.504 endx -41211.272 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2453 0 cap 1
	color 0 11
 dis 0 picpos begx -8093.2735 begy 46562.5 endx -8092.2735 endy 46562.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2630 0 cap 1
	color 0 3
 dis 0 picpos begx 7222.7655 begy 46162.5 endx 7223.7655 endy 46162.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8245 0 cap 1
	color 0 14
 dis 0 picpos begx 35132.608 begy 25146.5 endx 35133.608 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8246 0 cap 1
	color 0 13
 dis 0 picpos begx 34532.608 begy 24546.5 endx 34533.608 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8249 0 cap 1
	color 0 13
 dis 0 picpos begx 42497.656 begy 24546.5 endx 42498.656 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9396 0 cap 1
	color 0 13
 dis 0 picpos begx 61091.36 begy 11968.148 endx 61092.36 endy 11968.148 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5561 0 cap 1
	color 0 6
 dis 0 picpos begx 71329.408 begy 5730.5 endx 71330.408 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5958 0 cap 1
	color 0 6
 dis 0 picpos begx 51522.188 begy 13854.359 endx 51523.188 endy 13854.359 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7544 0 cap 1
	color 0 11
 dis 0 picpos begx 57355.204 begy -37174.568 endx 57356.204 endy -37174.568 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8225 0 cap 1
	color 0 5
 dis 0 picpos begx 41765.656 begy -21533.5 endx 41766.656 endy -21533.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block343 0 cap 1
	color 0 5
 dis 0 picpos begx -83843.28 begy 56712.5 endx -83842.28 endy 56712.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1190 0 cap 1
	color 0 12
 dis 0 picpos begx -69273.28 begy 97262.496 endx -69272.28 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4351 0 cap 1
	color 0 14
 dis 0 picpos begx -81444.472 begy 93412.496 endx -81443.472 endy 93412.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7168 0 cap 1
	color 0 11
 dis 0 picpos begx 99999.608 begy -44287.496 endx 100000.608 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7166 0 cap 1
	color 0 6
 dis 0 picpos begx 82060.248 begy -43637.496 endx 82061.248 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7578 0 cap 1
	color 0 14
 dis 0 picpos begx 62091.796 begy -37424.568 endx 62092.796 endy -37424.568 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4193 0 cap 1
	color 0 11
 dis 0 picpos begx 132306.72 begy -65587.5 endx 132307.72 endy -65587.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3140 0 cap 1
	color 0 12
 dis 0 picpos begx 10618.328 begy -68187.504 endx 10619.328 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3106 0 cap 1
	color 0 12
 dis 0 picpos begx 251.875 begy -68187.504 endx 252.875 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3011 0 cap 1
	color 0 5
 dis 0 picpos begx -30419.272 begy -68837.504 endx -30418.272 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3807 0 cap 1
	color 0 5
 dis 0 picpos begx -95528.08 begy -82912.496 endx -95527.08 endy -82912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4101 0 cap 1
	color 0 5
 dis 0 picpos begx -62491.648 begy -71418.304 endx -62490.648 endy -71418.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2472 0 cap 1
	color 0 6
 dis 0 picpos begx -11293.273 begy 47212.5 endx -11292.273 endy 47212.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5920 0 cap 1
	color 0 5
 dis 0 picpos begx 42097.656 begy 43862.5 endx 42098.656 endy 43862.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8237 0 cap 1
	color 0 5
 dis 0 picpos begx 31460.188 begy -21603.5 endx 31461.188 endy -21603.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block6857 0 cap 1
	color 0 14
 dis 0 picpos begx 70929.408 begy 8309.859 endx 70930.408 endy 8309.859 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8235 0 cap 1
	color 0 6
 dis 0 picpos begx 51621.608 begy -20933.5 endx 51622.608 endy -20933.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7795 0 cap 1
	color 0 3
 dis 0 picpos begx -120470.544 begy -84987.504 endx -120469.544 endy -84987.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1706 0 cap 1
	color 0 5
 dis 0 picpos begx -83344.472 begy 93722.496 endx -83343.472 endy 93722.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1119 0 cap 1
	color 0 5
 dis 0 picpos begx -97547.368 begy 82587.504 endx -97546.368 endy 82587.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1042 0 cap 1
	color 0 6
 dis 0 picpos begx -117278.312 begy 80422.496 endx -117277.312 endy 80422.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block667 0 cap 1
	color 0 3
 dis 0 picpos begx -42935.516 begy 99562.496 endx -42934.516 endy 99562.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7161 0 cap 1
	color 0 6
 dis 0 picpos begx 97269.608 begy -43637.496 endx 97270.608 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5408 0 cap 1
	color 0 5
 dis 0 picpos begx 74273.448 begy -21603.5 endx 74274.448 endy -21603.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3047 0 cap 1
	color 0 5
 dis 0 picpos begx -19550.272 begy -68837.504 endx -19549.272 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4125 0 cap 1
	color 0 5
 dis 0 picpos begx -41212.272 begy -71418.304 endx -41211.272 endy -71418.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7708 0 cap 1
	color 0 5
 dis 0 picpos begx -74423.16 begy -71278.304 endx -74422.16 endy -71278.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3804 0 cap 1
	color 0 6
 dis 0 picpos begx -96628.08 begy -82312.496 endx -96627.08 endy -82312.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4819 0 cap 1
	color 0 5
 dis 0 picpos begx 25862.672 begy 43962.5 endx 25863.672 endy 43962.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4588 0 cap 1
	color 0 12
 dis 0 picpos begx 41447.656 begy 44612.5 endx 41448.656 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8254 0 cap 1
	color 0 13
 dis 0 picpos begx 50522.188 begy 24546.5 endx 50523.188 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5943 0 cap 1
	color 0 5
 dis 0 picpos begx 60691.36 begy 24546.5 endx 60692.36 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7436 0 cap 1
	color 0 5
 dis 0 picpos begx 99849.608 begy 1030.5 endx 99850.608 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4574 0 cap 1
	color 0 12
 dis 0 picpos begx 114811.216 begy 1680.5 endx 114812.216 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block625 0 cap 1
	color 0 4
 dis 0 picpos begx 124156.168 begy 2730.50775 endx 124157.168 endy 2730.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block350 0 cap 1
	color 0 6
 dis 0 picpos begx -89243.28 begy 57512.5 endx -89242.28 endy 57512.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1117 0 cap 1
	color 0 6
 dis 0 picpos begx -99147.368 begy 83187.504 endx -99146.368 endy 83187.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1061 0 cap 1
	color 0 6
 dis 0 picpos begx -117278.312 begy 77842.496 endx -117277.312 endy 77842.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block665 0 cap 1
	color 0 4
 dis 0 picpos begx -43535.516 begy 98312.496 endx -43534.516 endy 98312.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7402 0 cap 1
	color 0 6
 dis 0 picpos begx 82060.248 begy -40137.496 endx 82061.248 endy -40137.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5449 0 cap 1
	color 0 14
 dis 0 picpos begx 73173.448 begy -37424.568 endx 73174.448 endy -37424.568 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3255 0 cap 1
	color 0 12
 dis 0 picpos begx 43677.904 begy -68187.504 endx 43678.904 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3212 0 cap 1
	color 0 12
 dis 0 picpos begx 32730.562 begy -68187.504 endx 32731.562 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4456 0 cap 1
	color 0 5
 dis 0 picpos begx 2401.875 begy -68837.504 endx 2402.875 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3085 0 cap 1
	color 0 5
 dis 0 picpos begx -8251.258 begy -68837.504 endx -8250.258 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7633 0 cap 1
	color 0 5
 dis 0 picpos begx -84086.864 begy -82735.304 endx -84085.864 endy -82735.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7631 0 cap 1
	color 0 6
 dis 0 picpos begx -85186.864 begy -82135.304 endx -85185.864 endy -82135.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3987 0 cap 1
	color 0 5
 dis 0 picpos begx -52942.5 begy -71725.736 endx -52941.5 endy -71725.736 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9164 0 cap 1
	color 0 14
 dis 0 picpos begx 62731.904 begy 12768.148 endx 62732.904 endy 12768.148 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9307 0 cap 1
	color 0 13
 dis 0 picpos begx 74429.408 begy 9937.5 endx 74430.408 endy 9937.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9400 0 cap 1
	color 0 14
 dis 0 picpos begx 70929.408 begy 12768.148 endx 70930.408 endy 12768.148 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5557 0 cap 1
	color 0 11
 dis 0 picpos begx 97740.8 begy 5080.5 endx 97741.8 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8233 0 cap 1
	color 0 5
 dis 0 picpos begx 52521.608 begy -21533.5 endx 52522.608 endy -21533.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8216 0 cap 1
	color 0 6
 dis 0 picpos begx 62491.796 begy -21003.5 endx 62492.796 endy -21003.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block465 0 cap 1
	color 0 4
 dis 0 picpos begx 132106.72 begy 2730.5 endx 132107.72 endy 2730.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7827 0 cap 1
	color 0 5
 dis 0 picpos begx -100693.28 begy -94507.504 endx -100692.28 endy -94507.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9559 0 cap 1
	color 0 12
 dis 0 picpos begx -106349.208 begy -81987.504 endx -106348.208 endy -81987.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1233 0 cap 1
	color 0 12
 dis 0 picpos begx -54785.256 begy 97262.496 endx -54784.256 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1192 0 cap 1
	color 0 5
 dis 0 picpos begx -66523.272 begy 96612.496 endx -66522.272 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1151 0 cap 1
	color 0 6
 dis 0 picpos begx -84594.464 begy 83187.504 endx -84593.464 endy 83187.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8414 0 cap 1
	color 0 11
 dis 0 picpos begx 68678.808 begy -37174.568 endx 68679.808 endy -37174.568 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7165 0 cap 1
	color 0 11
 dis 0 picpos begx 117631.216 begy -44287.496 endx 117632.216 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3176 0 cap 1
	color 0 12
 dis 0 picpos begx 21587.28 begy -68187.504 endx 21588.28 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3142 0 cap 1
	color 0 5
 dis 0 picpos begx 12868.328 begy -68837.504 endx 12869.328 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4149 0 cap 1
	color 0 5
 dis 0 picpos begx -19550.272 begy -71418.304 endx -19549.272 endy -71418.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4011 0 cap 1
	color 0 5
 dis 0 picpos begx -31419.272 begy -71728.304 endx -31418.272 endy -71728.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7673 0 cap 1
	color 0 6
 dis 0 picpos begx -75523.16 begy -82312.496 endx -75522.16 endy -82312.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3890 0 cap 1
	color 0 11
 dis 0 picpos begx -94378.08 begy -96887.488 endx -94377.08 endy -96887.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3968 0 cap 1
	color 0 6
 dis 0 picpos begx -54042.5 begy -82309.92 endx -54041.5 endy -82309.92 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block448 0 cap 1
	color 0 5
 dis 0 picpos begx -8243.273 begy 53245.484 endx -8242.273 endy 53245.484 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4855 0 cap 1
	color 0 5
 dis 0 picpos begx 60691.36 begy 43962.5 endx 60692.36 endy 43962.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9111 0 cap 1
	color 0 4
 dis 0 picpos begx 68681.912 begy 12118.148 endx 68682.912 endy 12118.148 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5667 0 cap 1
	color 0 6
 dis 0 picpos begx 94890.8 begy 5730.5 endx 94891.8 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8250 0 cap 1
	color 0 14
 dis 0 picpos begx 51122.188 begy 25146.5 endx 51123.188 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5372 0 cap 1
	color 0 6
 dis 0 picpos begx 73573.448 begy -21003.5 endx 73574.448 endy -21003.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7435 0 cap 1
	color 0 5
 dis 0 picpos begx 99849.608 begy -2469.5 endx 99850.608 endy -2469.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7383 0 cap 1
	color 0 5
 dis 0 picpos begx 83660.248 begy -4469.5 endx 83661.248 endy -4469.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block352 0 cap 1
	color 0 6
 dis 0 picpos begx -89243.28 begy 61029.5 endx -89242.28 endy 61029.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4349 0 cap 1
	color 0 14
 dis 0 picpos begx -69523.28 begy 93412.496 endx -69522.28 endy 93412.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7140 0 cap 1
	color 0 6
 dis 0 picpos begx 114961.216 begy -43637.496 endx 114962.216 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3214 0 cap 1
	color 0 5
 dis 0 picpos begx 34880.56 begy -68837.504 endx 34881.56 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3290 0 cap 1
	color 0 12
 dis 0 picpos begx 55575.58 begy -68187.504 endx 55576.58 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3178 0 cap 1
	color 0 5
 dis 0 picpos begx 23737.28 begy -68837.504 endx 23738.28 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4173 0 cap 1
	color 0 5
 dis 0 picpos begx 2401.875 begy -71418.304 endx 2402.875 endy -71418.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3887 0 cap 1
	color 0 6
 dis 0 picpos begx -96628.08 begy -96237.512 endx -96627.08 endy -96237.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3909 0 cap 1
	color 0 6
 dis 0 picpos begx -96628.08 begy -93657.512 endx -96627.08 endy -93657.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4091 0 cap 1
	color 0 5
 dis 0 picpos begx -62491.648 begy -82912.496 endx -62490.648 endy -82912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7675 0 cap 1
	color 0 5
 dis 0 picpos begx -74423.16 begy -82912.496 endx -74422.16 endy -82912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2454 0 cap 1
	color 0 11
 dis 0 picpos begx -6793.2735 begy 47212.5 endx -6792.2735 endy 47212.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2626 0 cap 1
	color 0 3
 dis 0 picpos begx 60738.312 begy 46162.5 endx 60739.312 endy 46162.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2502 0 cap 1
	color 0 4
 dis 0 picpos begx 60138.312 begy 45662.5 endx 60139.312 endy 45662.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4858 0 cap 1
	color 0 6
 dis 0 picpos begx 59791.36 begy 25146.5 endx 59792.36 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9146 0 cap 1
	color 0 6
 dis 0 picpos begx 63131.904 begy 15631.641 endx 63132.904 endy 15631.641 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5594 0 cap 1
	color 0 11
 dis 0 picpos begx 115082.168 begy 5080.5 endx 115083.168 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7429 0 cap 1
	color 0 5
 dis 0 picpos begx 117481.216 begy 1030.5 endx 117482.216 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4560 0 cap 1
	color 0 12
 dis 0 picpos begx 124883.28 begy 1680.5 endx 124884.28 endy 1680.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block227 0 cap 1
	color 0 5
 dis 0 picpos begx -83843.28 begy 65912.5 endx -83842.28 endy 65912.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block742 0 cap 1
	color 0 4
 dis 0 picpos begx -70639.912 begy 66962.5 endx -70638.912 endy 66962.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block253 0 cap 1
	color 0 12
 dis 0 picpos begx -89393.28 begy 66562.5 endx -89392.28 endy 66562.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9583 0 cap 1
	color 0 4
 dis 0 picpos begx -109746.032 begy -81587.504 endx -109745.032 endy -81587.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1168 0 cap 1
	color 0 5
 dis 0 picpos begx -83344.472 begy 82587.504 endx -83343.472 endy 82587.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1699 0 cap 1
	color 0 6
 dis 0 picpos begx -99147.368 begy 72052.496 endx -99146.368 endy 72052.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block672 0 cap 1
	color 0 3
 dis 0 picpos begx 97.015625 begy 99562.496 endx 98.015625 endy 99562.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7423 0 cap 1
	color 0 6
 dis 0 picpos begx 98269.608 begy -40137.496 endx 98270.608 endy -40137.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3356 0 cap 1
	color 0 12
 dis 0 picpos begx 75248.912 begy -68187.504 endx 75249.912 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3257 0 cap 1
	color 0 5
 dis 0 picpos begx 45927.904 begy -68837.504 endx 45928.904 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4035 0 cap 1
	color 0 5
 dis 0 picpos begx -9251.258 begy -71728.304 endx -9250.258 endy -71728.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4458 0 cap 1
	color 0 13
 dis 0 picpos begx -7851.258 begy -72937.504 endx -7850.258 endy -72937.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3992 0 cap 1
	color 0 6
 dis 0 picpos begx -32519.272 begy -82312.496 endx -32518.272 endy -82312.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4112 0 cap 1
	color 0 6
 dis 0 picpos begx -42312.272 begy -82312.496 endx -42311.272 endy -82312.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3971 0 cap 1
	color 0 5
 dis 0 picpos begx -52942.5 begy -82909.92 endx -52941.5 endy -82909.92 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7703 0 cap 1
	color 0 6
 dis 0 picpos begx -85186.864 begy -91268.12 endx -85185.864 endy -91268.12 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4088 0 cap 1
	color 0 6
 dis 0 picpos begx -63591.648 begy -82312.496 endx -63590.648 endy -82312.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block450 0 cap 1
	color 0 6
 dis 0 picpos begx -11293.273 begy 61029.5 endx -11292.273 endy 61029.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9302 0 cap 1
	color 0 3
 dis 0 picpos begx 75079.408 begy 10587.5 endx 75080.408 endy 10587.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8213 0 cap 1
	color 0 5
 dis 0 picpos begx 63391.796 begy -21603.5 endx 63392.796 endy -21603.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7160 0 cap 1
	color 0 13
 dis 0 picpos begx 100249.608 begy -6770.914 endx 100250.608 endy -6770.914 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block320 0 cap 1
	color 0 5
 dis 0 picpos begx -106043.272 begy 71526.768 endx -106042.272 endy 71526.768 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9058 0 cap 1
	color 0 3
 dis 0 picpos begx -105112.28 begy 67462.496 endx -105111.28 endy 67462.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1630 0 cap 1
	color 0 12
 dis 0 picpos begx -45694.912 begy 97262.496 endx -45693.912 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1235 0 cap 1
	color 0 5
 dis 0 picpos begx -52035.256 begy 96612.496 endx -52034.256 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1623 0 cap 1
	color 0 3
 dis 0 picpos begx -110242.768 begy 76262.496 endx -110241.768 endy 76262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block670 0 cap 1
	color 0 4
 dis 0 picpos begx -502.984375 begy 98312.496 endx -501.984375 endy 98312.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4559 0 cap 1
	color 0 11
 dis 0 picpos begx 127031.688 begy -44287.496 endx 127032.688 endy -44287.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7378 0 cap 1
	color 0 6
 dis 0 picpos begx 114961.216 begy -40137.496 endx 114962.216 endy -40137.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3569 0 cap 1
	color 0 4
 dis 0 picpos begx 131906.72 begy -67137.504 endx 131907.72 endy -67137.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3325 0 cap 1
	color 0 12
 dis 0 picpos begx 61728.112 begy -68187.504 endx 61729.112 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3923 0 cap 1
	color 0 5
 dis 0 picpos begx 34880.56 begy -71418.304 endx 34881.56 endy -71418.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4059 0 cap 1
	color 0 5
 dis 0 picpos begx 11868.328 begy -71728.304 endx 11869.328 endy -71728.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4115 0 cap 1
	color 0 5
 dis 0 picpos begx -41212.272 begy -82912.496 endx -41211.272 endy -82912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7720 0 cap 1
	color 0 13
 dis 0 picpos begx -83686.864 begy -92950.304 endx -83685.864 endy -92950.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7623 0 cap 1
	color 0 6
 dis 0 picpos begx -86186.864 begy -96237.504 endx -86185.864 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9083 0 cap 1
	color 0 12
 dis 0 picpos begx 65175.768 begy 44612.5 endx 65176.768 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4853 0 cap 1
	color 0 12
 dis 0 picpos begx 59641.36 begy 44612.5 endx 59642.36 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5597 0 cap 1
	color 0 6
 dis 0 picpos begx 112432.168 begy 5730.5 endx 112433.168 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5680 0 cap 1
	color 0 11
 dis 0 picpos begx 128285.72 begy 5080.5 endx 128286.72 endy 5080.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7403 0 cap 1
	color 0 6
 dis 0 picpos begx 82060.248 begy -20948.688 endx 82061.248 endy -20948.688 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block833 0 cap 1
	color 0 4
 dis 0 picpos begx -31011.734 begy 66962.5 endx -31010.734 endy 66962.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block765 0 cap 1
	color 0 3
 dis 0 picpos begx -70039.912 begy 67462.496 endx -70038.912 endy 67462.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1803 0 cap 1
	color 0 5
 dis 0 picpos begx -67523.272 begy 91822.496 endx -67522.272 endy 91822.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1658 0 cap 1
	color 0 13
 dis 0 picpos begx -81944.472 begy 76362.496 endx -81943.472 endy 76362.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1105 0 cap 1
	color 0 11
 dis 0 picpos begx -97397.368 begy 68512.496 endx -97396.368 endy 68512.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7404 0 cap 1
	color 0 5
 dis 0 picpos begx 83660.248 begy -21548.688 endx 83661.248 endy -21548.688 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4555 0 cap 1
	color 0 6
 dis 0 picpos begx 125033.28 begy -43637.496 endx 125034.28 endy -43637.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3327 0 cap 1
	color 0 5
 dis 0 picpos begx 63978.112 begy -68837.504 endx 63979.112 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3292 0 cap 1
	color 0 5
 dis 0 picpos begx 57225.58 begy -68837.504 endx 57226.58 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4016 0 cap 1
	color 0 6
 dis 0 picpos begx -10351.258 begy -82312.496 endx -10350.258 endy -82312.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4136 0 cap 1
	color 0 6
 dis 0 picpos begx -20650.272 begy -82142.496 endx -20649.272 endy -82142.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3995 0 cap 1
	color 0 5
 dis 0 picpos begx -31419.272 begy -82912.496 endx -31418.272 endy -82912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7706 0 cap 1
	color 0 6
 dis 0 picpos begx -75523.16 begy -91355.312 endx -75522.16 endy -91355.312 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2954 0 cap 1
	color 0 11
 dis 0 picpos begx -83936.864 begy -96887.504 endx -83935.864 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7661 0 cap 1
	color 0 11
 dis 0 picpos begx -73273.16 begy -96887.504 endx -73272.16 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2448 0 cap 1
	color 0 11
 dis 0 picpos begx 89106.72 begy 46562.5 endx 89107.72 endy 46562.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9110 0 cap 1
	color 0 6
 dis 0 picpos begx 63131.904 begy 26303.906 endx 63132.904 endy 26303.906 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9488 0 cap 1
	color 0 5
 dis 0 picpos begx 68431.912 begy 19288.906 endx 68432.912 endy 19288.906 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9304 0 cap 1
	color 0 14
 dis 0 picpos begx 94490.8 begy 10737.5 endx 94491.8 endy 10737.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5681 0 cap 1
	color 0 6
 dis 0 picpos begx 125335.72 begy 5730.5 endx 125336.72 endy 5730.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7370 0 cap 1
	color 0 5
 dis 0 picpos begx 116481.216 begy -2469.5 endx 116482.216 endy -2469.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4546 0 cap 1
	color 0 5
 dis 0 picpos begx 126881.696 begy 1030.5 endx 126882.696 endy 1030.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block255 0 cap 1
	color 0 12
 dis 0 picpos begx -11443.273 begy 66562.5 endx -11442.273 endy 66562.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1225 0 cap 1
	color 0 5
 dis 0 picpos begx -52035.256 begy 94032.496 endx -52034.256 endy 94032.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1196 0 cap 1
	color 0 6
 dis 0 picpos begx -69123.024 begy 83187.504 endx -69122.024 endy 83187.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1107 0 cap 1
	color 0 6
 dis 0 picpos begx -100147.368 begy 69162.496 endx -100146.368 endy 69162.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7849 0 cap 1
	color 0 4
 dis 0 picpos begx -8612.844 begy 98312.496 endx -8611.844 endy 98312.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4511 0 cap 1
	color 0 4
 dis 0 picpos begx 87283.112 begy -76787.504 endx 87284.112 endy -76787.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3358 0 cap 1
	color 0 5
 dis 0 picpos begx 76898.912 begy -68837.504 endx 76899.912 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3938 0 cap 1
	color 0 5
 dis 0 picpos begx 44927.904 begy -71278.304 endx 44928.904 endy -71278.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4040 0 cap 1
	color 0 6
 dis 0 picpos begx 10768.328 begy -82312.496 endx 10769.328 endy -82312.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4139 0 cap 1
	color 0 5
 dis 0 picpos begx -19550.272 begy -82742.496 endx -19549.272 endy -82742.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3874 0 cap 1
	color 0 6
 dis 0 picpos begx -43312.272 begy -96237.504 endx -43311.272 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4135 0 cap 1
	color 0 6
 dis 0 picpos begx -42312.272 begy -93347.512 endx -42311.272 endy -93347.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3880 0 cap 1
	color 0 11
 dis 0 picpos begx -51792.5 begy -96887.488 endx -51791.5 endy -96887.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3991 0 cap 1
	color 0 6
 dis 0 picpos begx -54042.5 begy -93654.944 endx -54041.5 endy -93654.944 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4111 0 cap 1
	color 0 6
 dis 0 picpos begx -63591.648 begy -93347.512 endx -63590.648 endy -93347.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3882 0 cap 1
	color 0 6
 dis 0 picpos begx -64591.648 begy -96237.512 endx -64590.648 endy -96237.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7663 0 cap 1
	color 0 6
 dis 0 picpos begx -75523.16 begy -96237.504 endx -75522.16 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block218 0 cap 1
	color 0 5
 dis 0 picpos begx -8243.273 begy 65912.5 endx -8242.273 endy 65912.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2483 0 cap 1
	color 0 6
 dis 0 picpos begx 83556.72 begy 47212.5 endx 83557.72 endy 47212.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7318 0 cap 1
	color 0 14
 dis 0 picpos begx 59391.36 begy 40235.64 endx 59392.36 endy 40235.64 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9492 0 cap 1
	color 0 5
 dis 0 picpos begx 68431.912 begy 22793.906 endx 68432.912 endy 22793.906 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9299 0 cap 1
	color 0 11
 dis 0 picpos begx 82393.376 begy 10987.5 endx 82394.376 endy 10987.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9305 0 cap 1
	color 0 4
 dis 0 picpos begx 93840.8 begy 10087.5 endx 93841.8 endy 10087.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7424 0 cap 1
	color 0 6
 dis 0 picpos begx 98269.608 begy -20948.688 endx 98270.608 endy -20948.688 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block756 0 cap 1
	color 0 3
 dis 0 picpos begx -30411.734 begy 67462.496 endx -30410.734 endy 67462.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8986 0 cap 1
	color 0 4
 dis 0 picpos begx -42724.056 begy -99187.504 endx -42723.056 endy -99187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1633 0 cap 1
	color 0 5
 dis 0 picpos begx -44244.912 begy 96612.496 endx -44243.912 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8868 0 cap 1
	color 0 6
 dis 0 picpos begx -45544.912 begy 83187.504 endx -45543.912 endy 83187.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1121 0 cap 1
	color 0 6
 dis 0 picpos begx -84594.464 begy 71742.496 endx -84593.464 endy 71742.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1289 0 cap 1
	color 0 12
 dis 0 picpos begx -31390.204 begy 97262.496 endx -31389.204 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block675 0 cap 1
	color 0 3
 dis 0 picpos begx 55094.92 begy 99562.496 endx 55095.92 endy 99562.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7425 0 cap 1
	color 0 5
 dis 0 picpos begx 99849.608 begy -21548.688 endx 99850.608 endy -21548.688 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4557 0 cap 1
	color 0 6
 dis 0 picpos begx 125033.28 begy -21003.5 endx 125034.28 endy -21003.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4509 0 cap 1
	color 0 3
 dis 0 picpos begx 87883.112 begy -76287.504 endx 87884.112 endy -76287.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3261 0 cap 1
	color 0 6
 dis 0 picpos begx 43827.904 begy -82312.496 endx 43828.904 endy -82312.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8942 0 cap 1
	color 0 5
 dis 0 picpos begx 57225.58 begy -82912.496 endx 57226.58 endy -82912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4083 0 cap 1
	color 0 5
 dis 0 picpos begx 22737.28 begy -71728.304 endx 22738.28 endy -71728.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4163 0 cap 1
	color 0 5
 dis 0 picpos begx 2401.875 begy -82912.496 endx 2402.875 endy -82912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4160 0 cap 1
	color 0 6
 dis 0 picpos begx 1401.875 begy -82312.496 endx 1402.875 endy -82312.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4019 0 cap 1
	color 0 5
 dis 0 picpos begx -9251.258 begy -82912.496 endx -9250.258 endy -82912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4015 0 cap 1
	color 0 6
 dis 0 picpos begx -32519.272 begy -93657.512 endx -32518.272 endy -93657.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3877 0 cap 1
	color 0 6
 dis 0 picpos begx -54042.5 begy -96237.512 endx -54041.5 endy -96237.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block239 0 cap 1
	color 0 12
 dis 0 picpos begx 82106.72 begy 65912.5 endx 82107.72 endy 65912.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5563 0 cap 1
	color 0 12
 dis 0 picpos begx 71179.408 begy 44612.5 endx 71180.408 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9182 0 cap 1
	color 0 5
 dis 0 picpos begx 65825.768 begy 43962.5 endx 65826.768 endy 43962.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9169 0 cap 1
	color 0 6
 dis 0 picpos begx 63131.904 begy 33714.56 endx 63132.904 endy 33714.56 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9239 0 cap 1
	color 0 6
 dis 0 picpos begx 78343.376 begy 14979 endx 78344.376 endy 14979 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5560 0 cap 1
	color 0 6
 dis 0 picpos begx 72329.408 begy 9658.93 endx 72330.408 endy 9658.93 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9371 0 cap 1
	color 0 13
 dis 0 picpos begx 97990.8 begy 16916.914 endx 97991.8 endy 16916.914 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9368 0 cap 1
	color 0 14
 dis 0 picpos begx 112032.168 begy 17716.914 endx 112033.168 endy 17716.914 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1138 0 cap 1
	color 0 11
 dis 0 picpos begx -82194.472 begy 68512.496 endx -82193.472 endy 68512.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1140 0 cap 1
	color 0 6
 dis 0 picpos begx -84594.464 begy 69162.496 endx -84593.464 endy 69162.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block673 0 cap 1
	color 0 4
 dis 0 picpos begx 54494.92 begy 98312.496 endx 54495.92 endy 98312.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7851 0 cap 1
	color 0 3
 dis 0 picpos begx 11715.953 begy 98912.496 endx 11716.953 endy 98912.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4544 0 cap 1
	color 0 5
 dis 0 picpos begx 126881.696 begy -21603.5 endx 126882.696 endy -21603.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4487 0 cap 1
	color 0 6
 dis 0 picpos begx 82547.752 begy -77687.504 endx 82548.752 endy -77687.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3364 0 cap 1
	color 0 5
 dis 0 picpos begx 76898.912 begy -82912.496 endx 76899.912 endy -82912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3220 0 cap 1
	color 0 5
 dis 0 picpos begx 34880.56 begy -82912.496 endx 34881.56 endy -82912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8940 0 cap 1
	color 0 6
 dis 0 picpos begx 55725.58 begy -82312.496 endx 55726.58 endy -82312.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4064 0 cap 1
	color 0 6
 dis 0 picpos begx 21737.28 begy -82312.496 endx 21738.28 endy -82312.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4043 0 cap 1
	color 0 5
 dis 0 picpos begx 11868.328 begy -82912.496 endx 11869.328 endy -82912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3041 0 cap 1
	color 0 6
 dis 0 picpos begx -21650.272 begy -96237.504 endx -21649.272 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4159 0 cap 1
	color 0 6
 dis 0 picpos begx -20650.272 begy -93347.512 endx -20649.272 endy -93347.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3004 0 cap 1
	color 0 11
 dis 0 picpos begx -30269.272 begy -96887.504 endx -30268.272 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7718 0 cap 1
	color 0 13
 dis 0 picpos begx -76423.16 begy -93037.504 endx -76422.16 endy -93037.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3885 0 cap 1
	color 0 11
 dis 0 picpos begx -62341.648 begy -96887.488 endx -62340.648 endy -96887.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block754 0 cap 1
	color 0 4
 dis 0 picpos begx 18021.61 begy 66312.5 endx 18022.61 endy 66312.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2634 0 cap 1
	color 0 3
 dis 0 picpos begx 113207.688 begy 46162.5 endx 113208.688 endy 46162.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2496 0 cap 1
	color 0 4
 dis 0 picpos begx 112607.688 begy 45662.5 endx 112608.688 endy 45662.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9426 0 cap 1
	color 0 11
 dis 0 picpos begx 65975.768 begy 40936.5 endx 65976.768 endy 40936.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9171 0 cap 1
	color 0 5
 dis 0 picpos begx 68431.912 begy 30103.906 endx 68432.912 endy 30103.906 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7493 0 cap 1
	color 0 5
 dis 0 picpos begx 73029.408 begy 24546.5 endx 73030.408 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9287 0 cap 1
	color 0 11
 dis 0 picpos begx 90726.84 begy 10987.5 endx 90727.84 endy 10987.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9243 0 cap 1
	color 0 6
 dis 0 picpos begx 78343.376 begy 18529.008 endx 78344.376 endy 18529.008 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5468 0 cap 1
	color 0 6
 dis 0 picpos begx 72329.408 begy 25146.5 endx 72330.408 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9375 0 cap 1
	color 0 4
 dis 0 picpos begx 111382.168 begy 17066.914 endx 111383.168 endy 17066.914 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1662 0 cap 1
	color 0 6
 dis 0 picpos begx -45544.912 begy 69162.496 endx -45543.912 endy 69162.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1198 0 cap 1
	color 0 5
 dis 0 picpos begx -67523.272 begy 82587.504 endx -67522.272 endy 82587.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block679 0 cap 1
	color 0 3
 dis 0 picpos begx 97009.952 begy 99562.496 endx 97010.952 endy 99562.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7380 0 cap 1
	color 0 5
 dis 0 picpos begx 116481.216 begy -21548.688 endx 116482.216 endy -21548.688 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3362 0 cap 1
	color 0 6
 dis 0 picpos begx 75398.912 begy -82312.496 endx 75399.912 endy -82312.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3218 0 cap 1
	color 0 6
 dis 0 picpos begx 33880.56 begy -82312.496 endx 33881.56 endy -82312.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3284 0 cap 1
	color 0 11
 dis 0 picpos begx 57375.58 begy -96887.504 endx 57376.58 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4067 0 cap 1
	color 0 5
 dis 0 picpos begx 22737.28 begy -82912.496 endx 22738.28 endy -82912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3006 0 cap 1
	color 0 6
 dis 0 picpos begx -32519.272 begy -96237.504 endx -32518.272 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3876 0 cap 1
	color 0 11
 dis 0 picpos begx -41062.272 begy -96887.504 endx -41061.272 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block381 0 cap 1
	color 0 5
 dis 0 picpos begx 88956.72 begy 53245.484 endx 88957.72 endy 53245.484 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9286 0 cap 1
	color 0 6
 dis 0 picpos begx 86177.768 begy 11796.625 endx 86178.768 endy 11796.625 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7487 0 cap 1
	color 0 5
 dis 0 picpos begx 96590.8 begy 24546.5 endx 96591.8 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block724 0 cap 1
	color 0 4
 dis 0 picpos begx 16895.704 begy 66962.5 endx 16896.704 endy 66962.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8983 0 cap 1
	color 0 3
 dis 0 picpos begx -42124.056 begy -97937.504 endx -42123.056 endy -97937.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4355 0 cap 1
	color 0 14
 dis 0 picpos begx -43344.912 begy 93412.496 endx -43343.912 endy 93412.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8867 0 cap 1
	color 0 5
 dis 0 picpos begx -44244.912 begy 82587.504 endx -44243.912 endy 82587.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1238 0 cap 1
	color 0 6
 dis 0 picpos begx -53635.256 begy 83187.504 endx -53634.256 endy 83187.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1342 0 cap 1
	color 0 12
 dis 0 picpos begx -8788.008 begy 97262.496 endx -8787.008 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1322 0 cap 1
	color 0 12
 dis 0 picpos begx -22140.914 begy 97262.496 endx -22139.914 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1291 0 cap 1
	color 0 5
 dis 0 picpos begx -28630.204 begy 96612.496 endx -28629.204 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block677 0 cap 1
	color 0 4
 dis 0 picpos begx 96409.952 begy 98312.496 endx 96410.952 endy 98312.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3463 0 cap 1
	color 0 12
 dis 0 picpos begx 127456.28 begy -68187.504 endx 127457.28 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3960 0 cap 1
	color 0 5
 dis 0 picpos begx 62978.112 begy -71728.304 endx 62979.112 endy -71728.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3263 0 cap 1
	color 0 5
 dis 0 picpos begx 44927.904 begy -82912.496 endx 44928.904 endy -82912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3286 0 cap 1
	color 0 6
 dis 0 picpos begx 55725.58 begy -96237.504 endx 55726.58 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4183 0 cap 1
	color 0 6
 dis 0 picpos begx 1401.875 begy -93347.512 endx 1402.875 endy -93347.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4039 0 cap 1
	color 0 6
 dis 0 picpos begx -10351.258 begy -93657.512 endx -10350.258 endy -93657.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2455 0 cap 1
	color 0 11
 dis 0 picpos begx 90406.72 begy 47212.5 endx 90407.72 endy 47212.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5559 0 cap 1
	color 0 5
 dis 0 picpos begx 74029.408 begy 43962.5 endx 74030.408 endy 43962.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9166 0 cap 1
	color 0 5
 dis 0 picpos begx 68431.912 begy 37233.656 endx 68432.912 endy 37233.656 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9282 0 cap 1
	color 0 6
 dis 0 picpos begx 86177.768 begy 15383.25 endx 86178.768 endy 15383.25 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9086 0 cap 1
	color 0 5
 dis 0 picpos begx 82243.376 begy 22109.024 endx 82244.376 endy 22109.024 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9240 0 cap 1
	color 0 6
 dis 0 picpos begx 78343.376 begy 25659.032 endx 78344.376 endy 25659.032 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9144 0 cap 1
	color 0 3
 dis 0 picpos begx 98640.8 begy 17566.914 endx 98641.8 endy 17566.914 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9351 0 cap 1
	color 0 12
 dis 0 picpos begx 102244.44 begy 16666.914 endx 102245.44 endy 16666.914 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9143 0 cap 1
	color 0 11
 dis 0 picpos begx 106454.264 begy 17966.914 endx 106455.264 endy 17966.914 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7379 0 cap 1
	color 0 6
 dis 0 picpos begx 114961.216 begy -20948.688 endx 114962.216 endy -20948.688 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1184 0 cap 1
	color 0 11
 dis 0 picpos begx -66373.272 begy 68512.496 endx -66372.272 endy 68512.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block866 0 cap 1
	color 0 4
 dis 0 picpos begx 22411.204 begy -99187.504 endx 22412.204 endy -99187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4353 0 cap 1
	color 0 14
 dis 0 picpos begx -31640.204 begy 93412.496 endx -31639.204 endy 93412.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1370 0 cap 1
	color 0 12
 dis 0 picpos begx 7049.203 begy 97258.328 endx 7050.203 endy 97258.328 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3458 0 cap 1
	color 0 12
 dis 0 picpos begx 114566.36 begy -68187.504 endx 114567.36 endy -68187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3391 0 cap 1
	color 0 5
 dis 0 picpos begx 84647.752 begy -78487.504 endx 84648.752 endy -78487.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3425 0 cap 1
	color 0 12
 dis 0 picpos begx 93317.808 begy -77837.504 endx 93318.808 endy -77837.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3350 0 cap 1
	color 0 11
 dis 0 picpos begx 77048.912 begy -96887.504 endx 77049.912 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3328 0 cap 1
	color 0 6
 dis 0 picpos begx 61878.112 begy -82312.496 endx 61879.112 endy -82312.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3936 0 cap 1
	color 0 6
 dis 0 picpos begx 43827.904 begy -91355.312 endx 43828.904 endy -91355.312 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3134 0 cap 1
	color 0 11
 dis 0 picpos begx 13018.328 begy -96887.504 endx 13019.328 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3517 0 cap 1
	color 0 6
 dis 0 picpos begx -10351.258 begy -96237.504 endx -10350.258 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4337 0 cap 1
	color 0 13
 dis 0 picpos begx -498.125 begy -93037.504 endx -497.125 endy -93037.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3039 0 cap 1
	color 0 11
 dis 0 picpos begx -19400.272 begy -96887.504 endx -19399.272 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5668 0 cap 1
	color 0 12
 dis 0 picpos begx 94740.8 begy 44612.5 endx 94741.8 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block835 0 cap 1
	color 0 4
 dis 0 picpos begx 131906.72 begy 45662.5 endx 131907.72 endy 45662.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block332 0 cap 1
	color 0 5
 dis 0 picpos begx 88956.72 begy 56712.5 endx 88957.72 endy 56712.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block382 0 cap 1
	color 0 6
 dis 0 picpos begx 83556.72 begy 57512.5 endx 83557.72 endy 57512.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7491 0 cap 1
	color 0 5
 dis 0 picpos begx 73029.408 begy 40462.5 endx 73030.408 endy 40462.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5558 0 cap 1
	color 0 6
 dis 0 picpos begx 95890.8 begy 9458.93 endx 95891.8 endy 9458.93 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1186 0 cap 1
	color 0 6
 dis 0 picpos begx -69124.272 begy 69162.496 endx -69123.272 endy 69162.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2844 0 cap 1
	color 0 11
 dis 0 picpos begx -44094.912 begy 68512.496 endx -44093.912 endy 68512.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1227 0 cap 1
	color 0 11
 dis 0 picpos begx -51885.256 begy 68512.496 endx -51884.256 endy 68512.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1167 0 cap 1
	color 0 6
 dis 0 picpos begx -69123.272 begy 71742.496 endx -69122.272 endy 71742.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8011 0 cap 1
	color 0 12
 dis 0 picpos begx -363.375 begy 97262.496 endx -362.375 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1281 0 cap 1
	color 0 5
 dis 0 picpos begx -28630.204 begy 94032.496 endx -28629.204 endy 94032.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3460 0 cap 1
	color 0 5
 dis 0 picpos begx 116216.36 begy -68837.504 endx 116217.36 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4467 0 cap 1
	color 0 12
 dis 0 picpos begx 106816.088 begy -77837.504 endx 106817.088 endy -77837.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3395 0 cap 1
	color 0 6
 dis 0 picpos begx 82547.752 begy -87137.504 endx 82548.752 endy -87137.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3352 0 cap 1
	color 0 6
 dis 0 picpos begx 75398.912 begy -96237.504 endx 75399.912 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4343 0 cap 1
	color 0 13
 dis 0 picpos begx 35280.56 begy -93037.504 endx 35281.56 endy -93037.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3933 0 cap 1
	color 0 6
 dis 0 picpos begx 33880.56 begy -91355.312 endx 33881.56 endy -91355.312 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3208 0 cap 1
	color 0 6
 dis 0 picpos begx 32880.562 begy -96237.504 endx 32881.562 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3170 0 cap 1
	color 0 11
 dis 0 picpos begx 23887.28 begy -96887.504 endx 23888.28 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3136 0 cap 1
	color 0 6
 dis 0 picpos begx 10768.328 begy -96237.504 endx 10769.328 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4063 0 cap 1
	color 0 6
 dis 0 picpos begx 10768.328 begy -93657.512 endx 10769.328 endy -93657.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4339 0 cap 1
	color 0 13
 dis 0 picpos begx -7851.258 begy -93037.504 endx -7850.258 endy -93037.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3103 0 cap 1
	color 0 6
 dis 0 picpos begx 401.875 begy -96237.504 endx 402.875 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5467 0 cap 1
	color 0 12
 dis 0 picpos begx 112282.168 begy 44612.5 endx 112283.168 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block832 0 cap 1
	color 0 11
 dis 0 picpos begx 131718.064 begy 47212.5 endx 131719.064 endy 47212.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9316 0 cap 1
	color 0 13
 dis 0 picpos begx 74429.408 begy 36409.064 endx 74430.408 endy 36409.064 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9284 0 cap 1
	color 0 5
 dis 0 picpos begx 90576.84 begy 18933.602 endx 90577.84 endy 18933.602 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9280 0 cap 1
	color 0 6
 dis 0 picpos begx 86177.768 begy 22701.734 endx 86178.768 endy 22701.734 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9253 0 cap 1
	color 0 5
 dis 0 picpos begx 82243.376 begy 29209.04 endx 82244.376 endy 29209.04 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9242 0 cap 1
	color 0 6
 dis 0 picpos begx 78343.376 begy 32759.048 endx 78344.376 endy 32759.048 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9417 0 cap 1
	color 0 6
 dis 0 picpos begx 102394.44 begy 12610.203 endx 102395.44 endy 12610.203 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7490 0 cap 1
	color 0 5
 dis 0 picpos begx 96590.8 begy 40462.5 endx 96591.8 endy 40462.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5605 0 cap 1
	color 0 6
 dis 0 picpos begx 95890.8 begy 25146.5 endx 95891.8 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9427 0 cap 1
	color 0 13
 dis 0 picpos begx 108334.248 begy 8724.172 endx 108335.248 endy 8724.172 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1319 0 cap 1
	color 0 11
 dis 0 picpos begx -20840.914 begy 68512.496 endx -20839.914 endy 68512.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1283 0 cap 1
	color 0 11
 dis 0 picpos begx -28480.204 begy 68512.496 endx -28479.204 endy 68512.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4370 0 cap 1
	color 0 3
 dis 0 picpos begx -31095.11 begy -97937.504 endx -31094.11 endy -97937.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1741 0 cap 1
	color 0 6
 dis 0 picpos begx -53635.256 begy 72052.496 endx -53634.256 endy 72052.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1674 0 cap 1
	color 0 5
 dis 0 picpos begx -7038.008 begy 96612.496 endx -7037.008 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1317 0 cap 1
	color 0 5
 dis 0 picpos begx -20990.914 begy 96612.496 endx -20989.914 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8874 0 cap 1
	color 0 6
 dis 0 picpos begx -21990.914 begy 83187.504 endx -21989.914 endy 83187.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block681 0 cap 1
	color 0 4
 dis 0 picpos begx 132106.72 begy 98312.496 endx 132107.72 endy 98312.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7994 0 cap 1
	color 0 5
 dis 0 picpos begx 1886.625 begy 96612.496 endx 1887.625 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3465 0 cap 1
	color 0 5
 dis 0 picpos begx 129706.28 begy -68837.504 endx 129707.28 endy -68837.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3949 0 cap 1
	color 0 5
 dis 0 picpos begx 62978.112 begy -82912.496 endx 62979.112 endy -82912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3249 0 cap 1
	color 0 11
 dis 0 picpos begx 46077.904 begy -96887.504 endx 46078.904 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3319 0 cap 1
	color 0 11
 dis 0 picpos begx 64128.112 begy -96887.504 endx 64129.112 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3321 0 cap 1
	color 0 6
 dis 0 picpos begx 61878.112 begy -96237.504 endx 61879.112 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3172 0 cap 1
	color 0 6
 dis 0 picpos begx 21737.28 begy -96237.504 endx 21738.28 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4087 0 cap 1
	color 0 6
 dis 0 picpos begx 21737.28 begy -93657.512 endx 21738.28 endy -93657.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3101 0 cap 1
	color 0 11
 dis 0 picpos begx 2551.875 begy -96887.504 endx 2552.875 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block59 0 cap 1
	color 0 3
 dis 0 picpos begx 68886.72 begy 68112.496 endx 68887.72 endy 68112.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block228 0 cap 1
	color 0 12
 dis 0 picpos begx 83406.72 begy 66562.5 endx 83407.72 endy 66562.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1538 0 cap 1
	color 0 6
 dis 0 picpos begx 18172.656 begy 70041.912 endx 18173.656 endy 70041.912 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9085 0 cap 1
	color 0 12
 dis 0 picpos begx 102244.44 begy 44612.5 endx 102245.44 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block384 0 cap 1
	color 0 6
 dis 0 picpos begx 83556.72 begy 61029.5 endx 83557.72 endy 61029.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9208 0 cap 1
	color 0 12
 dis 0 picpos begx 78193.376 begy 36159.064 endx 78194.376 endy 36159.064 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9343 0 cap 1
	color 0 6
 dis 0 picpos begx 102394.44 begy 20594.938 endx 102395.44 endy 20594.938 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5620 0 cap 1
	color 0 6
 dis 0 picpos begx 113432.168 begy 9230.5 endx 113433.168 endy 9230.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9418 0 cap 1
	color 0 5
 dis 0 picpos begx 106304.264 begy 24372.96 endx 106305.264 endy 24372.96 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7496 0 cap 1
	color 0 5
 dis 0 picpos begx 113932.168 begy 26068.828 endx 113933.168 endy 26068.828 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1341 0 cap 1
	color 0 11
 dis 0 picpos begx -6888.008 begy 68512.496 endx -6887.008 endy 68512.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1285 0 cap 1
	color 0 6
 dis 0 picpos begx -31240.204 begy 69162.496 endx -31239.204 endy 69162.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block868 0 cap 1
	color 0 3
 dis 0 picpos begx 23011.204 begy -97937.504 endx 23012.204 endy -97937.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4184 0 cap 1
	color 0 6
 dis 0 picpos begx 114716.36 begy -79812.496 endx 114717.36 endy -79812.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3427 0 cap 1
	color 0 5
 dis 0 picpos begx 95573.856 begy -78487.504 endx 95574.856 endy -78487.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4341 0 cap 1
	color 0 13
 dis 0 picpos begx 42927.904 begy -93037.504 endx 42928.904 endy -93037.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3078 0 cap 1
	color 0 11
 dis 0 picpos begx -8101.258 begy -96887.504 endx -8100.258 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8995 0 cap 1
	color 0 6
 dis 0 picpos begx 65156.72 begy 69842.496 endx 65157.72 endy 69842.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9342 0 cap 1
	color 0 5
 dis 0 picpos begx 106304.264 begy 43695.56 endx 106305.264 endy 43695.56 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5669 0 cap 1
	color 0 5
 dis 0 picpos begx 97590.8 begy 43962.5 endx 97591.8 endy 43962.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9298 0 cap 1
	color 0 5
 dis 0 picpos begx 90576.84 begy 26254.766 endx 90577.84 endy 26254.766 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9087 0 cap 1
	color 0 6
 dis 0 picpos begx 86177.768 begy 30039.656 endx 86178.768 endy 30039.656 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5622 0 cap 1
	color 0 6
 dis 0 picpos begx 113432.168 begy 26668.828 endx 113433.168 endy 26668.828 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9405 0 cap 1
	color 0 6
 dis 0 picpos begx 107434.248 begy 6574.172 endx 107435.248 endy 6574.172 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1670 0 cap 1
	color 0 6
 dis 0 picpos begx -8638.008 begy 69162.496 endx -8637.008 endy 69162.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block864 0 cap 1
	color 0 4
 dis 0 picpos begx 76546.952 begy -99187.504 endx 76547.952 endy -99187.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1672 0 cap 1
	color 0 5
 dis 0 picpos begx -7038.008 begy 82595.856 endx -7037.008 endy 82595.856 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1561 0 cap 1
	color 0 12
 dis 0 picpos begx 62615.904 begy 97262.496 endx 62616.904 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1858 0 cap 1
	color 0 12
 dis 0 picpos begx 40009.984 begy 97260.304 endx 40010.984 endy 97260.304 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block174 0 cap 1
	color 0 12
 dis 0 picpos begx 18022.22 begy 97262.496 endx 18023.22 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8026 0 cap 1
	color 0 6
 dis 0 picpos begx 7199.203 begy 83187.504 endx 7200.203 endy 83187.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3397 0 cap 1
	color 0 5
 dis 0 picpos begx 84647.752 begy -87737.504 endx 84648.752 endy -87737.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3384 0 cap 1
	color 0 11
 dis 0 picpos begx 84797.752 begy -96887.504 endx 84798.752 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3251 0 cap 1
	color 0 6
 dis 0 picpos begx 43827.904 begy -96237.504 endx 43828.904 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3206 0 cap 1
	color 0 11
 dis 0 picpos begx 35030.56 begy -96887.504 endx 35031.56 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3958 0 cap 1
	color 0 6
 dis 0 picpos begx 61878.112 begy -93657.512 endx 61879.112 endy -93657.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block194 0 cap 1
	color 0 3
 dis 0 picpos begx 70440.448 begy 67462.496 endx 70441.448 endy 67462.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8057 0 cap 1
	color 0 6
 dis 0 picpos begx 19172.22 begy 72551.912 endx 19173.22 endy 72551.912 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5686 0 cap 1
	color 0 12
 dis 0 picpos begx 125185.72 begy 44612.5 endx 125186.72 endy 44612.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5608 0 cap 1
	color 0 5
 dis 0 picpos begx 114932.168 begy 43962.5 endx 114933.168 endy 43962.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1620 0 cap 1
	color 0 4
 dis 0 picpos begx 129138.064 begy 66312.5 endx 129139.064 endy 66312.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9323 0 cap 1
	color 0 3
 dis 0 picpos begx 75079.408 begy 37213.968 endx 75080.408 endy 37213.968 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9359 0 cap 1
	color 0 13
 dis 0 picpos begx 97990.8 begy 35257.5 endx 97991.8 endy 35257.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9337 0 cap 1
	color 0 6
 dis 0 picpos begx 102394.44 begy 25172.96 endx 102395.44 endy 25172.96 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8010 0 cap 1
	color 0 11
 dis 0 picpos begx 2036.625 begy 68512.496 endx 2037.625 endy 68512.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1305 0 cap 1
	color 0 6
 dis 0 picpos begx -21990.914 begy 69162.496 endx -21989.914 endy 69162.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1665 0 cap 1
	color 0 6
 dis 0 picpos begx -8638.008 begy 83195.856 endx -8637.008 endy 83195.856 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8873 0 cap 1
	color 0 5
 dis 0 picpos begx -20990.914 begy 82587.504 endx -20989.914 endy 82587.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1435 0 cap 1
	color 0 12
 dis 0 picpos begx 94953.472 begy 97262.496 endx 94954.472 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1522 0 cap 1
	color 0 12
 dis 0 picpos begx 72766.448 begy 97262.496 endx 72767.448 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1839 0 cap 1
	color 0 12
 dis 0 picpos begx 28067.124 begy 97262.496 endx 28068.124 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1859 0 cap 1
	color 0 5
 dis 0 picpos begx 42259.984 begy 96610.304 endx 42260.984 endy 96610.304 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8039 0 cap 1
	color 0 5
 dis 0 picpos begx 7799.203 begy 93722.496 endx 7800.203 endy 93722.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4464 0 cap 1
	color 0 5
 dis 0 picpos begx 109066.088 begy -78487.504 endx 109067.088 endy -78487.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3469 0 cap 1
	color 0 6
 dis 0 picpos begx 127606.28 begy -82312.496 endx 127607.28 endy -82312.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3454 0 cap 1
	color 0 6
 dis 0 picpos begx 114716.36 begy -96237.504 endx 114717.36 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3386 0 cap 1
	color 0 6
 dis 0 picpos begx 82547.752 begy -96237.504 endx 82548.752 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3431 0 cap 1
	color 0 6
 dis 0 picpos begx 93467.808 begy -87137.504 endx 93468.808 endy -87137.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2848 0 cap 1
	color 0 11
 dis 0 picpos begx 75166.448 begy 68512.496 endx 75167.448 endy 68512.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block324 0 cap 1
	color 0 5
 dis 0 picpos begx 88956.72 begy 65912.5 endx 88957.72 endy 65912.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1351 0 cap 1
	color 0 6
 dis 0 picpos begx 7199.203 begy 69158.328 endx 7200.203 endy 69158.328 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9360 0 cap 1
	color 0 6
 dis 0 picpos begx 102394.44 begy 39925.56 endx 102395.44 endy 39925.56 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9325 0 cap 1
	color 0 11
 dis 0 picpos begx 106454.264 begy 36307.5 endx 106455.264 endy 36307.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9312 0 cap 1
	color 0 14
 dis 0 picpos begx 94490.8 begy 37363.968 endx 94491.8 endy 37363.968 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9288 0 cap 1
	color 0 5
 dis 0 picpos begx 90576.84 begy 33725.968 endx 90577.84 endy 33725.968 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9190 0 cap 1
	color 0 12
 dis 0 picpos begx 86027.768 begy 36159.064 endx 86028.768 endy 36159.064 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9361 0 cap 1
	color 0 14
 dis 0 picpos begx 112032.168 begy 36057.5 endx 112033.168 endy 36057.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9338 0 cap 1
	color 0 12
 dis 0 picpos begx 102244.44 begy 35007.5 endx 102245.44 endy 35007.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9373 0 cap 1
	color 0 4
 dis 0 picpos begx 111382.168 begy 35407.5 endx 111383.168 endy 35407.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block7488 0 cap 1
	color 0 5
 dis 0 picpos begx 113932.168 begy 40462.5 endx 113933.168 endy 40462.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5606 0 cap 1
	color 0 5
 dis 0 picpos begx 127135.72 begy 24546.5 endx 127136.72 endy 24546.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8876 0 cap 1
	color 0 6
 dis 0 picpos begx -213.375 begy 69158.328 endx -212.375 endy 69158.328 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1295 0 cap 1
	color 0 6
 dis 0 picpos begx -30240.204 begy 83187.504 endx -30239.204 endy 83187.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1409 0 cap 1
	color 0 12
 dis 0 picpos begx 82216.472 begy 97262.496 endx 82217.472 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1817 0 cap 1
	color 0 5
 dis 0 picpos begx 30417.124 begy 96612.496 endx 30418.124 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8040 0 cap 1
	color 0 6
 dis 0 picpos begx 7199.203 begy 71742.496 endx 7200.203 endy 71742.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4187 0 cap 1
	color 0 5
 dis 0 picpos begx 116216.36 begy -80412.496 endx 116217.36 endy -80412.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4271 0 cap 1
	color 0 6
 dis 0 picpos begx 106964.088 begy -87137.504 endx 106965.088 endy -87137.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block870 0 cap 1
	color 0 3
 dis 0 picpos begx 77146.952 begy -97937.504 endx 77147.952 endy -97937.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2846 0 cap 1
	color 0 6
 dis 0 picpos begx 72916.448 begy 69162.496 endx 72917.448 endy 69162.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block751 0 cap 1
	color 0 4
 dis 0 picpos begx 116967.664 begy 66962.5 endx 116968.664 endy 66962.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1647 0 cap 1
	color 0 13
 dis 0 picpos begx 20672.22 begy 79362.496 endx 20673.22 endy 79362.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8929 0 cap 1
	color 0 11
 dis 0 picpos begx 126795.248 begy 68512.496 endx 126796.248 endy 68512.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9267 0 cap 1
	color 0 11
 dis 0 picpos begx 82393.376 begy 37613.968 endx 82394.376 endy 37613.968 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9317 0 cap 1
	color 0 4
 dis 0 picpos begx 93840.8 begy 36559.064 endx 93841.8 endy 36559.064 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5676 0 cap 1
	color 0 6
 dis 0 picpos begx 126335.72 begy 9230.5 endx 126336.72 endy 9230.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1749 0 cap 1
	color 0 6
 dis 0 picpos begx -30240.204 begy 72052.496 endx -30239.204 endy 72052.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1477 0 cap 1
	color 0 12
 dis 0 picpos begx 103555.472 begy 97262.496 endx 103556.472 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1591 0 cap 1
	color 0 5
 dis 0 picpos begx 84966.472 begy 96612.496 endx 84967.472 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1564 0 cap 1
	color 0 5
 dis 0 picpos begx 64765.904 begy 96612.496 endx 64766.904 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1649 0 cap 1
	color 0 5
 dis 0 picpos begx 20272.22 begy 96612.496 endx 20273.22 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4359 0 cap 1
	color 0 14
 dis 0 picpos begx 17772.656 begy 93412.496 endx 17773.656 endy 93412.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4357 0 cap 1
	color 0 14
 dis 0 picpos begx 9699.203 begy 93412.496 endx 9700.203 endy 93412.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8031 0 cap 1
	color 0 5
 dis 0 picpos begx 7799.203 begy 82587.504 endx 7800.203 endy 82587.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3471 0 cap 1
	color 0 5
 dis 0 picpos begx 129706.28 begy -82912.496 endx 129707.28 endy -82912.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2857 0 cap 1
	color 0 6
 dis 0 picpos begx 72916.448 begy 71742.496 endx 72917.448 endy 71742.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5588 0 cap 1
	color 0 5
 dis 0 picpos begx 128135.72 begy 43962.5 endx 128136.72 endy 43962.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9237 0 cap 1
	color 0 6
 dis 0 picpos begx 78343.376 begy 39859.064 endx 78344.376 endy 39859.064 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9369 0 cap 1
	color 0 3
 dis 0 picpos begx 98640.8 begy 35907.5 endx 98641.8 endy 35907.5 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5679 0 cap 1
	color 0 6
 dis 0 picpos begx 126335.72 begy 25146.5 endx 126336.72 endy 25146.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8894 0 cap 1
	color 0 6
 dis 0 picpos begx -213.375 begy 71742.496 endx -212.375 endy 71742.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8880 0 cap 1
	color 0 6
 dis 0 picpos begx -213.375 begy 83057.504 endx -212.375 endy 83057.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1517 0 cap 1
	color 0 12
 dis 0 picpos begx 118898.552 begy 97262.496 endx 118899.552 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1519 0 cap 1
	color 0 5
 dis 0 picpos begx 75016.448 begy 96612.496 endx 75017.448 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1437 0 cap 1
	color 0 5
 dis 0 picpos begx 97803.472 begy 96612.496 endx 97804.472 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8958 0 cap 1
	color 0 13
 dis 0 picpos begx 116616.36 begy -85289.856 endx 116617.36 endy -85289.856 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3433 0 cap 1
	color 0 5
 dis 0 picpos begx 95573.856 begy -87737.504 endx 95574.856 endy -87737.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4393 0 cap 1
	color 0 3
 dis 0 picpos begx 97038.968 begy -97937.504 endx 97039.968 endy -97937.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1405 0 cap 1
	color 0 11
 dis 0 picpos begx 85116.472 begy 68512.496 endx 85117.472 endy 68512.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8431 0 cap 1
	color 0 3
 dis 0 picpos begx 21322.22 begy 81311.912 endx 21323.22 endy 81311.912 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9130 0 cap 1
	color 0 11
 dis 0 picpos begx 90726.84 begy 37613.968 endx 90727.84 endy 37613.968 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1512 0 cap 1
	color 0 11
 dis 0 picpos begx 121648.552 begy 68512.496 endx 121649.552 endy 68512.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block5570 0 cap 1
	color 0 5
 dis 0 picpos begx 127135.72 begy 40462.5 endx 127136.72 endy 40462.5 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8934 0 cap 1
	color 0 12
 dis 0 picpos begx 125195.248 begy 97262.496 endx 125196.248 endy 97262.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1475 0 cap 1
	color 0 5
 dis 0 picpos begx 105555.472 begy 96612.496 endx 105556.472 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8050 0 cap 1
	color 0 5
 dis 0 picpos begx 20272.22 begy 94031.912 endx 20273.22 endy 94031.912 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4264 0 cap 1
	color 0 11
 dis 0 picpos begx 109216.088 begy -96887.504 endx 109217.088 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3452 0 cap 1
	color 0 11
 dis 0 picpos begx 116366.36 begy -96887.504 endx 116367.36 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3421 0 cap 1
	color 0 6
 dis 0 picpos begx 93467.808 begy -96237.504 endx 93468.808 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block3419 0 cap 1
	color 0 11
 dis 0 picpos begx 95723.856 begy -96887.504 endx 95724.856 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1408 0 cap 1
	color 0 6
 dis 0 picpos begx 82366.472 begy 69162.496 endx 82367.472 endy 69162.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8927 0 cap 1
	color 0 6
 dis 0 picpos begx 125345.248 begy 69162.496 endx 125346.248 endy 69162.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8933 0 cap 1
	color 0 5
 dis 0 picpos begx 126645.248 begy 96612.496 endx 126646.248 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1612 0 cap 1
	color 0 5
 dis 0 picpos begx 97803.472 begy 93722.496 endx 97804.472 endy 93722.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1861 0 cap 1
	color 0 6
 dis 0 picpos begx 40159.984 begy 82362.496 endx 40160.984 endy 82362.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4273 0 cap 1
	color 0 5
 dis 0 picpos begx 109066.088 begy -87737.504 endx 109067.088 endy -87737.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4299 0 cap 1
	color 0 6
 dis 0 picpos begx 127606.28 begy -96237.504 endx 127607.28 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4347 0 cap 1
	color 0 13
 dis 0 picpos begx 95973.856 begy -93037.504 endx 95974.856 endy -93037.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1559 0 cap 1
	color 0 11
 dis 0 picpos begx 64915.904 begy 81712.496 endx 64916.904 endy 81712.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1404 0 cap 1
	color 0 6
 dis 0 picpos begx 82366.472 begy 71742.496 endx 82367.472 endy 71742.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1516 0 cap 1
	color 0 5
 dis 0 picpos begx 121498.552 begy 96612.496 endx 121499.552 endy 96612.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2868 0 cap 1
	color 0 5
 dis 0 picpos begx 74016.448 begy 93722.496 endx 74017.448 endy 93722.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4345 0 cap 1
	color 0 13
 dis 0 picpos begx 106066.088 begy -93037.504 endx 106067.088 endy -93037.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1414 0 cap 1
	color 0 11
 dis 0 picpos begx 97953.472 begy 68512.496 endx 97954.472 endy 68512.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2855 0 cap 1
	color 0 6
 dis 0 picpos begx 72916.448 begy 83187.504 endx 72917.448 endy 83187.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1470 0 cap 1
	color 0 11
 dis 0 picpos begx 105705.472 begy 68512.496 endx 105706.472 endy 68512.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1510 0 cap 1
	color 0 6
 dis 0 picpos begx 119048.552 begy 69162.496 endx 119049.552 endy 69162.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4361 0 cap 1
	color 0 14
 dis 0 picpos begx 118648.552 begy 93412.496 endx 118649.552 endy 93412.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8386 0 cap 1
	color 0 14
 dis 0 picpos begx 106455.472 begy 93412.496 endx 106456.472 endy 93412.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1752 0 cap 1
	color 0 5
 dis 0 picpos begx 83966.472 begy 93722.496 endx 83967.472 endy 93722.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1818 0 cap 1
	color 0 6
 dis 0 picpos begx 28217.124 begy 82362.496 endx 28218.124 endy 82362.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1838 0 cap 1
	color 0 11
 dis 0 picpos begx 30567.124 begy 81712.496 endx 30568.124 endy 81712.496 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4266 0 cap 1
	color 0 6
 dis 0 picpos begx 106966.088 begy -96237.504 endx 106967.088 endy -96237.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1613 0 cap 1
	color 0 6
 dis 0 picpos begx 95103.472 begy 69162.496 endx 95104.472 endy 69162.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block2856 0 cap 1
	color 0 5
 dis 0 picpos begx 74016.448 begy 82587.504 endx 74017.448 endy 82587.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8367 0 cap 1
	color 0 5
 dis 0 picpos begx 121498.552 begy 93722.496 endx 121499.552 endy 93722.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8904 0 cap 1
	color 0 6
 dis 0 picpos begx 103705.472 begy 83187.504 endx 103706.472 endy 83187.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8917 0 cap 1
	color 0 5
 dis 0 picpos begx 104555.472 begy 93722.496 endx 104556.472 endy 93722.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1560 0 cap 1
	color 0 6
 dis 0 picpos begx 62765.904 begy 82362.496 endx 62766.904 endy 82362.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block4323 0 cap 1
	color 0 11
 dis 0 picpos begx 129856.28 begy -96887.504 endx 129857.28 endy -96887.504 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1413 0 cap 1
	color 0 6
 dis 0 picpos begx 82366.472 begy 83187.504 endx 82367.472 endy 83187.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1441 0 cap 1
	color 0 6
 dis 0 picpos begx 96103.472 begy 83187.504 endx 96104.472 endy 83187.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1473 0 cap 1
	color 0 6
 dis 0 picpos begx 103705.472 begy 69162.496 endx 103706.472 endy 69162.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8374 0 cap 1
	color 0 6
 dis 0 picpos begx 120048.552 begy 72052.496 endx 120049.552 endy 72052.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1415 0 cap 1
	color 0 5
 dis 0 picpos begx 83966.472 begy 82587.504 endx 83967.472 endy 82587.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8918 0 cap 1
	color 0 6
 dis 0 picpos begx 103705.472 begy 70942.496 endx 103706.472 endy 70942.496 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9529 0 cap 1
	color 0 14
 dis 0 picpos begx 94703.376 begy 73928.088 endx 94704.376 endy 73928.088 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block8909 0 cap 1
	color 0 5
 dis 0 picpos begx 104555.472 begy 82587.504 endx 104556.472 endy 82587.504 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9531 0 cap 1
	color 0 13
 dis 0 picpos begx 94033.872 begy 73328.088 endx 94034.872 endy 73328.088 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9534 0 cap 1
	color 0 5
 dis 0 picpos begx 93633.872 begy 76817.2 endx 93634.872 endy 76817.2 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
5 5 0 1 1 none
1
310 17
5 5 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block9526 0 cap 1
	color 0 6
 dis 0 picpos begx 93133.872 begy 69516.312 endx 93134.872 endy 69516.312 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
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
