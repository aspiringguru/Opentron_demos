"""
#open dos shell
cmd
d:
cd D:\2020\coding\anne_EC50\robot
opentron_venv\Scripts\activate.bat
opentrons_simulate.exe demo_new_4.py

NB: .mix & .touch steps commented out during code testing
refer "for matthew.ods" for explanation of plates and movements.
"""

from opentrons import protocol_api
# metadata
metadata = {
    'protocolName': 'TimTamDemo1',
    'author': 'Matthew <bmatthewtaylor@gmail.com>',
    'description': 'protocol for demo',
    'apiLevel': '2.9'
}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions

def run(protocol):
    #
    f = open('transfer_pos_records.csv','w')
    # labware
    microplate_name = 'corning_384_wellplate_112ul_flat'
    master 		= protocol.load_labware(microplate_name, '1')
    destination1 = protocol.load_labware(microplate_name, '2')
    destination2 = protocol.load_labware(microplate_name, '6')#check position
    destination3 = protocol.load_labware(microplate_name, '7')#check position
    destination4 = protocol.load_labware(microplate_name, '8')#check position
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
    print("type(master):", type(master))
    print("type(destination1):", type(destination1))
    print("type(destination2):", type(destination2))
    print("type(destination3):", type(destination3))
    print("type(destination4):", type(destination4))
    print("type(control_1):", type(control_1))
    print("type(control_2):", type(control_2))
    print("type(tipracks_):", type(tipracks_))
    print("type(left_pipette):", type(left_pipette))
    #
    #control1 from col2 to destination col2 and 22.
    for col_pos in [2,22]:
        for offset_row in ["A","B"]:
            source_pos = offset_row+str(2)#pickup from control1 col 2
            source = control_1[source_pos]
            well_pos = offset_row+str(col_pos)
            csv_string = source_pos+","+well_pos
            print(csv_string)
            left_pipette.pick_up_tip()
            left_pipette.mix(2, 10)
            left_pipette.transfer(5, source.bottom(2), destination1[well_pos].top(-2), new_tip='never')
            left_pipette.touch_tip()   #reinstate .touch step for production
            left_pipette.drop_tip()
            f.write("control1: "+csv_string+"\n")
    #
    #control2 from col2 to destination col3 and 22.
    for col_pos in [3,23]:
        for offset_row in ["A","B"]:
            source_pos = offset_row+str(2)#pickup from control2 col 2
            source = control_2[source_pos]
            well_pos = offset_row+str(col_pos)
            csv_string = source_pos+","+well_pos
            print(csv_string)
            left_pipette.pick_up_tip()
            left_pipette.mix(2, 10)
            left_pipette.transfer(5, source.bottom(2), destination1[well_pos].top(-2), new_tip='never')
            left_pipette.touch_tip()   #reinstate .touch step for production
            left_pipette.drop_tip()
            f.write("control2: "+csv_string+"\n")
#    f.close()
    #this section runs fine, commented out during coding of control section.
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
                left_pipette.mix(2, 10)    #reinstate .mix step for production.
                f.write("destination: "+offset_row+str(col_pos+1)+","+well_pos+"\n")
                left_pipette.transfer(5, source.bottom(2), destination1[well_pos].top(-2), new_tip='never')
                left_pipette.touch_tip()   #reinstate .touch step for production
                left_pipette.drop_tip()
    #
    f.close()
"""
    ctrl_1 = [well for well in control_1.cols(control_column)[:2]]
    ctrl_2 = [well for well in control_2.cols(control_column)[:2]]
    #err below : 'Labware' object has no attribute 'cols'
    ctrl_1_dest = [[destination.cols(col_num)[index]
                   for col_num in ['2', '22']]
                   for index in range(2)]
    ctrl_2_dest = [[destination.cols(col_num)[index]
                    for col_num in ['3', '23']]
                    for index in range(2)]

"""
"""
	for source, dests in zip(ctrl_1, ctrl_1_dest):
	    for dest in dests:
	        m10.pick_up_tip()
	        m10.mix(1, 10)
	        m10.transfer(control_volume, source.bottom(2), dest.top(-4), new_tip='never')
	        m10.blow_out()
	        m10.touch_tip()
	        m10.drop_tip()

	for source, dests in zip(ctrl_2, ctrl_2_dest):
	    for dest in dests:
	        m10.pick_up_tip()
	        m10.mix(1, 10)
	        m10.transfer(control_volume, source.bottom(2), dest.top(-4), new_tip='never')
	        m10.blow_out()
	        m10.touch_tip()
	        m10.drop_tip()
"""




#https://docs.opentrons.com/v2/new_complex_commands.html
