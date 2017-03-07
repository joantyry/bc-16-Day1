def data_type(data):
	   		
	  if type(data) == str:
	    return len(data)
	  elif (data is None):
    
	    return "no value"
	  elif type(data) == bool:
	    if data == True: return True
	    else : return False
	  elif type(data) == int:
	    if data < 100: return "less than 100"
	    elif data> 100: return "more than 100"
	    else : return "equal to 100"
	  elif type(data) == list:
	  	if len(data) < 3:
			return None
		else:
			return data[2]