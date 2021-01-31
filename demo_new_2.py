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
	microplate_name = 'corning_96_wellplate_360ul_flat'
	master 		= protocol.load_labware(microplate_name, '1')
	destination = protocol.load_labware(microplate_name, '2')
	control_1  	= protocol.load_labware(microplate_name, '3')
	control_2 	= protocol.load_labware(microplate_name, '5')
	#
	tiprack_1 = protocol.load_labware('geb_96_tiprack_10ul', '4')
	tiprack_2 = protocol.load_labware('geb_96_tiprack_10ul', '6')
	tiprack_3 = protocol.load_labware('geb_96_tiprack_10ul', '7')
	tiprack_4 = protocol.load_labware('geb_96_tiprack_10ul', '8')
	tipracks_ = [tiprack_1, tiprack_2, tiprack_3, tiprack_4]
	#
	left_pipette = protocol.load_instrument('p10_multi', 'left', tip_racks=tipracks_)
	#
	#left_pipette.pick_up_tip()
	# Change default aspirate speed to 50ul/s, 1/3 of the default
	#left_pipette.flow_rate.aspirate = 50
	#left_pipette.aspirate(100, plate['A1'])   
	# Slow down dispense too
	#left_pipette.flow_rate.dispense = 50
	#left_pipette.dispense(100, plate['B2'])
	#left_pipette.drop_tip()
	#
	left_pipette.transfer(
	    10,
	    master['A1'],
	    destination['A2'],
	    mix_before=(2, 10)# mix 2 times with 50uL before aspirating
	) 
	#