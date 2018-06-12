{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 7,
			"minor" : 2,
			"revision" : 3,
			"architecture" : "x86",
			"modernui" : 1
		}
,
		"rect" : [ 99.0, 254.0, 903.0, 804.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"boxes" : [ 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-2",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 469.75, 116.0, 261.0, 23.0 ],
					"style" : "",
					"text" : "/predictArray/ 0.2 0.3 0.1 0.5 0.5 0.2 0.1 0.3"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.412297, 1.0, 0.414311, 1.0 ],
					"fontsize" : 20.0,
					"id" : "obj-8",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 227.0, 296.0, 155.0, 29.0 ],
					"style" : "",
					"text" : "LEARNIG"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.412297, 1.0, 0.414311, 1.0 ],
					"fontsize" : 20.0,
					"id" : "obj-7",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 232.0, 35.0, 1407.0, 29.0 ],
					"style" : "",
					"text" : "OFAPP"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"linecount" : 44,
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 288.0, 428.0, 162.0, 598.0 ],
					"style" : "",
					"text" : "/predict/ 0.373751 0.322069 0.355576 0.344842 0.334515 0.383911 0.304261 0.401507 0.292335 0.402555 0.2851 0.386516 0.294899 0.366247 0.317404 0.370186 0.337156 0.415542 0.351878 0.416811 0.380601 0.43456 0.372548 0.421435 0.357512 0.375616 0.366992 0.300843 0.425104 0.247827 0.433117 0.255356 0.396165 0.314402 0.362614 0.342552 0.35896 0.322225 0.349704 0.355318 0.357157 0.392444 0.376876 0.399009 0.39556 0.374582 0.383336 0.36698 0.331342 0.337865 0.301628 0.323931 0.265016 0.317691 0.274351 0.323636 0.271661 0.309527 0.233112 0.24855 0.206696 0.199127 0.208907 0.249342 0.221648 0.291879 0.195557 0.271078 0.155964 0.228122 0.151496 0.22929 0.125156 0.198422 0.136146 0.177906 0.150063 0.229348 0.189423 0.279893 0.187509 0.337037 0.224562 0.336231 0.266555 0.30079 0.326466 0.274599 0.35452 0.293946 0.359506 0.308488 0.33878 0.291653 0.310824 0.268095 0.27874 0.218079 0.31747 0.171427"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-4",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 247.25, 362.0, 106.0, 23.0 ],
					"style" : "",
					"text" : "udpreceive 2011"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-1",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 505.0, 534.0, 45.0, 22.0 ],
					"style" : "",
					"text" : "/finish/"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-3",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 406.75, 618.0, 151.0, 23.0 ],
					"style" : "",
					"text" : "udpsend 127.0.0.1 2002"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-9",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 270.75, 102.0, 108.0, 23.0 ],
					"style" : "",
					"text" : "/predict/ 0.5 0.05"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-24",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 270.75, 152.0, 150.0, 23.0 ],
					"style" : "",
					"text" : "udpsend 127.0.0.1 2010"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-18",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 686.0, 424.0, 45.0, 22.0 ],
					"style" : "",
					"text" : "/finish/"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-14",
					"linecount" : 2,
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 637.75, 382.0, 103.0, 35.0 ],
					"style" : "",
					"text" : "/pos/ 0.014648 -0.009115"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-10",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 613.75, 491.0, 151.0, 23.0 ],
					"style" : "",
					"text" : "udpsend 127.0.0.1 2001"
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-3", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-1", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-14", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-18", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-24", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-2", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 1 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-24", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-9", 0 ]
				}

			}
 ],
		"dependency_cache" : [  ],
		"autosave" : 0
	}

}
