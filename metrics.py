import sys

if len(sys.argv) == 1:
	metrics = ["user growth", "user churn", "user retention", "funding", "ARR", "MRR", "team size", "experience"]
	output = ""
	for metric in metrics:
		output += "db.recipes.update({\"autocomplete\":\""+metric+"\"}, {\"autocomplete\":\""+metric+"\"}, {upsert:true});\n"
	print output
else:
	s = ""
	metrics = []
	for arg in sys.argv[1:]:
		s += arg + " "
	metrics = s[0:-1].split(', ')
	output = ""
	for metric in metrics:
		output += "db.recipes.insert({\"autocomplete\":\""+metric+"\"});\n"
	print output

