for col_pos in list(range(0, 6)):
	for offset_row in ["A","B"]:
		#print("source col_pos:", col_pos+1)
		#print("dest col_pos:", col_pos*3+4)
		print("source pos:", offset_row+str(col_pos))
		for i in range(0,3):
			print("dest pos: ", offset_row+str(col_pos*3+4+i))
		print("----------------------------")
