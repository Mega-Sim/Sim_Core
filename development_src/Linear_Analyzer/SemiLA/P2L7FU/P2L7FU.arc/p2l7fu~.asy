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

BLOCK name Block980 0 cap 1
	color 0 13
 dis 0 picpos begx -133123.504 begy -18176.734 endx -133122.504 endy -18176.734 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block987 0 cap 1
	color 0 14
 dis 0 picpos begx -132623.504 begy -17576.734 endx -132622.504 endy -17576.734 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block822 0 cap 1
	color 0 6
 dis 0 picpos begx -132223.504 begy 4180.508 endx -132222.504 endy 4180.508 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1004 0 cap 1
	color 0 13
 dis 0 picpos begx -133123.504 begy 16019.516 endx -133122.504 endy 16019.516 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block818 0 cap 1
	color 0 11
 dis 0 picpos begx -131573.504 begy 2730.50775 endx -131572.504 endy 2730.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block965 0 cap 1
	color 0 14
 dis 0 picpos begx -132623.48 begy -35115.292 endx -132622.48 endy -35115.292 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block964 0 cap 1
	color 0 13
 dis 0 picpos begx -133123.48 begy -35715.292 endx -133122.48 endy -35715.292 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block71 0 cap 1
	color 0 11
 dis 0 picpos begx -121406.488 begy 2730.50775 endx -121405.488 endy 2730.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block995 0 cap 1
	color 0 14
 dis 0 picpos begx -132623.504 begy 16619.516 endx -132622.504 endy 16619.516 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block25 0 cap 1
	color 0 3
 dis 0 picpos begx -117879.24 begy 1680.50775 endx -117878.24 endy 1680.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block955 0 cap 1
	color 0 14
 dis 0 picpos begx -132623.48 begy -52089.096 endx -132622.48 endy -52089.096 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block954 0 cap 1
	color 0 13
 dis 0 picpos begx -133123.48 begy -52689.096 endx -133122.48 endy -52689.096 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block429 0 cap 1
	color 0 12
 dis 0 picpos begx -74415.728 begy 3380.50775 endx -74414.728 endy 3380.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block172 0 cap 1
	color 0 11
 dis 0 picpos begx -63344.116 begy 2730.50775 endx -63343.116 endy 2730.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1020 0 cap 1
	color 0 13
 dis 0 picpos begx -133123.504 begy 36608.736 endx -133122.504 endy 36608.736 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block600 0 cap 1
	color 0 3
 dis 0 picpos begx -54243.196 begy 1680.50775 endx -54242.196 endy 1680.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block170 0 cap 1
	color 0 12
 dis 0 picpos begx -63944.116 begy 4030.50775 endx -63943.116 endy 4030.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block610 0 cap 1
	color 0 4
 dis 0 picpos begx -110971.264 begy 5080.508 endx -110970.264 endy 5080.508 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1170 0 cap 1
	color 0 13
 dis 0 picpos begx -133123.504 begy -73283.376 endx -133122.504 endy -73283.376 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1171 0 cap 1
	color 0 14
 dis 0 picpos begx -132623.504 begy -72683.376 endx -132622.504 endy -72683.376 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block431 0 cap 1
	color 0 11
 dis 0 picpos begx -42297.264 begy 2730.50775 endx -42296.264 endy 2730.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1011 0 cap 1
	color 0 14
 dis 0 picpos begx -132623.504 begy 37208.736 endx -132622.504 endy 37208.736 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1031 0 cap 1
	color 0 13
 dis 0 picpos begx -133123.504 begy 62313.484 endx -133122.504 endy 62313.484 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block72 0 cap 1
	color 0 4
 dis 0 picpos begx -41551.04 begy 5080.508 endx -41550.04 endy 5080.508 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block132 0 cap 1
	color 0 3
 dis 0 picpos begx -28317.772 begy 1680.50775 endx -28316.772 endy 1680.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1027 0 cap 1
	color 0 14
 dis 0 picpos begx -132623.504 begy 62913.484 endx -132622.504 endy 62913.484 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1084 0 cap 1
	color 0 6
 dis 0 picpos begx -130923.488 begy -84837.488 endx -130922.488 endy -84837.488 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
6 6 0 1 1 none
1
310 17
6 6 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block232 0 cap 1
	color 0 13
 dis 0 picpos begx -29367.772 begy 1030.5078125 endx -29366.772 endy 1030.5078125 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block177 0 cap 1
	color 0 11
 dis 0 picpos begx -14149.945 begy 2730.50775 endx -14148.945 endy 2730.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block175 0 cap 1
	color 0 12
 dis 0 picpos begx -14749.945 begy 4030.50775 endx -14748.945 endy 4030.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block87 0 cap 1
	color 0 13
 dis 0 picpos begx -41401.04 begy 43868.984 endx -41400.04 endy 43868.984 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block83 0 cap 1
	color 0 14
 dis 0 picpos begx -40801.04 begy 5730.508 endx -40800.04 endy 5730.508 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block324 0 cap 1
	color 0 12
 dis 0 picpos begx -58244.516 begy 99562.512 endx -58243.516 endy 99562.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block131 0 cap 1
	color 0 14
 dis 0 picpos begx -28467.772 begy -42737.492 endx -28466.772 endy -42737.492 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block773 0 cap 1
	color 0 4
 dis 0 picpos begx -15844.938 begy 5080.508 endx -15843.938 endy 5080.508 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1283 0 cap 1
	color 0 12
 dis 0 picpos begx -104486.488 begy -84987.488 endx -104485.488 endy -84987.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1276 0 cap 1
	color 0 11
 dis 0 picpos begx -130273.504 begy -85487.488 endx -130272.504 endy -85487.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block602 0 cap 1
	color 0 3
 dis 0 picpos begx 28000.234 begy 1680.50775 endx 28001.234 endy 1680.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block769 0 cap 1
	color 0 11
 dis 0 picpos begx -126606.488 begy 98312.512 endx -126605.488 endy 98312.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block322 0 cap 1
	color 0 11
 dis 0 picpos begx -57644.516 begy 98312.512 endx -57643.516 endy 98312.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block767 0 cap 1
	color 0 12
 dis 0 picpos begx -83995.032 begy 98912.512 endx -83994.032 endy 98912.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block604 0 cap 1
	color 0 3
 dis 0 picpos begx 37986.624 begy 1680.50775 endx 37987.624 endy 1680.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block434 0 cap 1
	color 0 12
 dis 0 picpos begx 53051.472 begy 3380.50775 endx 53052.472 endy 3380.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block181 0 cap 1
	color 0 11
 dis 0 picpos begx 59935.328 begy 2730.50775 endx 59936.328 endy 2730.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block776 0 cap 1
	color 0 4
 dis 0 picpos begx 8414.844 begy 5080.508 endx 8415.844 endy 5080.508 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block330 0 cap 1
	color 0 12
 dis 0 picpos begx -3252.4845 begy 99562.512 endx -3251.4845 endy 99562.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block179 0 cap 1
	color 0 12
 dis 0 picpos begx 59335.328 begy 4030.50775 endx 59336.328 endy 4030.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block441 0 cap 1
	color 0 11
 dis 0 picpos begx 88503.136 begy 2730.50775 endx 88504.136 endy 2730.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block612 0 cap 1
	color 0 4
 dis 0 picpos begx 16489.875 begy 5080.508 endx 16490.875 endy 5080.508 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1281 0 cap 1
	color 0 13
 dis 0 picpos begx -101206.496 begy -87417.488 endx -101205.496 endy -87417.488 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block607 0 cap 1
	color 0 3
 dis 0 picpos begx 70123.16 begy 1680.50775 endx 70124.16 endy 1680.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block75 0 cap 1
	color 0 13
 dis 0 picpos begx -44858.132 begy 96612.512 endx -44857.132 endy 96612.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block640 0 cap 1
	color 0 3
 dis 0 picpos begx -82207.688 begy 97262.512 endx -82206.688 endy 97262.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block763 0 cap 1
	color 0 11
 dis 0 picpos begx -41086.256 begy 98312.512 endx -41085.256 endy 98312.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block289 0 cap 1
	color 0 14
 dis 0 picpos begx -44258.132 begy 69162.512 endx -44257.132 endy 69162.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block328 0 cap 1
	color 0 11
 dis 0 picpos begx -2652.4845 begy 98312.512 endx -2651.4845 endy 98312.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block609 0 cap 1
	color 0 3
 dis 0 picpos begx 83600.576 begy 1680.50775 endx 83601.576 endy 1680.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block334 0 cap 1
	color 0 12
 dis 0 picpos begx 73214.72 begy 99562.512 endx 73215.72 endy 99562.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1284 0 cap 1
	color 0 11
 dis 0 picpos begx -99656.496 begy -99187.488 endx -99655.496 endy -99187.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block749 0 cap 1
	color 0 13
 dis 0 picpos begx -31032.492 begy -68837.488 endx -31031.492 endy -68837.488 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block614 0 cap 1
	color 0 4
 dis 0 picpos begx 52857.92 begy 5080.508 endx 52858.92 endy 5080.508 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block300 0 cap 1
	color 0 3
 dis 0 picpos begx -44108.132 begy 97262.512 endx -44107.132 endy 97262.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block644 0 cap 1
	color 0 4
 dis 0 picpos begx -69406.496 begy 96662.512 endx -69405.496 endy 96662.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block689 0 cap 1
	color 0 4
 dis 0 picpos begx -74901.712 begy -96887.488 endx -74900.712 endy -96887.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block70 0 cap 1
	color 0 11
 dis 0 picpos begx -96756.496 begy -99187.488 endx -96755.496 endy -99187.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block651 0 cap 1
	color 0 3
 dis 0 picpos begx -40497.42 begy 97262.512 endx -40496.42 endy 97262.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block685 0 cap 1
	color 0 3
 dis 0 picpos begx -85795.424 begy -96287.488 endx -85794.424 endy -96287.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block583 0 cap 1
	color 0 4
 dis 0 picpos begx -31182.492 begy -96887.488 endx -31181.492 endy -96887.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block384 0 cap 1
	color 0 12
 dis 0 picpos begx 132093.504 begy 4030.50775 endx 132094.504 endy 4030.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block283 0 cap 1
	color 0 12
 dis 0 picpos begx 132093.504 begy 99562.512 endx 132094.504 endy 99562.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block307 0 cap 1
	color 0 11
 dis 0 picpos begx 73814.72 begy 98312.512 endx 73815.72 endy 98312.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block761 0 cap 1
	color 0 12
 dis 0 picpos begx 48583.86 begy 98912.512 endx 48584.86 endy 98912.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block235 0 cap 1
	color 0 14
 dis 0 picpos begx -30432.492 begy -96237.488 endx -30431.492 endy -96237.488 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block381 0 cap 1
	color 0 3
 dis 0 picpos begx 125770.064 begy 1680.50775 endx 125771.064 endy 1680.50775 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block712 0 cap 1
	color 0 13
 dis 0 picpos begx 125020.064 begy 1030.5078125 endx 125021.064 endy 1030.5078125 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block647 0 cap 1
	color 0 4
 dis 0 picpos begx -31582.444 begy 96662.512 endx -31581.444 endy 96662.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block757 0 cap 1
	color 0 11
 dis 0 picpos begx 89732.84 begy 98312.512 endx 89733.84 endy 98312.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block634 0 cap 1
	color 0 3
 dis 0 picpos begx 10335.484 begy 97262.512 endx 10336.484 endy 97262.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1268 0 cap 1
	color 0 11
 dis 0 picpos begx -46402.92 begy -99187.488 endx -46401.92 endy -99187.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1270 0 cap 1
	color 0 12
 dis 0 picpos begx -47002.92 begy -97937.488 endx -47001.92 endy -97937.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block657 0 cap 1
	color 0 11
 dis 0 picpos begx -87826.064 begy -98537.488 endx -87825.064 endy -98537.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block696 0 cap 1
	color 0 4
 dis 0 picpos begx 118402.28 begy 5080.508 endx 118403.28 endy 5080.508 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block479 0 cap 1
	color 0 11
 dis 0 picpos begx 124770.064 begy -46487.492 endx 124771.064 endy -46487.492 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block346 0 cap 1
	color 0 14
 dis 0 picpos begx 125620.224 begy -43637.488 endx 125621.224 endy -43637.488 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block653 0 cap 1
	color 0 3
 dis 0 picpos begx 105775.808 begy 97262.512 endx 105776.808 endy 97262.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block630 0 cap 1
	color 0 4
 dis 0 picpos begx 673.65625 begy -96887.488 endx 674.65625 endy -96887.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block637 0 cap 1
	color 0 4
 dis 0 picpos begx 23543.5 begy 96662.512 endx 23544.5 endy 96662.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block616 0 cap 1
	color 0 3
 dis 0 picpos begx -8114.4765 begy -96287.488 endx -8113.4765 endy -96287.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block531 0 cap 1
	color 0 4
 dis 0 picpos begx 127372.496 begy 5080.508 endx 127373.496 endy 5080.508 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block660 0 cap 1
	color 0 12
 dis 0 picpos begx 4184.90625 begy -97937.488 endx 4185.90625 endy -97937.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block394 0 cap 1
	color 0 11
 dis 0 picpos begx 22997.968 begy -99187.488 endx 22998.968 endy -99187.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block714 0 cap 1
	color 0 3
 dis 0 picpos begx 126782.032 begy 97262.512 endx 126783.032 endy 97262.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block1274 0 cap 1
	color 0 4
 dis 0 picpos begx 117985.328 begy 96662.512 endx 117986.328 endy 96662.512 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block396 0 cap 1
	color 0 12
 dis 0 picpos begx 22397.968 begy -97937.488 endx 22398.968 endy -97937.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block631 0 cap 1
	color 0 4
 dis 0 picpos begx 43364.688 begy -96887.488 endx 43365.688 endy -96887.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block717 0 cap 1
	color 0 13
 dis 0 picpos begx 126032.032 begy 96612.512 endx 126033.032 endy 96612.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block619 0 cap 1
	color 0 3
 dis 0 picpos begx 34917.344 begy -96287.488 endx 34918.344 endy -96287.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block708 0 cap 1
	color 0 14
 dis 0 picpos begx 128122.496 begy 5730.508 endx 128123.496 endy 5730.508 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block523 0 cap 1
	color 0 13
 dis 0 picpos begx 127522.496 begy 43062.516 endx 127523.496 endy 43062.516 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block501 0 cap 1
	color 0 14
 dis 0 picpos begx 126632.032 begy 70172.512 endx 126633.032 endy 70172.512 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block391 0 cap 1
	color 0 11
 dis 0 picpos begx 77133.736 begy -99187.488 endx 77134.736 endy -99187.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block393 0 cap 1
	color 0 12
 dis 0 picpos begx 76533.736 begy -97937.488 endx 76534.736 endy -97937.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block679 0 cap 1
	color 0 11
 dis 0 picpos begx 30329.048 begy -98537.488 endx 30330.048 endy -98537.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
11 11 0 1 1 none
1
310 17
11 11 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block485 0 cap 1
	color 0 13
 dis 0 picpos begx 127593.056 begy -69737.488 endx 127594.056 endy -69737.488 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
13 13 0 1 1 none
1
310 17
13 13 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block632 0 cap 1
	color 0 4
 dis 0 picpos begx 106802.872 begy -96887.488 endx 106803.872 endy -96887.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block620 0 cap 1
	color 0 3
 dis 0 picpos begx 95710.64 begy -96287.488 endx 95711.64 endy -96287.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
3 3 0 1 1 none
1
310 17
3 3 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block704 0 cap 1
	color 0 14
 dis 0 picpos begx 128193.056 begy -96237.488 endx 128194.056 endy -96237.488 scx 228 scy 170 scz 0.100000003539026

	UserDef	template Millimeters
700 17
14 14 0 1 1 none
1
310 17
14 14 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block705 0 cap 1
	color 0 4
 dis 0 picpos begx 127443.056 begy -96887.488 endx 127444.056 endy -96887.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
4 4 0 1 1 none
1
310 17
4 4 0 1 1 none
4 4 4 4 4 0 0
end
BLOCK name Block669 0 cap 1
	color 0 12
 dis 0 picpos begx 127484.688 begy -97937.488 endx 127485.688 endy -97937.488 scx 170 scy 228 scz 0.100000003539026

	UserDef	template Millimeters
700 17
12 12 0 1 1 none
1
310 17
12 12 0 1 1 none
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
