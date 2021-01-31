from opentrons import protocol_api
# metadata
metadata = {
    'protocolName': 'My Protocol',
    'author': 'Name <email@address.com>',
    'description': 'Simple protocol to get started using OT2',
    'apiLevel': '2.9'
}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions

def run(protocol):
	# labware
	microplate_name = 'corning_384_wellplate_112ul_flat'
	master 		= protocol.load_labware(microplate_name, '1')
	destination = protocol.load_labware(microplate_name, '2')
	control_1  	= protocol.load_labware(microplate_name, '3')
	control_2 	= protocol.load_labware(microplate_name, '5')
	#
	tipracks_ = [protocol.load_labware('geb_96_tiprack_10ul', str(slot))
            for slot in ['4', '6', '7', '8']]
	#
	left_pipette = protocol.load_instrument('p10_multi', 'left', tip_racks=tipracks_)
	#
	#left_pipette.pick_up_tip()
	# Change default aspirate speed to 50ul/s, 1/3 of the default
	left_pipette.flow_rate.aspirate = 10
	#left_pipette.aspirate(100, plate['A1'])   
	# Slow down dispense too
	left_pipette.flow_rate.dispense = 200
	#left_pipette.dispense(100, plate['B2'])
	#left_pipette.drop_tip()
	#
	"""
	source = master['A1']
	for well_pos in ['A4', 'A5', 'A6']:
		left_pipette.pick_up_tip()
		left_pipette.mix(2, 10)
		left_pipette.transfer(5, source.bottom(2), destination[well_pos].top(-2), new_tip='never')
		left_pipette.touch_tip()
		left_pipette.drop_tip()
	#
	source = master['B1']
	for well_pos in ['B4', 'B5', 'B6']:
		left_pipette.pick_up_tip()
		left_pipette.mix(2, 10)
		left_pipette.transfer(5, source, destination[well_pos], new_tip='never')
		left_pipette.touch_tip()
		left_pipette.drop_tip()
	#
	source = master['A2']
	for well_pos in ['A7', 'A8', 'A9']:
		left_pipette.pick_up_tip()
		left_pipette.mix(2, 10)
		left_pipette.transfer(5, source, destination[well_pos], new_tip='never')
		left_pipette.touch_tip()
		left_pipette.drop_tip()
	#
	source = master['B2']
	for well_pos in ['B7', 'B8', 'B9']:
		left_pipette.pick_up_tip()
		left_pipette.mix(2, 10)
		left_pipette.transfer(5, source, destination[well_pos], new_tip='never')
		left_pipette.touch_tip()
		left_pipette.drop_tip()
	#
	source = master['A3']
	for well_pos in ['A10', 'A11', 'A12']:
		left_pipette.pick_up_tip()
		left_pipette.mix(2, 10)
		left_pipette.transfer(5, source, destination[well_pos], new_tip='never')
		left_pipette.touch_tip()
		left_pipette.drop_tip()
	#
	source = master['B3']
	for well_pos in ['B10', 'B11', 'B12']:
		left_pipette.pick_up_tip()
		left_pipette.mix(2, 10)
		left_pipette.transfer(5, source, destination[well_pos], new_tip='never')
		left_pipette.touch_tip()
		left_pipette.drop_tip()

	"""

	#for col_pos in list(range(4,21, 3)):
	for col_pos in list(range(0, 6)):
		for offset_row in ["A","B"]:
			#print("source col_pos:", col_pos+1)
			#print("dest col_pos:", col_pos*3+4)
			#print("source pos:", offset_row+str(col_pos+1))
			source = master[offset_row+str(col_pos+1)]
			#for well_pos in ['A4', 'A5', 'A6']:
			for i in range(0,3):
				#print("dest pos: ", offset_row+str(col_pos*3+4+i))
				well_pos = offset_row+str(col_pos*3+4+i)
				left_pipette.pick_up_tip()
				#left_pipette.mix(2, 10)
				left_pipette.transfer(5, source.bottom(2), destination[well_pos].top(-2), new_tip='never')
				#left_pipette.touch_tip()
				left_pipette.drop_tip()




"""
	left_pipette.transfer(
	    5,
	    master['B1'],
	    [destination[well_pos] for well_pos in ['B4', 'B5', 'B6']],
	    mix_before=(2, 10),# mix 2 times with 50uL before aspirating
	    touch_tip=True,
	    new_tip='always'#'always' or 'never' or 'once'
	) 
"""
	#----------------------------------------------



#https://docs.opentrons.com/v2/new_complex_commands.html