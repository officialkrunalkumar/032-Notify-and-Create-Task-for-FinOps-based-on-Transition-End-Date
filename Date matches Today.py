from datetime import datetime, timedelta

def main(event):
  createtask = 0
  tedate = int(event.get("inputFields").get("ted"))
  tedate = tedate / 1000
  tedate = datetime.utcfromtimestamp(tedate)
  print("Transition End Date = ",tedate)
  ctimestamp = datetime.now().timestamp()
  cdate = datetime.utcfromtimestamp(ctimestamp)
  print("Current Date = ", cdate)
  if cdate == tedate:
    createtask = 1
  return {
    "outputFields": {
      "createtask": createtask
    }
  }