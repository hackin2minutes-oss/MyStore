from pytm import TM, Actor, Datastore, Dataflow, Server, Boundary

tm = TM("MyStore Threat Model")

# Trust Boundaries
internet = Boundary("Internet")
app_tier = Boundary("Application Tier")

# Elements
user = Actor("User / Browser", inBoundary=internet)
web_app = Server("MyStore Web App", inBoundary=app_tier, sourceFiles=["MyStore/"])
database = Datastore("App Database", inBoundary=app_tier, sourceFiles=["MyStore/"])

# Dataflows
flow1 = Dataflow(user, web_app, "HTTPS Request", protocol="HTTPS", dstPort=443, order=1)
flow2 = Dataflow(web_app, database, "Database Query", protocol="TCP", dstPort=1433, order=2)

if __name__ == "__main__":
    tm.process()
