def valid_Pin(x):    
    
  if len(x) != 4 and len(x) != 6: 
    return False
  elif x.isdigit() == False:
    return False
  elif x.isspace() == True:
    return False
  else:
    return True   
   

def test_answer():
    assert valid_Pin("") == False
    assert valid_Pin("1234") == True
    assert valid_Pin("45135") ==  False
    assert valid_Pin("89abc1") ==  False
    assert valid_Pin("900876") ==  True
    assert valid_Pin(" 4983") ==  False