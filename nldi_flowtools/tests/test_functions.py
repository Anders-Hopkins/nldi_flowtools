from nldi_flowtools.nldi_flowtools import splitcatchment, flowtrace
# from nldi_flowtools import splitcatchment, flowtrace


def test_splitcatchment():
    actual = None
    actual = splitcatchment(-93, 45, True)
    expected = {"features": [{"geometry": {"coordinates": [[[-93.0047, 44.9929], [-93.0053, 44.993], [-93.0051, 44.9944], [-93.0067, 44.9949], [-93.0091, 44.9959], [-93.01, 44.9974], [-93.0105, 44.9986], [-93.0098, 45.0], [-93.0125, 45.0025], [-93.0158, 45.0024], [-93.0169, 45.0033], [-93.0173, 45.0058], [-93.0182, 45.0064], [-93.0195, 45.0075], [-93.0164, 45.009], [-93.0159, 45.0104], [-93.0147, 45.0108], [-93.0147, 45.012], [-93.0178, 45.0116], [-93.0246, 45.0115], [-93.0279, 45.0129], [-93.0302, 45.0133], [-93.0306, 45.0144], [-93.0318, 45.0152], [-93.0323, 45.0156], [-93.0319, 45.0159], [-93.0313, 45.0162], [-93.0307, 45.0168], [-93.0285, 45.0173], [-93.0291, 45.0194], [-93.0257, 45.0199], [-93.0273, 45.0213], [-93.0276, 45.0219], [-93.028, 45.0224], [-93.0283, 45.0235], [-93.0291, 45.0235], [-93.0304, 45.0242], [-93.0296, 45.0251], [-93.0302, 45.0264], [-93.0313, 45.027], [-93.0304, 45.0298], [-93.032, 45.0302], [-93.0324, 45.0302], [-93.0322, 45.0309], [-93.0317, 45.0316], [-93.0323, 45.0329], [-93.0297, 45.0336], [-93.0298, 45.0347], [-93.0277, 45.0363], [-93.0263, 45.0354], [-93.0259, 45.0337], [-93.0256, 45.0318], [-93.0249, 45.032], [-93.0244, 45.0327], [-93.0228, 45.0331], [-93.0218, 45.0328], [-93.0212, 45.0322], [-93.0176, 45.0325], [-93.0162, 45.033], [-93.0134, 45.0318], [-93.0112, 45.0317], [-93.0108, 45.0325], [-93.0103, 45.033], [-93.0099, 45.0349], [-93.008, 45.0356], [-93.0057, 45.0357], [-93.0045, 45.0356], [-93.003, 45.0361], [-93.001, 45.0363], [-93.0003, 45.0372], [-92.9981, 45.0381], [-92.9963, 45.0395], [-92.9963, 45.04], [-92.9952, 45.0413], [-92.9943, 45.0444], [-92.9934, 45.0451], [-92.9927, 45.0455], [-92.9939, 45.046], [-92.995, 45.0469], [-92.9967, 45.048], [-92.9955, 45.0486], [-92.9949, 45.0496], [-92.9936, 45.0506], [-92.9915, 45.0503], [-92.9909, 45.0501], [-92.9897, 45.0499], [-92.989, 45.0486], [-92.9876, 45.0481], [-92.988, 45.0476], [-92.9892, 45.0469], [-92.9891, 45.0454], [-92.9897, 45.0446], [-92.9894, 45.0392], [-92.9889, 45.0389], [-92.9891, 45.0388], [-92.9917, 45.0381], [-92.9925, 45.0368], [-92.9938, 45.0356], [-92.9935, 45.0347], [-92.9921, 45.0338], [-92.992, 45.0334], [-92.9939, 45.0329], [-92.9958, 45.0319], [-92.996, 45.0312], [-92.9953, 45.0303], [-92.9958, 45.0285], [-92.995, 45.027], [-92.9946, 45.0265], [-92.9936, 45.0246], [-92.9952, 45.0238], [-92.9944, 45.023], [-92.9937, 45.0221], [-92.9921, 45.0224], [-92.9907, 45.0227], [-92.9895, 45.0226], [-92.9891, 45.0226], [-92.9883, 45.0225], [-92.9862, 45.0229], [-92.9849, 45.0244], [-92.9842, 45.0263], [-92.9825, 45.0253], [-92.9823, 45.0211], [-92.9816, 45.0197], [-92.9832, 45.0184], [-92.9832, 45.0179], [-92.9834, 45.0169], [-92.9822, 45.0157], [-92.9814, 45.0142], [-92.9803, 45.0136], [-92.9804, 45.013], [-92.9792, 45.0125], [-92.9774, 45.0122], [-92.9768, 45.0134], [-92.9747, 45.0126], [-92.9757, 45.0109], [-92.9789, 45.01], [-92.9792, 45.009], [-92.9772, 45.0079], [-92.9764, 45.0063], [-92.9765, 45.0056], [-92.9764, 45.0047], [-92.9773, 45.0039], [-92.9788, 45.0033], [-92.9804, 45.0035], [-92.9815, 45.0033], [-92.9836, 45.003], [-92.9849, 45.0016], [-92.9844, 45.0006], [-92.9837, 45.0003], [-92.9834, 45.0], [-92.984, 44.9996], [-92.985, 44.9969], [-92.9849, 44.9958], [-92.985, 44.9953], [-92.9866, 44.994], [-92.9871, 44.9931], [-92.9887, 44.9933], [-92.9914, 44.9932], [-92.993, 44.9939], [-92.994, 44.9938], [-92.9949, 44.9939], [-92.9966, 44.9938], [-92.9974, 44.9932], [-93.0001, 44.9949], [-93.0015, 44.9948], [-93.0028, 44.9938], [-93.0037, 44.9935], [-93.0043, 44.9931], [-93.0047, 44.9929]]], "type": "Polygon"}, "id": "catchment", "properties": {"catchmentID": "1100118"}, "type": "Feature"}, {"geometry": {"coordinates": [[[-93.000194, 45.00006], [-93.000206, 44.999791], [-92.999444, 44.999774], [-92.999432, 45.000043], [-93.000194, 45.00006]]], "type": "Polygon"}, "id": "splitCatchment", "properties": {}, "type": "Feature"}], "type": "FeatureCollection"}
    assert actual == expected

    # actual = splitcatchment(-93.06089554438601, 41.65410801168578, False)
    # expected = {"features": [{"geometry": {"coordinates": [[[-93.0688, 41.6547], [-93.0688, 41.6578], [-93.0682, 41.6596], [-93.0687, 41.6608], [-93.0687, 41.6613], [-93.0675, 41.6628], [-93.0673, 41.6643], [-93.0653, 41.6641], [-93.0639, 41.6625], [-93.0635, 41.6618], [-93.0621, 41.6611], [-93.0618, 41.6608], [-93.0616, 41.6607], [-93.0616, 41.6602], [-93.0613, 41.6602], [-93.0607, 41.6594], [-93.0591, 41.6589], [-93.058, 41.6573], [-93.0571, 41.6569], [-93.056, 41.657], [-93.0554, 41.6567], [-93.0545, 41.6556], [-93.052, 41.6551], [-93.0516, 41.654], [-93.0519, 41.6533], [-93.054, 41.6513], [-93.0548, 41.6509], [-93.056, 41.6516], [-93.057, 41.6519], [-93.0592, 41.6507], [-93.0596, 41.6511], [-93.064, 41.6515], [-93.0661, 41.6529], [-93.0665, 41.6539], [-93.0675, 41.6542], [-93.0682, 41.6546], [-93.0688, 41.6547]]], "type": "Polygon"}, "id": "catchment", "properties": {"catchmentID": "6981570"}, "type": "Feature"}, {"geometry": {"coordinates": [[[-93.054925, 41.655718], [-93.054936, 41.65545], [-93.055299, 41.655459], [-93.05531, 41.655191], [-93.055673, 41.655199], [-93.056036, 41.655207], [-93.056047, 41.654939], [-93.05641, 41.654948], [-93.056421, 41.65468], [-93.056784, 41.654688], [-93.057872, 41.654713], [-93.057883, 41.654445], [-93.058246, 41.654453], [-93.060422, 41.654503], [-93.060433, 41.654235], [-93.060796, 41.654243], [-93.061159, 41.654252], [-93.061237, 41.652376], [-93.060512, 41.652359], [-93.060534, 41.651823], [-93.060172, 41.651815], [-93.060194, 41.651279], [-93.059469, 41.651263], [-93.059491, 41.650727], [-93.059128, 41.650719], [-93.059117, 41.650986], [-93.058754, 41.650978], [-93.058392, 41.65097], [-93.058381, 41.651238], [-93.058018, 41.65123], [-93.058007, 41.651497], [-93.057644, 41.651489], [-93.057633, 41.651757], [-93.055819, 41.651716], [-93.05583, 41.651448], [-93.055468, 41.651439], [-93.055479, 41.651171], [-93.055116, 41.651163], [-93.055128, 41.650895], [-93.054402, 41.650879], [-93.054391, 41.651146], [-93.054028, 41.651138], [-93.054017, 41.651406], [-93.053654, 41.651398], [-93.053632, 41.651934], [-93.053269, 41.651925], [-93.053258, 41.652193], [-93.052895, 41.652185], [-93.052873, 41.652721], [-93.05251, 41.652713], [-93.052499, 41.652981], [-93.052136, 41.652972], [-93.052125, 41.65324], [-93.051762, 41.653232], [-93.051695, 41.65484], [-93.052057, 41.654848], [-93.052046, 41.655116], [-93.052771, 41.655133], [-93.05276, 41.655401], [-93.054211, 41.655434], [-93.0542, 41.655702], [-93.054925, 41.655718]]], "type": "Polygon"}, "id": "splitCatchment", "properties": {}, "type": "Feature"}], "type": "FeatureCollection"}
    # assert actual == expected


def test_flowtrace():
    actual = None
    actual = flowtrace(-93.06089554438601, 41.65410801168578, True, "up")
    expected = {"features": [{"geometry": {"coordinates": [[-93.062, 41.6608], [-93.0621, 41.6606], [-93.0623, 41.6605], [-93.0626, 41.66], [-93.0627, 41.6596], [-93.0629, 41.6593], [-93.0645, 41.658], [-93.0665, 41.6566], [-93.0672, 41.6558], [-93.0684, 41.6549]], "type": "LineString"}, "id": "upstreamFlowline", "properties": {"comid": 6981570, "gnis_name": "Sewer Creek", "intersectionPoint": (41.6549, -93.0684), "measure": 3.75, "raindropPathDist": 685.44, "reachcode": "07080105001380"}, "type": "Feature"}, {"geometry": {"coordinates": [[-93.060987, 41.654115], [-93.06135, 41.654123], [-93.061702, 41.6544], [-93.062064, 41.654408], [-93.062427, 41.654416], [-93.06279, 41.654424], [-93.063152, 41.654433], [-93.063515, 41.654441], [-93.063878, 41.654449], [-93.064241, 41.654458], [-93.064603, 41.654466], [-93.064966, 41.654474], [-93.065329, 41.654482], [-93.065691, 41.654491], [-93.066043, 41.654767], [-93.066394, 41.655043], [-93.066757, 41.655051], [-93.067109, 41.655328], [-93.067471, 41.655336], [-93.067845, 41.655076], [-93.0684, 41.6549]], "type": "LineString"}, "id": "raindropPath", "properties": {}, "type": "Feature"}], "type": "FeatureCollection"}
    assert actual == expected

    # actual = flowtrace(-91.55700978897856, 43.36502302924605, True, "none")
    # expected = {"features": [{"geometry": {"coordinates": [[-91.5672, 43.3688], [-91.5669, 43.3689], [-91.5644, 43.3707], [-91.5615, 43.3711], [-91.5593, 43.3721], [-91.5592, 43.3722]], "type": "LineString"}, "id": "nhdFlowline", "properties": {"comid": 13337372, "gnis_name": "Upper Iowa River", "intersectionPoint": (43.3689, -91.5669), "measure": 96.55, "raindropPathDist": 995.51, "reachcode": "07060002000062"}, "type": "Feature"}, {"geometry": {"coordinates": [[-91.55683, 43.364987], [-91.557202, 43.364999], [-91.557573, 43.365012], [-91.557945, 43.365024], [-91.558316, 43.365037], [-91.558688, 43.365049], [-91.559059, 43.365062], [-91.559431, 43.365074], [-91.559802, 43.365087], [-91.560174, 43.3651], [-91.560545, 43.365112], [-91.560899, 43.365393], [-91.561271, 43.365406], [-91.561625, 43.365687], [-91.561979, 43.365968], [-91.562333, 43.366248], [-91.562705, 43.366261], [-91.563077, 43.366274], [-91.563431, 43.366555], [-91.563802, 43.366567], [-91.564156, 43.366848], [-91.564511, 43.367129], [-91.564865, 43.36741], [-91.565219, 43.367691], [-91.565573, 43.367972], [-91.565927, 43.368253], [-91.566282, 43.368534], [-91.5669, 43.3689]], "type": "LineString"}, "id": "raindropPath", "properties": {}, "type": "Feature"}], "type": "FeatureCollection"}
    # assert actual == expected

    # actual = flowtrace(-105.55976687902356, 40.691486512824966, False, "none")
    # expected = {"features": [{"geometry": {"coordinates": [[-105.5803, 40.6981], [-105.5793, 40.6982], [-105.5782, 40.6985], [-105.5778, 40.6988], [-105.5772, 40.6989], [-105.5766, 40.6988], [-105.5757, 40.6984], [-105.5747, 40.6981], [-105.574, 40.6982], [-105.5735, 40.6984], [-105.5725, 40.699], [-105.5719, 40.6992], [-105.5703, 40.6993], [-105.5697, 40.6994], [-105.5673, 40.7009], [-105.567, 40.701], [-105.5666, 40.701], [-105.5661, 40.7007], [-105.5649, 40.6997], [-105.564, 40.6993], [-105.5628, 40.699], [-105.5621, 40.6989], [-105.559, 40.6992], [-105.5562, 40.6992], [-105.5555, 40.6993], [-105.5552, 40.6994], [-105.5543, 40.7], [-105.5538, 40.7002], [-105.5532, 40.7002], [-105.5522, 40.7001], [-105.5511, 40.6997], [-105.5501, 40.6996], [-105.5481, 40.6998], [-105.5471, 40.6998], [-105.5457, 40.6994], [-105.5452, 40.6994], [-105.5438, 40.6998], [-105.5426, 40.6998], [-105.5409, 40.6995], [-105.54, 40.6997], [-105.5392, 40.6999], [-105.5386, 40.6999], [-105.5383, 40.6997], [-105.5381, 40.6993], [-105.5378, 40.6989]], "type": "LineString"}, "id": "nhdFlowline", "properties": {"comid": 2899241, "gnis_name": "Cache la Poudre River", "intersectionPoint": (40.6992, -105.5562), "measure": 42.87, "reachcode": "10190007000308"}, "type": "Feature"}], "type": "FeatureCollection"}
    # assert actual == expected

    # actual = flowtrace(-93,45,True,"down")
    # expected = {"features": [{"geometry": {"coordinates": [[-93.0087, 45.0163], [-93.0092, 45.0163], [-93.0099, 45.0165], [-93.0108, 45.0169], [-93.0111, 45.0169], [-93.0119, 45.0168], [-93.0127, 45.0166], [-93.0133, 45.0166], [-93.0137, 45.0167], [-93.0143, 45.0171], [-93.0143, 45.0172], [-93.0146, 45.0174], [-93.0158, 45.0174], [-93.016, 45.0175], [-93.0166, 45.0179], [-93.0172, 45.0181], [-93.0182, 45.0184], [-93.0192, 45.0186], [-93.0213, 45.0185], [-93.0215, 45.0183], [-93.022, 45.0178], [-93.0223, 45.0176], [-93.0227, 45.0176], [-93.023, 45.0178], [-93.0232, 45.0181], [-93.0233, 45.0184], [-93.0233, 45.0196], [-93.0231, 45.0201], [-93.0231, 45.0209], [-93.0233, 45.0214], [-93.0237, 45.0217], [-93.0237, 45.0219], [-93.0238, 45.0225], [-93.0239, 45.0226], [-93.0244, 45.0227], [-93.0254, 45.0228], [-93.0258, 45.023], [-93.026, 45.0233], [-93.026, 45.0243], [-93.0261, 45.0244], [-93.026, 45.0245], [-93.0262, 45.0247], [-93.0276, 45.0257], [-93.029, 45.0264], [-93.0298, 45.0267], [-93.0303, 45.0267], [-93.0308, 45.0267]], "type": "LineString"}, "id": "downstreamFlowline", "properties": {"comid": 1100118, "gnis_name": "none", "intersectionPoint": [45.0163, -93.0087], "measure": 71.22, "raindropPathDist": 2549.11, "reachcode": "07010206000564"}, "type": "Feature"}, {"geometry": {"coordinates": [[-93.000007, 44.999919], [-93.000388, 44.999928], [-93.000769, 44.999936], [-93.00115, 44.999945], [-93.001531, 44.999953], [-93.001911, 44.999962], [-93.00228, 45.000239], [-93.002661, 45.000248], [-93.003042, 45.000257], [-93.003423, 45.000265], [-93.003803, 45.000273], [-93.004184, 45.000282], [-93.004565, 45.00029], [-93.004553, 45.00056], [-93.004541, 45.000829], [-93.004529, 45.001099], [-93.004517, 45.001368], [-93.004505, 45.001638], [-93.004874, 45.001916], [-93.005255, 45.001924], [-93.005635, 45.001933], [-93.005623, 45.002202], [-93.005992, 45.00248], [-93.00598, 45.00275], [-93.006349, 45.003028], [-93.006337, 45.003297], [-93.006706, 45.003575], [-93.006694, 45.003844], [-93.006682, 45.004114], [-93.00667, 45.004383], [-93.006658, 45.004653], [-93.006646, 45.004922], [-93.006634, 45.005192], [-93.006241, 45.005453], [-93.005848, 45.005714], [-93.005836, 45.005983], [-93.005443, 45.006244], [-93.005431, 45.006514], [-93.0058, 45.006792], [-93.006169, 45.00707], [-93.006538, 45.007348], [-93.006526, 45.007617], [-93.006514, 45.007886], [-93.006502, 45.008156], [-93.00649, 45.008425], [-93.006478, 45.008695], [-93.006466, 45.008964], [-93.006835, 45.009242], [-93.006823, 45.009512], [-93.006811, 45.009781], [-93.006799, 45.010051], [-93.006787, 45.01032], [-93.006775, 45.01059], [-93.006763, 45.010859], [-93.006751, 45.011129], [-93.00712, 45.011406], [-93.007488, 45.011684], [-93.007476, 45.011954], [-93.007464, 45.012223], [-93.007452, 45.012493], [-93.007821, 45.012771], [-93.00819, 45.013049], [-93.008178, 45.013318], [-93.008166, 45.013588], [-93.008154, 45.013857], [-93.008535, 45.013866], [-93.008142, 45.014127], [-93.007749, 45.014388], [-93.007356, 45.014649], [-93.007344, 45.014918], [-93.007332, 45.015188], [-93.00732, 45.015457], [-93.007308, 45.015726], [-93.007296, 45.015996], [-93.007665, 45.016274], [-93.008046, 45.016282], [-93.008427, 45.016291], [-93.0087, 45.0163]], "type": "LineString"}, "id": "raindropPath", "properties": {}, "type": "Feature"}], "type": "FeatureCollection"}
    # assert actual == expected
