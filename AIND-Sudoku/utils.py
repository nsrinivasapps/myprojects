"""
  utils functions related to Suduko project
"""
rows = 'ABCDEFGHI'
cols = '123456789'
#boxes = cross(rows,cols)
def cross(a,b):
    return [x + y for x in a for y in b]

def grid_values(boxes,values):
    #Input:Suduko in String format
    #Suduko in dict form .if no value found..value will be '123456789'
    chars = []
    for c in values:
        if c in digits:
           chars.append(c)
        else c in '.0':
           chars.append(cols)
    assert len(chars) == 81
    return dict(zip(boxes,chars)) 
if __name__ == "__main__":
   boxes = cross(rows,cols)
  # for box in boxes:
   #    print(box)
   
  ## prepare row units
  
   rowUnits = [cross(r,cols) for r in rows]
   print("rowUnits")
   for rU in rowUnits:
       print(rU)
  
   ## prepare col units
   colUnits =  [cross(rows,c) for c in cols]
   print("colUnits")
   for cU in colUnits:
       print (cU)
  
   ## prepare square units
   sqUnits = [cross(r,c) for r in ('ABC','DEF','GHI') for c in ('123','456','789')]
   print("sqUnits")
   for sU in sqUnits:
       print(sU)
   
   #complete unitlist
   unitList = rowUnits + colUnits + sqUnits
   print("unitList")
   for unit in unitList:
       print(unit)

   #fetch unit
   units = dict((s,[u for u in unitList if s in u]) for s in boxes)
   print("units C3")
   #for u in unit['c3']:
   print (units["C3"])
   print (sum(units["C3"],[]))

   # compute peers of a box
   peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
   print("C3 peers")
   print(peers["C3"]) 
  
   grid1 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
   gridValues = grid_ values(boxes,grid1)
