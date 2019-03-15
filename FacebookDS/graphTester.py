import snap

UG = snap.LoadEdgeList(snap.PUNGraph, "test.txt", 0, 1)
UG.Dump()

snap.DrawGViz(UG, snap.gvlDot, "graphTester.png", "Graph Tester")
