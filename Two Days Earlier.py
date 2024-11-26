from datetime import datetime, timedelta

def main(event):
  tedate = int(event.get("inputFields").get("ted"))
  tedate = tedate / 1000
  tedate = datetime.utcfromtimestamp(tedate)
  print("Transition End Date = ",tedate)
  twodaysearlier = tedate - timedelta(days = 2)
  tdetimestamp = int(twodaysearlier.timestamp() * 1000)
  twodateearly = datetime.utcfromtimestamp(tdetimestamp/1000)
  print("Two Days Earlier to the Transition End Date = ", twodateearly)
  ctimestamp = datetime.now().timestamp()
  cdate = datetime.utcfromtimestamp(ctimestamp)
  print("Current Date = ", cdate)
  if tdetimestamp == ctimestamp:
    notify = 1
  else:
    notify = 0
  return {
    "outputFields": {
      "notify": notify
    }
  }