import init_context
sc,sp = init_context.init_context()
df = sp.read.format("csv").option("header","true").option("mode","FAILFAST").option("inferSchema","True").load("Data/2015-summary.csv")
