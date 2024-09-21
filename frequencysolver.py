from ortools.sat.python import cp_model

model = cp_model.CpModel()
solver = cp_model.CpSolver()

freqs = {0:"f1", 1:"f2", 2:"f3"}

an1 = model.NewIntVar(0, 2, "an1")
an2 = model.NewIntVar(0, 2, "an2")
an3 = model.NewIntVar(0, 2, "an3")
an4 = model.NewIntVar(0, 2, "an4")
an5 = model.NewIntVar(0, 2, "an5")
an6 = model.NewIntVar(0, 2, "an6")
an7 = model.NewIntVar(0, 2, "an7")
an8 = model.NewIntVar(0, 2, "an8")
an9 = model.NewIntVar(0, 2, "an9")

model.Add(an1 != an2)
model.Add(an1 != an3)
model.Add(an1 != an4)
model.Add(an2 != an3)
model.Add(an2 != an5)
model.Add(an2 != an6)
model.Add(an3 != an6)
model.Add(an3 != an9)
model.Add(an4 != an2)
model.Add(an4 != an5)
model.Add(an6 != an7)
model.Add(an6 != an8)
model.Add(an7 != an8)
model.Add(an8 != an9)

status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
	print("Antenna 1: %s" % freqs[solver.Value(an1)])
	print("Antenna 2: %s" % freqs[solver.Value(an2)])
	print("Antenna 3: %s" % freqs[solver.Value(an3)])
	print("Antenna 4: %s" % freqs[solver.Value(an4)])
	print("Antenna 5: %s" % freqs[solver.Value(an5)])
	print("Antenna 6: %s" % freqs[solver.Value(an6)])
	print("Antenna 7: %s" % freqs[solver.Value(an7)])
	print("Antenna 8: %s" % freqs[solver.Value(an8)])
	print("Antenna 9: %s" % freqs[solver.Value(an9)])
